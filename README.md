# Phononette
## Sujet
Le but du stage est de développer Phononette, une base de données dérivationnelle à grande échelle. Cette base de données doit être munie d'annotations permettant une description fine des alternances formelles (morphophonologiques) dans le lexique construit. Elle confirmerait empiriquement un ensemble d'hypothèses théoriques sur la manière dont les locuteurs perçoivent plus ou moins spontanément la proximité lexicale entre deux mots présentant des variations formelles.

## Première approche
La première approche abordée pour développer Phononette consiste à récupérer les relations dérivationnelles du français présentant des variations rares. La première étape (de cette première approche) est d'essayer de collecter les formes supplétives telles qu'elles sont définies dans les rubriques étymologiques de Kaikki. Donc pour le moment vous trouverez essentiellement des codes "expérimentaux" qui me permettent d'identifier :
- le meilleur modèle (GPT-oss, Phi-3, Qwen…?), 
- le meilleur type de prompt (concis, plus étoffé, few shot ?), 
- le meilleur "environnement d'exécution" (Google Colab, Grid5000 ?),
- le meilleur combo des trois caractéristiques précédentes (few shot sur Grid5000 avec le modèle Llama3.2 ou sans few shot sur Grid5000 avec le modèle Phi-3 mini ?…).  

## Données
Kaikki est une version structurée du Wiktionnaire. Pour télécharger les données fr-extract.jsonl.gz dirigez-vous vers ce lien : https://kaikki.org/dictionary/rawdata.html (quand vous y serez, descendez un peu avec la souris et vous tomberez dessus).

## Codes
Tous les codes se trouvent dans le dossier src. Il y a deux types : des notebooks avec l'extension ipynb utilisés sur Google Colab et des scripts avec l'extension py utilisés sur Grid5000. La plupart des notebooks Colab m'ont juste servi à tester mon code avant de le lancer sur Grid5000, donc les scripts Grid ne sont qu'une adaptation des notebooks. Pour mieux comprendre à quoi sert chaque code, je vous renvoie au fichier documentation_src.md que vous trouverez également dans le dossier src.

## Résultats
Tous les résultats au format csv se trouvent dans le dossier Results. Une fois dans le dossier Results vous trouverez deux sous-dossiers, un, intitulé Colab, et l'autre, Grid. 

Dans Colab vous trouverez les résultats de la plupart des notebooks et pour mieux comprendre quel fichier csv correspond à quel prompt, je vous renvoie au fichier documentation_results_Colab.md que vous trouverez également dans le dossier Results/Colab. 

Dans Grid vous trouverez les résultats de tous les scripts et pour mieux comprendre quel fichier csv correspond à quel prompt, je vous renvoie au fichier documentation_results_Grid.md que vous trouverez également dans le dossier Results/Grid.

Je vais faire un fichier qui résume les points forts et points faibles de chaque prompting, avec des remarques (mais pour le moment je n'ai pas encore eu le temps de faire ça au propre).

## Prochaine étape 
Mon nouveau but est de trouver un moyen d'avoir les formes supplétives et leur traduction. Par exemple, pour ovipare, mon LLM a récolté ov et pare et moi j'aimerais trouver un moyen d'avoir automatiquement ov = œuf, pare = qui produit. En plus de ce nouveau but, je cherche toujours un moyen d'améliorer mon prompting parce que, pour beaucoup d'entrées, je n'ai pas encore de super bons résultats.
