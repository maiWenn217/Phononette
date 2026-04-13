# Phononette
## Sujet
Le but du stage est de développer Phononette, une base de données dérivationnelle à grande échelle. Cette base de données doit être munie d'annotations permettant une description fine des alternances formelles (morphophonologiques) dans le lexique construit. Elle confirmerait empiriquement un ensemble d'hypothèses théoriques sur la manière dont les locuteurs perçoivent plus ou moins spontanément la proximité lexicale entre deux mots présentant des variations formelles.

## Première approche
La première approche abordée pour développer Phononette consiste à récupérer les relations dérivationnelles du français présentant des variations rares. La première étape (de cette première approche) est d'essayer de collecter les formes supplétives telles qu'elles sont définies dans les rubriques étymologiques de Kaikki. Vous trouverez des codes "expérimentaux" qui permettent d'identifier :
- le meilleur modèle (GPT-oss, Phi-3, Qwen…?), 
- le meilleur type de prompt (concis, plus étoffé, few shot ?), 
- le meilleur "environnement d'exécution" (Google Colab, Grid5000 ?),
- le meilleur combo des trois caractéristiques précédentes (few shot sur Grid5000 avec le modèle Llama3.2 ou sans few shot sur Grid5000 avec le modèle Phi-3 mini ?…).

La deuxième étape consiste à construire un jeu de données gold standard pour évaluer les réponses des modèles. La partie contexte est extraite automatiquement à partir de Kaikki et de la base de données Démonette, et la partie réponses est annotée manuellement. 

## Données
Toutes les données se trouvent dans le dossier data, je vous renvoie au fichier documentation_data.md pour plus de détails. Les données contextuelles sont majoritairement extraites de Kaikki. La base de données Démonette est utilisée pour apporter des informations sur la famille dérivationnelle de chaque mot du jeu de données. Le jeu de données gold standard issu, entre autres, de l'extraction de Kaikki et Démonette, se trouve dans le dossier data/gold. 

## Codes
Tous les codes se trouvent dans le dossier src. Dans le sous-dossier tests, vous trouverez les codes ayant servi à l'étape 1 : les tests. Il y a deux types de code : des notebooks avec l'extension ipynb utilisés sur Google Colab et des scripts avec l'extension py utilisés sur Grid5000. La plupart des notebooks Colab m'ont juste servi à tester mon code avant de le lancer sur Grid5000, donc les scripts Grid ne sont qu'une adaptation des notebooks. Pour mieux comprendre à quoi sert chaque code, je vous renvoie au fichier documentation_src_tests.md que vous trouverez également dans le dossier src. En dehors du dossier tests vous trouverez le code ayant servi à l'étape 2 : la création du jeu de données gold standard. Pour plus de détails sur ce code, je vous renvoie au fichier documentation_src.md. 

## Résultats
Tous les résultats au format csv se trouvent dans le dossier results/tests. Une fois dans le dossier results/tests vous trouverez deux sous-dossiers, un, intitulé Colab, et l'autre, Grid. 

Dans Colab vous trouverez les résultats de la plupart des notebooks et pour mieux comprendre quel fichier csv correspond à quel prompt, je vous renvoie au fichier documentation_results_Colab.md que vous trouverez également dans le dossier results/tests/Colab. 

Dans Grid vous trouverez les résultats de tous les scripts et pour mieux comprendre quel fichier csv correspond à quel prompt, je vous renvoie au fichier documentation_results_Grid.md que vous trouverez également dans le dossier results/tests/Grid.

Un fichier qui résume les points forts et points faibles de chaque prompting, avec des remarques, est disponible dans le dossier results (analysis_results.md).

## Prochaine étape 
Le jeu de données étant créé, il ne reste plus qu'à tester différents modèles et trouver des métriques pour pouvoir les évaluer. 
