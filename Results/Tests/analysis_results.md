# Analyse des tests

Après analyse des résultats de chaque test, on peut conclure que **Grid5000** est largement plus pratique à utiliser que Google Colab, car il permet d'utiliser de meilleurs modèles. Parmi les modèles utilisés sur Grid5000, **phi3:mini** donne de bons résultats et est plus rapide, voire meilleur que Llama 3.2.

Un prompt plus étoffé n'est peut-être pas la meilleure idée : ajouter toujours plus de règles peut rendre le prompt trop strict et rejeter énormément de données. Trop de règles peut aussi embrouiller le LLM, et certaines règles peuvent se contredire. Rester sur un **prompt simple et concis** semble plus efficace.

Les données étant toujours mauvaises, l'ajout d'exemples dans le prompt (few-shot prompting) a été testé. Cela s'est avéré bénéfique pour certaines entrées (notamment les affixations), mais l'amélioration globale reste limitée.

Après les tests, un petit jeu de données _gold standard_ sera construit en se concentrant uniquement sur des catégories pertinentes pour analyser la dérivation :

- Nom commun
- Verbe
- Adjectif

Les dérivations affixales seront privilégiées, car elles sont nombreuses et plus facilement identifiées par le LLM, notamment grâce au few-shot prompting. Ce jeu de données servira à évaluer la performance des LLM.

# Résumé des tests
| Test | Modèle | Environnement | Observations | 
|-------|-------|---------------|--------------|
| Test 1 | Llama 3.2 | Grid5000 | Très peu de réponses, nombreuses inventions |
| Test 2 | gpt-oss | Colab | Plus de réponses mais encore des inventions |
| Test 3 | Llama 3.2 | Grid5000 | Résultats incohérents |
| Test 4 | phi3:mini | Grid5000 | Plus rapide mais irrégulier |
| Test 5 | gpt-oss (few-shot) | Colab | Meilleure stabilité |
| Test 6 | phi3:mini | Grid5000 | Pas d'amélioration notable |

# Détails des tests
## Test 1 Llama 3.2 (Grid5000)
- prompt simple :

_Tu es un assistant qui répond efficacement aux questions à partir d'un fichier JSON qui contient plusieurs informations à propos d'un mot. Tu ne dois pas donner d'explications, tu ne dois pas raisonner, tu ne dois pas reformuler la tâche.

L'enregistrement en JSON suivant : {json_entry} contient un mot du français, une catégorie, une définition et une étymologie. Construis un nouvel enregistrement JSON qui contient les réponses aux questions suivantes :
        * Q1 = quelle est la langue d'origine du mot qui est indiquée dans l'étymologie ? (un seul mot ou NULL si l'information est absente)
        * Q2 = quelle est la base du mot qui est indiquée dans l'étymologie ? (un seul mot ou NULL si l'information est absente)
        * Q3 = si un préfixe est indiqué dans l'étymologie, quel est ce préfixe ? (un seul mot ou NULL si l'information est absente)
        * Q4 = si un suffixe est indiqué dans l'étymologie, quel est ce suffixe ? (un seul mot ou NULL si l'information est absente)
        * Q5 = si des composants sont indiqués dans l'étymologie, quels sont ces composants ? (liste de composants ou NULL si l'information est absente)
        * Q6 = si le type du procédé morphologique est indiqué dans l'étymologie (suffixation, préfixation, composition, conversion, apocope, etc.), quel est ce type ? (un seul mot ou NULL si l'information est absente)_
        
- donne très peu de réponses (18/140)
- gros décalage, les réponses ne correspondent pas aux entrées pour une grosse partie des données, par exemple : pour l'entrée "ouvrage" nous avons les réponses de l'entrée "siège" à la place
- ce problème découle sûrement du fait que Llama 3.2 répond en minuscules "q1" à la place de "Q1", "q2" à la place de "Q2" etc. et beaucoup de réponses ont été rejetées car je n'acceptais que le format en capitales => il s'agit de quelque chose à changer pour le prochain test
- ce problème de format de sortie prouve que le LLM est irrégulier puisque parfois il répond en minuscules et parfois en capitales => il faut trouver un moyen de rendre les données plus uniformes en forçant le LLM à répondre d'une certaine manière ou en prenant un modèle plus cohérent (consistency) pour le prochain test
- pour les cas où le modèle a donné une réponse, nous remarquons qu'il a beaucoup inventé, par exemple : pour le mot "accueil" on a l'étymologie "Déverbal de accueillir." et on a comme réponse "lang:grec, base:ancien, pref:en-, suff:e, comps:['ancien, grec'], type:composition", rien à voir avec ce qui est dit dans l'étymologie
- réponses très mauvaises (quand il y en a)

## Test 2 gpt-oss (Colab)
- prompt plus (peut-être trop ?) avec ajout de règles et rappel strict du format de sortie pour forcer le LLM à répondre au format suivant : {"Q1" : "", "Q2" : "", ...} :
Tu es un assistant d'extraction d'information.
  Règles :
  - tu ne dois pas donner d'explications, tu ne dois pas raisonner et tu ne dois pas reformuler la tâche
  - tu ne dois rien déduire
  - tu dois répondre uniquement avec un JSON valide
  - il ne doit y avoir aucun texte avant ou après le JSON
  - les réponses sont en minuscules et sans déterminant
  - le JSON doit être sur une seule ligne

[...]

Réponds uniquement avec ce de JSON :
        * 'Q1' : ' ',
        * 'Q2' : ' ',
        * 'Q3' : ' ',
        * 'Q4' : ' ',
        * 'Q5' : [ ],
        * 'Q6' : ' '
        Si l'information n'est pas explicitement présente dans l'étymologie ou la définition, répondre NULL. Ne jamais déduire ou supposer une information.

- les clés (q1, q2, q3…) ont été automatiquement mises en capitales après la sortie du modèle, ce qui veut dire que si un modèle répond en minuscules, la réponse n'est pas rejetée et nous avons donc beaucoup plus de réponses et aucun décalage
- quelques inventions notables, par exemple : pour le mot "siège" nous avons l'étymologie "Du latin sediculum (« siège, chaise, banquette ») diminutif de sedes, devenu en bas latin *sedicum de là siège. Il est lié au verbe latin sedere (« asseoir »)." et comme réponse "lang:latin, base:sedes, pref: , suff: , comps:['sedes', 'sedere'], type:suffixation", la suffixation a été inventée car n'est pas mentionnée dans l'étymologie, et en plus ce n'est pas la bonne réponse, nous pouvons quand même mentionner qu'il ne s'agit plus d'invention totale comme le précédent test
- nous avons beaucoup plus de réponses mais des inventions sont récurrentes => essayer un autre modèle pour voir si le problème vient du modèle ou du prompt

## Test 3 Llama 3.2 (Grid5000)
- même prompt que le test 2
- invente toujours, seulement 2 cas d'invention totale dans les 50 premières entrées (le cas de manchot et Allemands) mais plusieurs petites inventions ça et là
- phénomène d'influence, pour deux entrées consécutives et presque identiques (Allemande et Allemands), lorsque la première entrée a un contexte étymologique mais pas la seconde, le LLM invente des réponses pour la seconde sur le calque de la précédente
- extrait aléatoirement, le LLM a bien compris qu'il devait se baser sur ce qu'on lui donnait mais il prend des mots de la définition et de l'étymologie (alors que le prompt dit de ne regarder que l'étymologie), de manière aléatoire, pour créer des composants, par exemple : pour le mot "encyclopédie" nous avons l'étymologie "Du latin encyclopaedia forgé à la Renaissance, fausse lecture d’un manuscrit pour ἐγκύκλοπαιδεία ; mot tiré du grec ancien ἐγκύκλιος, énkúklios (« circulaire ») — voir encyclique — et παιδεία, paideía (« instruction ») soit le sens de « éducation comprenant l’ensemble de toutes les sciences »." et comme réponse "comps:['grec', 'latin']", la réponse n'est pas cohérente du tout avec ce qui est demandé d'autant plus qu'on s'attendait à retrouver énkúklios et paideía
- les réponses restent mauvaises dans l'ensemble

## Test 4 Phi3:mini (Grid5000)
- même prompt que les tests 2 et 3
- invente toujours
- ne donne pas de réponses uniformes, répond nan, NULL, null, liste vide, ['NULL']... - beaucoup plus rapide que Llama 3.2, génère 538 entrées en 2h quand Llama 3.2 en génère 140
- les mêmes problèmes que Llama 3.2 mais plus rapide

## Test 5 gpt-oss avec few-shot (Colab)
- ajout de deux exemples au prompt (few-shot prompting) dans l'espoir de limiter les inventions : 
contexte 1 :
L'enregistrement en JSON suivant : {'mot':'ouvrage', 'catégorie':'Nom commun', 'définition':['Travail ; action de travailler.'], 'étymologie':"['Dérivé de ouvrer, ancienne forme de œuvrer, avec le suffixe -age.']"} contient un mot du français, une catégorie, une définition et une étymologie. Construis un nouvel enregistrement JSON qui contient les réponses aux questions suivantes :
[...]
réponse 1 :
{"Q1":"français", "Q2":"ouvrer", "Q3":null, "Q4":"-age", "Q5":null, "Q6":"suffixation"}

contexte 2 :
L'enregistrement en JSON suivant : {'mot':'week', 'catégorie':'Nom commun', 'définition':['Week-end.'], 'étymologie':"['Apocope de week-end.']"} contient un mot du français, une catégorie, une définition et une étymologie. Construis un nouvel enregistrement JSON qui contient les réponses aux questions suivantes :
[...]
réponse 2 :
{"Q1":null, "Q2":"week", "Q3":null, "Q4":null, "Q5":null, "Q6":"apocope"}
- quand le LLM ne sait pas, il ne répond pas, au lieu d'inventer ou d'extraire aléatoirement un mot
- format de réponse régulier
- repère mieux les suffixations/préfixations que les tests précédents
- le prompt n'améliore pas significativement les réponses mais il a donné des résultats plutôt satisfaisants et surprenants, par exemple : pour le mot "blog", le LLM a trouvé qu'il s'agissait d'une aphérèse alors que pour tous les autres tests il avait été identifié comme étant une composition
- le choix des exemples a un rôle à jouer dans l'efficacité du LLM à répondre correctement, un exemple de suffixation a été mis, donc pour les affixations, les LLM est meilleur, un exemple d'apocope a été mis, donc pour les procédés qui touchent à la troncation comme l'aphérèse et la syncope, le LLM est meilleur => si nous nous concentrons sur les affixations en dérivation, il est plutôt pertinent de faire du few-shot prompting pour améliorer les résultats

## Test 6 Phi3:mini avec few-shot (Grid5000)
- même prompt que le test 5
- mêmes remarques que pour le test 5, n'est pas significativement meilleur
