# Description des fichiers
- gold_context.ipynb est un notebook qui permet de générer automatiquement le contexte étymologique, la définition et la famille des 100 mots présélectionnés, à partir de Kaikki et Démonette. Pour tourner, ce notebook a besoin de la liste des 100 mots présélectionnés, des données Kaikki et des données sur les lexèmes et les familles de Démonette. Toutes les données sont stockées dans le dossier data. 
- gold_context_extended.ipynb est un notebook qui permet d'étendre le contexte étymologique 

# Description des dossiers 
## Dossier tests
Ce dossier regroupe tous les scripts permettant d'identifier la meilleure combinaison prompt/modèle/environnement d'exécution. Pour en savoir plus sur chaque fichier, une documentation, documentation_src_tests.md, est disponible. 

## Dossier initial_context
Ce dossier regroupe le script utilisé pour interroger Mistral sur le contexte initial.

## Dossier extended_context
Ce dossier regroupe tous les scripts permettant d'interroger chaque LLM (Mistral, Deepseek, Llama, Gemma et Qwen) sur le contexte étendu.

## Dossier italian_context 
Ce dossier regroupe le script permettant d'interroger Qwen sur le contexte italien. 
