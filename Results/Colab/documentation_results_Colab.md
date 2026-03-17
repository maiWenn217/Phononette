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

- test_gpt_oss correspond à la sortie du notebook Colab_Kaikki_tests.ipynb avec le prompt de Nabil appliqué sur un morceau de données + le modèle GPT-oss.
- tests_csv_saved_v2 correspond à la sortie du notebook Colab_sauvegarde_csv_chunk_par_chunk.ipynb avec le prompt de Nabil modifié appliqué sur le plus de données possible + le modèle GPT-oss.
- tests_csv_few_shot correspond à la sortie du notebook Colab_few_shot_prompting.ipynb avec le prompt de Nabil modifié et deux exemples appliqué sur le plus de données possible + le modèle GPT-oss.

Tous les notebooks sont stockés dans le dossier src. 