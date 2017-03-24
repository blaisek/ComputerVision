
# Cahier des charges

## Détection d’objets en mouvement
###   Descriptif : 

La reconnaissance d’objets fait partie des technologies classiques liées au traitement du signal les plus employées. Une difficulté supplémentaire survient lorsque les objets à reconnaître sont en mouvement. Ors, le traitement de ce cas de figure est couramment nécessaire.

Des outils logiciels existent pour nous aider à traiter les différentes facettes de ce type de reconnaissance, notamment les outils de traitement d’images en temps réel.

Le présent travail propose d’explorer les solutions du marché et de l’appliquer à un cas d’étude à définir. L’objet choisi devra pouvoir aussi être détecté s’il est en mouvement dans une direction prédéterminée.



### Objectifs:

Créer un programme qui en prenant en entré le flux vidéo d'une caméra ip  pourra détecter le passage d'un objet devant un plan fixe.


### Tâches :

1. 
Réalisation du cahier des charges détaillé.


2. 
État de la technique du domaine.


3. 
Proposition d’une solution adaptée au cas d’étude choisi.


4. 
Réalisation d’un démonstrateur du cas d’étude. (Une vidéo enregistrée fera l'affaire)

5.
Fournir un mémoire en quatre tirages papier et l'accès aux codes sources, un résumé et une présentation orale. 


## Journal d'avancement du projet
### 15 mars 2017:
- Etat de la technique du domaine: 
BMC , Background Models Substraction, est une méthode souvent utilisée pour la détection de mouvement d'objet , en soustrayant le background d'un plan fixe, on isole en foreground tout objet qui passe dans le plan.   
- Proposition: 
Trouver un algorithme qui à partir de la matrice foreground obtenue par BMC , évalue si le contour de l'objet en mouvement ressemble plus ou moins à celui de l'objet de référence, par tâtonnement en mettant un objet dans le foreground pour extraire sa matrice. Puis faire la recherche de corrélation à un point précis du passage pour avoir la forme entière de l'objet.

### 22 mars 2017:
- Création d'un dépot gitHub 
- Réalisation du cahier des charges détaillé au format markdown
- installation d'opencv et des outils de développement sur la machine ubuntu en salle 505
- test 

% effectué:
100%
#### Objectif suivant:

Travailler sur les algorithmes de flux vidéo sur téléphone android en attendant la caméra IP commandée 
étudier et écrire sur la détection de mouvement 
### 24 mars 2017
- Mise en forme du mémoire avec le logiciel latex , page de titre fait et énoncé ajouté.
- recherche sur l'état de l'art
