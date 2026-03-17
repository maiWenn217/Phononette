Tous les fichiers csv ont la même structure : 
|lemma | cat | def | etym | lang | base | pref | suff | comps | type |
|------|-----|-----|------|------|------|------|------|-------|------|
|      |     |     |      |      |      |      |      |       |      |
lemma = lemme
cat = catégorie
def = définition
etym = étymologie
lang = langue 
base = base 
pref = préfixe 
suff = suffixe 
comps = composants 
type = type de procédé

- test_llama correspond à la sortie du script Grid_test_llama_csv.py avec le prompt de Nabil appliqué sur le plus de données possible + le modèle Llama3.2.
- test_new_prompt_llama correspond à la sortie du script Grid_test_new_prompt_llama.py avec le prompt de Nabil modifié appliqué sur le plus de données possible + le modèle Llama3.2.
- test_new_prompt_phi3 correspond à la sortie du script Grid_test_new_prompt_phi3.py avec le prompt de Nabil modifié appliqué sur le plus de données possible + le modèle Phi-3 mini.
- test_few_shot_phi3 correspond à la sortie du script Grid_test_few_shot_phi3.py avec le prompt de Nabil modifié et deux exemples appliqué sur le plus de données possible + le modèle Phi_3 mini.

Tous les scripts sont stockés dans le dossier src. 