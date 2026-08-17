# Description du contenu des dossiers

## Dossier tests
Au tout début du projet nous avons effectué des tests sur différents modèles, avec différents prompts, sur Grid5000, sur Google Colab, etc. Cette phase de tests nous a permis de nous familiariser avec les données Kaikki et nous a permis d'avoir une idée de quel prompt et quel modèle nous allions utilisé pour commencer à travailler sur notre dataset.
Dans le dossier tests nous pouvons trouver deux sous-dossiers : Grid5000 et Colab, qui correspondent respectivement à des scripts utilisés sur Grid et des notabooks utilisés sur Google Colab. Une analyse des résultats a été faite et est retrouvable dans le fichier analysis_results.md. Ce fichier offre une conclusion sur ce qui a marché et cea moins bien marché selon les tests.

## Dossier initial_context
Grâce aux tests précédemment effectués nous avons détermine quel était le contexte à donner au LLM. Le contexte a donc été fourni au modèle Mistral de deux façons différentes : avec un mélange préalable des entrées et sans mélange. Le fichier Mistral_responses_shuffled.csv correspond aufichier de résultats où les données ont été mélangées et le fichier Mistral_responses.csv correspond au fichier de résultats où les données n'ont pas été mélangées. 

## Dossier extended_context
Suite aux évaluations menées sur les résultats du modèle Mistral, nous avons pu constater que le contexte était lacunaire. De ce fait, nous avons étendu tout particulièrement le contexte étymologique et nous avons testé ce nouveau contexte étendu sur différents modèles (Mistral, Deepseek, Llama, Gemma et Qwen). Les résultats pour chaque modèle sont donc trouvables dans ce dossier.

## Dossier italian_context
Par simple curiosité, nous avons voulu voir si notre méthodologie pouvait fonctionner sur une autre langue que le français. Nous avons donc créé un nouveau contexte contenant des entrées supplétives italiennes et avons testé notreméthodologie sur le meilleur modèle: Qwen. Le fichier résultats correspondant se trouve donc dans ce dossier.

# Résultats et analyses
Les résultats des métriques d'évaluation et les conclusions que nous pouvons tirer sontexplicitées dans le mémoire Creation_lexicon_suppletive_stems.pdf.
