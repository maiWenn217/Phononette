# Phononette
## Sujet
Le projet général consiste à développer Phononette, une base de données dérivationnelle à grande échelle. Cette base de données doit être munie d'annotations permettant une description fine des alternances formelles (morphophonologiques) dans le lexique construit. Elle confirmerait empiriquement un ensemble d'hypothèses théoriques sur la manière dont les locuteurs perçoivent plus ou moins spontanément la proximité lexicale entre deux mots présentant des variations formelles.

L'objectif du stage consiste d'abord à développer BREF, une Base de données des Radicaux supplétifs sur critère Etymologique du Français. Cette base répertorierait tous les radicaux supplétifs existants pour chaque lexème (hipp-, éq-, caval- ... pour CHEVAL). 

## Première étape : tests et construction d'un jeu de données gold standard
La première étape est d'essayer de collecter les formes supplétives telles qu'elles sont définies dans les rubriques étymologiques de Kaikki. Vous trouverez des codes "expérimentaux" qui permettent d'identifier :
- le meilleur modèle (GPT-oss, Phi-3, Qwen…?), 
- le meilleur type de prompt (concis, plus étoffé, few shot ?), 
- le meilleur "environnement d'exécution" (Google Colab, Grid5000 ?),
- le meilleur combo des trois caractéristiques précédentes (few shot sur Grid5000 avec le modèle Llama3.2 ou sans few shot sur Grid5000 avec le modèle Phi-3 mini ?…).

Suite à ces expérimentations, nous avons construit un jeu de données gold standard pour évaluer les réponses des modèles. La partie contexte est extraite automatiquement à partir de Kaikki et de la base de données Démonette, et la partie réponses est annotée manuellement. 

Toutes les données se trouvent dans le dossier data, je vous renvoie au fichier documentation_data.md pour plus de détails. Les données contextuelles sont majoritairement extraites de Kaikki. La base de données Démonette est utilisée pour apporter des informations sur la famille dérivationnelle de chaque mot du jeu de données. Le jeu de données gold standard issu, entre autres, de l'extraction de Kaikki et Démonette, se trouve dans le dossier data/gold. 

Tous les codes se trouvent dans le dossier src. Dans le sous-dossier tests, vous trouverez les codes ayant servi pour les expérimentations. Il y a deux types de code : des notebooks avec l'extension ipynb utilisés sur Google Colab et des scripts avec l'extension py utilisés sur Grid5000. La plupart des notebooks Colab m'ont juste servi à tester mon code avant de le lancer sur Grid5000, donc les scripts Grid ne sont qu'une adaptation des notebooks. Pour mieux comprendre à quoi sert chaque code, je vous renvoie au fichier documentation_src_tests.md que vous trouverez également dans le dossier src. En dehors du dossier tests vous trouverez le code ayant servi à de construction de création du jeu de données gold standard. Pour plus de détails sur ce code, je vous renvoie au fichier documentation_src.md. 

Tous les résultats au format csv se trouvent dans le dossier results/tests. Une fois dans le dossier results/tests vous trouverez deux sous-dossiers, un, intitulé Colab, et l'autre, Grid. Dans Colab vous trouverez les résultats de la plupart des notebooks et pour mieux comprendre quel fichier csv correspond à quel prompt, je vous renvoie au fichier documentation_results_Colab.md que vous trouverez également dans le dossier results/tests/Colab. Dans Grid vous trouverez les résultats de tous les scripts et pour mieux comprendre quel fichier csv correspond à quel prompt, je vous renvoie au fichier documentation_results_Grid.md que vous trouverez également dans le dossier results/tests/Grid. Un fichier qui résume les points forts et points faibles de chaque prompting, avec des remarques, est disponible dans le dossier results (analysis_results.md).

## Deuxième étape : évaluation des premiers résultats
Le script issu de la phase de tests et qui tire partie des conclusions faites se trouve dans le dossier src/initial_context. 

Les premiers résultats sont d'abord annotés manuellement (toutes les annotations se trouvent dans le dossier evaluation/annotation). Ensuite, les scores humains sont comptabilisés et des métriques automatiques sont créées pour pouvoir approximer les scores humains. Vous retrouverez deux notebooks dansle dossier evaluation qui renvoient à l'évaluation humaine et à l'évaluation automatique (voir le fichier documentation_evaluation.md pour plus de détails). 

## Troisième étape : améliorer les résultats 
Pour améliorer les résultats nous avons : 1) étendu le contexte étymologique et 2) tester différents modèles. Le notebook ayant permis d'étendre le contexte étymologique se trouve dans le dossier src. Les scripts permettant de tester les différents modèles sur le contexte étymologique étendu se trouvent dans le dossier src/extended_context. Les résultats des différents modèles sur le contexte étendu se trouvent dans le dossier results/extended_context.

## Etape bonus : test sur une autre langue
Par curiosité nous avons testé notre méthodologie sur une autre langue que le français : l'italien. Pour ce faire, le jeu de données gold standard de l'italien se trouve dans le dossier data/gold. Les entrées sélectionnées ainsi que leur catégorie pour créer le contexte à donner au LLM se trouve dans data, ansi que le contexte lui-même. Le script utilisé pour interroger Qwen sur le contexte italien se trouve dans le dossier src/italian_contexte et le fichier des résultats se trouvent dans le dossier results/italian_context. 

Toutes les analyses de résultats ainsi que les différentes comparaisons entre les différents modèles, contextes et prompts sont explicitées dans le mémoire Creation_lexicon_suppletive_stems.pdf. 

## Prochaine étape 
La prochaine étape consistera à appliquer la méthodologie mise au point à grande échelle, c’est-à-dire à tous les lexèmes d’origine française disponibles dans Kaikki, et non plus uniquement aux 100 entrées de notre ensemble de données de référence. Cette extension nécessite tout d’abord d’intégrer les améliorations identifiées : révision de la consigne, meilleure définition des concepts morphologiques attendus et limitation du contexte étymologique étendu, afin d’éviter de propager les erreurs et les confusions observées dans notre échantillon.
