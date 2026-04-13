# Description des fichiers csv 

Tous les fichiers csv ont la même structure : 
|lemma | cat | def | etym | lang | base | pref | suff | comps | type |
|------|-----|-----|------|------|------|------|------|-------|------|
|      |     |     |      |      |      |      |      |       |      |

lemma = lemme ;
cat = catégorie ;
def = définition ;
etym = étymologie ;
lang = langue ;
base = base ;
pref = préfixe ;
suff = suffixe ;
comps = composants ;
type = type de procédé

- tests_gpt_oss.csv correspond à la sortie du notebook Colab_Kaikki_tests.ipynb avec le prompt original (celui que Nabil m'a envoyé) appliqué sur un morceau de données + le modèle GPT-oss.
- tests_csv_saved_v2.csv correspond à la sortie du notebook Colab_sauvegarde_csv_chunk_par_chunk.ipynb avec le prompt modifié appliqué sur le plus de données possible + le modèle GPT-oss.
- tests_csv_few_shot.csv correspond à la sortie du notebook Colab_few_shot_prompting.ipynb avec le prompt modifié + deux exemples appliqué sur le plus de données possible + le modèle GPT-oss.

# Où trouver les notebooks
Tous les notebooks sont stockés dans le dossier src/tests. 
