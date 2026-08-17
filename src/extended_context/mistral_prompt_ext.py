import pandas as pd
import json
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

shuffle = True
max_trials = 5
chunk_size = 10 # mettre un diviseur de 100
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.3" # à changer selon le modèle

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, trust_remote_code=True)
model.to(device)
model.eval()

all_contexts = pd.read_csv("./gold_context_extended.csv") # à changer selon le contexte
if shuffle :
  all_contexts = all_contexts.sample(frac=1, random_state=42)
full_df = pd.DataFrame()

for chunk_index in range(0, len(all_contexts) // chunk_size ) : 
  chunk = all_contexts.iloc[chunk_index * chunk_size : (chunk_index + 1) * chunk_size]
  list_of_dict = chunk.to_dict("records")

  with open("chunk_context.jsonl", "w", encoding="utf-8") as f :
    for d in list_of_dict :
      f.write(json.dumps(d, ensure_ascii=False) + "\n")

  json_entries = []

  with open("chunk_context.jsonl", "r", encoding="utf-8") as f :
    for line in f :
      json_entry = json.loads(line)
      json_entries.append(json_entry)

  llm_responses = []

  SYSTEM_PROMPT = """Tu es un assistant qui répond efficacement aux questions à partir d'un fichier JSON 
  qui contient plusieurs informations à propos d'un mot. Tu ne dois pas donner d'explications, tu ne dois pas raisonner, 
  tu ne dois pas reformuler la tâche."""

  nb_trials = 0
  json_entry_index = 0
  while json_entry_index < len(json_entries) :

    if nb_trials >= max_trials :
      llm_responses.append( {"Q1": ["FAIL"], "Q2": ["FAIL"], "Q3": "FAIL", "Q4": ["FAIL"], "Q5": "FAIL", "Q6": "FAIL", "Q7": ["FAIL"]}  )
      nb_trials = 0
      json_entry_index += 1
      continue

    json_entry = json_entries[json_entry_index]
    
    # print("json_entry :", json_entry)
    prompt = f"""L'enregistrement en JSON suivant : {json_entry} contient un mot du français, une catégorie, une définition, une étymologie, une étymologie étendue, une déclinaison et une famille de mots. Construis un nouvel enregistrement JSON qui contient les réponses aux questions suivantes : 
    * Q1 = si c'est un mot dérivé, quel est le type de procédé morphologique ? (répondre une liste d'un seul élément s'il n'y a qu'un seul procédé morphologique ou une liste de plusieurs éléments s'il y a plusieurs procédés morphologiques ou une liste vide si le mot n'est pas dérivé)
    * Q2 = quel est l'affixe du mot d'après l'étymologie et l'étymologie étendue ? (répondre une liste d'un seul élément s'il n'y a qu'un seul affixe ou une liste de plusieurs éléments s'il y a plusieurs affixes ou une liste vide si le mot n'est pas dérivé)
    * Q3 = quel est le radical du mot ? (répondre null si le mot n'est pas dérivé)
    * Q4 = quels sont les étymons qu'on retrouve dans l'étymologie et l'étymologie étendue et quel est leur sens ? (répondre une liste de couples étymon, sens ou une liste vide si le mot n'est pas dérivé)
    * Q5 = quelle est la langue source du mot ? (répondre un seul mot ou null si le mot n'est pas dérivé)
    * Q6 = quelle est la base française du mot ? (répondre un seul mot ou null si le mot n'est pas dérivé)
    * Q7 = à partir de la famille, quels sont les mots ayant le même radical ? (répondre une liste de ces mots ou une liste vide si le mot n'est pas dérivé)
     
    Réponds uniquement avec un unique objet JSON valide de cette forme :
    {{
      "Q1": [],
      "Q2": [],
      "Q3": "",
      "Q4": [],
      "Q5": "",
      "Q6": "",
      "Q7": []
    }}

    Contraintes strictes :
    - Ne renvoie pas une liste
    - Ne renvoie pas de texte avant ou après
    """

    messages = [{"role": "system", "content": SYSTEM_PROMPT}, 
                {"role": "user", "content": prompt}]
    
    formatted_prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(formatted_prompt, return_tensors="pt").to(device)

    with torch.no_grad():
      outputs = model.generate(
             **inputs,
              max_new_tokens=5000, # 1000 c'est trop peu 
              temperature=0.1,
              do_sample=False,
              pad_token_id=tokenizer.eos_token_id
          )

    generated_tokens = outputs[0][inputs["input_ids"].shape[-1]:]
    content = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()

    print("Réponse :", content)

    try :
      data = json.loads(content)
    except Exception as e :
      print("Réponse JSON invalide :", e)
      nb_trials += 1
      continue

    new_data = {}
    for k, v in data.items() :
      new_data[k.upper()] = v

    data = new_data

    if list(data.keys())[0] == "Q1" and list(data.keys())[1] == "Q2" and list(data.keys())[2] == "Q3" and list(data.keys())[3] == "Q4" and list(data.keys())[4] == "Q5" and list(data.keys())[5] == "Q6" and list(data.keys())[6] == "Q7" :
      llm_responses.append(data)
      json_entry_index += 1
      nb_trials = 0
    else :
      nb_trials += 1

  df_llm_responses = pd.DataFrame(llm_responses)
  df_llm_responses = df_llm_responses.rename(columns={"Q1": "proc", "Q2": "aff", "Q3": "rad", "Q4": "etym_mean", "Q5": "lang", "Q6": "base", "Q7": "etym_fam"})
  chunk = chunk.rename(columns={"mot": "lemma", "catégorie": "cat", "définition": "def", "étymologie": "etym", "famille": "fam"}).reset_index(drop = True)
  chunk_llm_responses_concat = pd.concat([chunk, df_llm_responses], axis=1)

  if len(full_df) == 0 :
    full_df = chunk_llm_responses_concat
    full_df.to_csv(f"./Mistral_responses_{'shuffled' if shuffle else 'unshuffled'}.csv", index=False) # à changer selon le modèle 
  else :
    full_df = pd.concat([full_df, chunk_llm_responses_concat], axis=0)
    full_df.to_csv(f"./Mistral_responses_{'shuffled' if shuffle else 'unshuffled'}.csv", index=False) # à changer selon le modèle