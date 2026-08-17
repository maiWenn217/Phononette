Chaque fichier contient les différents scores attribués pour chaque entrée selon la question. Des guidelines différentes ont été créées pour chaque question. 

## Guidelines proc_annotation.csv
0 : il a répondu faux alors que l'information était dans le contexte (1) ou n'a rien répondu alors que l'information était dans le contexte (qu'elle soit implicite (-ite)(2) ou explicite (suffixe -ite)(3))		
		
0.5 : il n'a rien répondu mais l'information n'était pas dans le contexte (4) ou il a répondu faux en extrayant quelque chose qui provenait du contexte tandis que ce contexte ne contenait pas l'information du procédé (5)		
		
1 : tout bon (6)		

actinique (1)	céphalaire (2)	fabisme (3) bibition (4)	antifébrile (5)	adipeux (6)		

## Guidelines aff_annotation.csv
0 : réponse fausse, n'a rien à voir avec ce qu'on attendait (1) 

0.5 : se rapproche fortement de ce qu'on attendait (2)

1 : réponse juste (3)

chthonien (1) carnassier (2) funiculaire (3)

## Guidelines rad_annotation.csv
0 : réponse fausse, ne correspond pas à ce qu'on attendait (1) ou le découpage est jugé non pertinent (2)	
	
0.5 : se rapproche fortement de ce qu'on attendait et la réponse est cohérente en termes de découpage et la séquence est retrouvable dans l'entrée (3)	
	
1 : réponse juste (4)	

sigillaire (1) 	viaire (2) crustacé (3)	coturnisme (4)	

## Guidelines etym_mean_annotation.csv
0 : a répondu quelque chose qui n'était pas un étymon même si le sens était bon (1) ou n'a rien répondu alors qu'il y avait un étymon à extraire dans le contexte (2)		
		
0.5 : quand on attendait plusieurs étymons, le LLM en a donné qu'un qui était juste et qui s'avère être le plus important à extraire (3) ou n'a rien répondu et il n'y avait pas d'étymon à extraire du contexte (4) ou quand on attendait qu'un seul étymon, en donne deux, dont un est la bonne réponse, et l'autre n'a rien à voir (5)		
		
1 : a tout juste (6) (en acceptant des variations du genre la forme du verbe qui peut être soit infinitive, soit supin, soit participe passé, tant que ça fait référence au même verbe (7), et les sens aussi peuvent contenir des variations (8))		

caprin (1)	caséeux (2)	chthonien (3) ovoïde (4)	kérosène (5) thélite (6) potable (7) igné (8)

## Guidelines lang_annotation.csv 
0 : mauvaise réponse (1)	
	
0.5 : réponse pertinente, mais pas totalement jsute (2)	
	
1 : réponse juste (3) (en acceptant certaines variantes vraiment pertinentes (4))	

gigantesque (1) polyadelphe (2)	visible (3)	bibition (4)

## Guidelines base_annotation.csv
0 : a répondu quelque chose qui n'a rien à voir avec ce qu'on attendait, quand à la place de la base il répond l'étymon (1), l'entrée elle-même (2) ou le radical (3), ou ne répond rien alors que l'information est dans le contexte (4)			
			
0.5 : a répondu quelque chose qui s'approche de ce qu'on attendait (5)					
			
1 : a répondu juste (6)			

divitisme (1)	cardiaque (2)	foliacé (3)	marmoréen (4) oblation (5) céleste (6) 			

## Guidelines etym_fam_annotation.csv 
0 : il y a trop de mots qui ne correspondent pas à ce qu'on veut (1) ou répond quelque chose qui n'est pas pertinent alors qu'on n'attendait aucune réponse (2)	
	
0.5 : donne tous les mots attendus mais l'entrée aussi (3) ou a donné tous, ou quasiment tous les mots attendus en plus d'une petite erreur (4)	
	
1 : a répondu avec des mots pertinents (5)	

potable (1)	thalassique (2) caséeux (3)	thélite (4) oblation (5)	
