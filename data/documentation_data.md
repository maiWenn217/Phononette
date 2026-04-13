# Description des données 

La majorité des données sont extraites de Kaikki. Kaikki est une version structurée du Wiktionnaire. Le fichier fr-extract.jsonl.gz sur lequel nous nous basons est la version du 03-03-2026. Le fichier étant trop lourd, il n'est pas disponible dans le répertoire mais téléchargeable au lien suivant : https://kaikki.org/dictionary/rawdata.html.

- selected_entries.csv est une liste de 100 mots manuellement présélectionnés et leur catégorie, pour chaque mot, le contexte étymologique, la définition et la famille seront extraits de Kaikki

- lexemes.csv et families.csv renferment toutes les informations concernant les lexèmes de la base de données Démonette ainsi que la famille de chaque lexème, les fichiers sont utilisés pour compléter la colonne famille

- gold_context.csv correspond à la sortie du notebook gold_context.ipynb, il s'agit du contexte des 100 mots, automatiquement extrait à partir de Kaikki et Démonette, à donner aux LLM pour la génération de réponses

## Dossier gold

- gold_dataset.csv est le jeu de données gold standard utilisé pour l'évaluation des réponses des LLM
- gold_dataset_explanations.md explique la création du jeu de données gold standard

