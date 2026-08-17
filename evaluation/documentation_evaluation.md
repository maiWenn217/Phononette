# Etapes d'évaluation des résultats
## Phase d'évaluation humaine
Tout d'abord nous avons mené une évaluation qualitative des résultats en attribuant des scores. Chaque question possède sa propre grille d'évaluation (subjective). Les fichiers contenant les scores attribués pour chaque entrée et pour chaque question se trouvent dans le dossier "annotation". Ainsi, dans ce dossier, nous retrouvons 7 fichiers, un par question. Par exemple, le fichier aff_annotation.csv contient les scores attribués pour les 100 entrées sur la question de l'affixe. 

Ensuite nous avons comptabilisé les scores, avons calculé une moyenne par question et avons fait quelques études plus poussées pour avoir une idée du type d'entrées qui fonctionnait bien pour une question précise, etc. Toutes ces évaluations se trouvent dans le notebook human_evaluation.ipynb.

## Phase d'évaluation automatique
Finalement, à partir de l'évaluation humaine, nous avons créé des métriques pour approximer les scores humains. En effet, une fois que nous passerons de 100 entrées à des milliers d'entrées, nous ne pourrons plus évaluer manuellement les résultats, nous serons obligés d'automatiser l'évaluation pour éviter de perdre du temps. Ces métriques ont donc été créées et ont été elles-mêmes évaluées à l'aide de tests statistiques (RMSE, r de Pearson, t-test, Kappa de Cohen). Toutes les métriques d'évaluation se trouvent dans le notebook automated_evaluation.ipynb. 
