# Imports
import pandas as pd
import ollama
import json

# Préparation du fichier JSONL
df = pd.read_json("./fr-extract.jsonl.gz", lines=True, chunksize=10) # le path du fichier Kaikki
full_df = pd.DataFrame()

for chunk in df :
  try :
     only_french_df = chunk[chunk["lang"] == "Français"][["word", "pos_title", "senses", "etymology_texts"]]
  except Exception as e :
    print(e)
    print(chunk)
    continue
  only_french_df["senses"] = only_french_df["senses"].apply( lambda x: x[0]["glosses"] if isinstance(x, list) and len(x) > 0 and "glosses" in x[0] else None )
  only_french_df = only_french_df.rename(columns={"word": "mot", "pos_title": "catégorie", "senses": "définition", "etymology_texts": "étymologie"})
  list_of_dict = only_french_df.to_dict("records")

  with open("chunk.jsonl", "w", encoding="utf-8") as f :
       for d in list_of_dict :
            f.write(json.dumps(d, ensure_ascii=False) + "\n")

  json_entries = []

  with open("chunk.jsonl", "r", encoding="utf-8") as f :
      for line in f :
          json_entry = json.loads(line)
          json_entries.append(json_entry)

  llm_responses = [] 
  bad_llm_responses = []

  SYSTEM_PROMPT = """Tu es un assistant d'extraction d'information.
  Règles :
  - tu ne dois pas donner d'explications, tu ne dois pas raisonner et tu ne dois pas reformuler la tâche
  - tu ne dois rien déduire
  - tu dois répondre uniquement avec un JSON valide
  - il ne doit y avoir aucun texte avant ou après le JSON
  - les réponses sont en minuscules et sans déterminant
  - le JSON doit être sur une seule ligne"""

  for json_entry in json_entries : 
    prompt = f"""l'enregistrement en JSON suivant : {json_entry} contient un mot du français, une catégorie, une définition et une étymologie. Construis un nouvel enregistrement JSON qui contient les réponses aux questions suivantes :
        * Q1 = quelle est la langue d'origine du mot qui est indiquée dans l'étymologie ? (un seul mot ou NULL si l'information est absente)
        * Q2 = quelle est la base du mot qui est indiquée dans l'étymologie ? (un seul mot ou NULL si l'information est absente)
        * Q3 = si un préfixe est indiqué dans l'étymologie, quel est ce préfixe ? (un seul mot ou NULL si l'information est absente)
        * Q4 = si un suffixe est indiqué dans l'étymologie, quel est ce suffixe ? (un seul mot ou NULL si l'information est absente)
        * Q5 = si des composants sont indiqués dans l'étymologie, quels sont ces composants ? (renvoie une liste de ces composants, sinon renvoie NULL)
        * Q6 = si le type du procédé morphologique est indiqué dans l'étymologie (suffixation, préfixation, composition, conversion, apocope, etc.), quel est ce type ? (un seul mot ou NULL si l'information est absente)
        Réponds uniquement avec ce de JSON :
        * 'Q1' : ' ',
        * 'Q2' : ' ',
        * 'Q3' : ' ',
        * 'Q4' : ' ',
        * 'Q5' : [ ],
        * 'Q6' : ' '
        Si l'information n'est pas explicitement présente dans l'étymologie ou la définition, répondre NULL. Ne jamais déduire ou supposer une information.
        """

    response = ollama.chat(
            model="phi3:mini", # le nom du modèle
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {"role": "user", "content": prompt},
            ],
            format="json"
        )
    print(f"Réponse : {response['message']['content']}")

    content = response["message"]["content"]
    data = json.loads(content)

    new_data = {}

    for k, v in data.items() : 
      new_data[k.upper()] = v

    data = new_data
    
    if list(data.keys())[0] == "Q1" and list(data.keys())[1] == "Q2" and list(data.keys())[2] == "Q3" and list(data.keys())[3] == "Q4" and list(data.keys())[4] == "Q5" and list(data.keys())[5] == "Q6" :
      llm_responses.append(data) 
    else : 
      bad_llm_responses.append(data)

  df_llm_responses = pd.DataFrame(llm_responses)
  df_llm_responses_modified = df_llm_responses.rename(columns={"Q1": "lang", "Q2": "base", "Q3": "pref", "Q4": "suff", "Q5": "comps", "Q6": "type"})
  only_french_df_modified = only_french_df.rename(columns={"mot": "lemma", "catégorie": "cat", "définition": "def", "étymologie": "etym"}).reset_index(drop = True)
  small_llm_responses_concat = pd.concat([only_french_df_modified, df_llm_responses_modified], axis=1)

  if len(full_df) == 0 :
    full_df = small_llm_responses_concat
    full_df.to_csv("./test_new_prompt_phi3.csv", index=False) # le path du dossier où le csv doit être sauvegardé
  else :
    full_df = pd.concat( [full_df, small_llm_responses_concat], axis=0 ) 
    full_df.to_csv("./test_new_prompt_phi3.csv", index=False) # le path du dossier où le csv doit être sauvegardé