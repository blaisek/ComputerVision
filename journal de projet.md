
# Journal de projet


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
### 26 mars 2017
- recherche sur l'état de l'art 
### 28 mars 2017
- exercices sur openCV avec android + JNI framework et études d'algorithmes d'openCV
- recherche sur l'état de l'art 
### 24 avril 2017
Reprise après une coupure pour finir le travail de semestre et la coupure de pâques. 

j'ai récupéré la caméra IP au labo aujourd'hui, il faut brancher la camera sur un routeur et exécuter une routine d'installation depuis un CD Compatible pour Windows ou mac OS 10 uniquement.  une fois l'installation faite il sera possible d’accéder aux images via internet depuis n'importe quel système.

- Ma machine au labo est sous Ubuntu. sois j'installe windows soit je fais la configuration sur un pc windows du même réseau. soit je fais la configuration sur mon mac OSX.

- sur quel routeur je pourrais brancher la caméra ?

- l'accès à distance à la caméra, se fait via un portail web www.mydlink.com , qu'on ne va pas utiliser.

- la platforme web propose entre autre une application de détection de mouvement 

- le software contient du code sous licence GNU dont la source peut se trouver sous 
http://tsd.dlink.com.tw/GPL.asp

### 27 avril 2017
Je suis passé sur windows 7 pour configurer la caméra ip.

Coincé depuis hier j'arrive toujours pas à installer une version de open cv qui va avec visual studio community 2017

j'ai regardé sur internet , rien de récent , le dernier tuto d'installation pour window opencv.org est pour VS 2012

soit la dernière version  d'openCV pour windows est prévue pour VS 2015, VS 2017 étant très récent et donc j'essaie d'installer VS 2015

soit c'est peut être VS 2017 qui n'est pas prévu pour une cible windows 7 .

Je vais graver VS 2015 puis l'installer et si ça va toujours pas, je retourne à ubuntu pour ne pas perdre plus de temps.

### 2 Mai 2017

Je suis retourné à ubuntu mais le script que j'avais utilisé y a 1 mois pour installer openCV ne fonctionnais plus après avoir passé plusieurs heures à débugger, j'ai finalement trouvé un autre script qui à l'air de tout installer comme il faut, mais en faisant un test en C++ que j'avais déjà effectuer la dernière fois, j'ai eu un message d'erreur provenant d'une fonction de la librairie openCV et non de mon code "modules/highgui/src/window.cpp" ligne 312.
le même test fait en python fonctionne. je pourrais éventuellement continuer en python.

### 3 mai 2017

étude de l'état de la techniques avec openCV et les caractéristiques des différents modules qui peuvent nous servir pour le projet. 
j'ai essayer de capter le flux vidéo via un petit programme en python mais j'ai de nouveau eu le même message d'erreur provenant de la ligne 312 méthode imshow dans le module highgui de la bibliothèque opencv.

### 5 mai 2017

le bug est réglé, ce message survient lorsque le fichier à lire est introuvable.
Je peux à présent afficher le flux de la caméra ip dans une fenêtre crée avec openCV

### 13 mai 2017

réfléxion sur la proposition d'un système adapté au cas d'études et présentation d'un schéma. la caméra donne sur une route Où passent beaucoup de voitures, quelques vélos et quelques passants sur les trottoirs. il s'agirait de concevoir un système capable de détecter au moins un des trois.

### 15 mai 2017

j'ai réussi à appliquer la méthode de soustraction de fond par mixture de gaussienne sur le flux de la caméra IP et on voit les objets en mouvement (piétons, voitures, 2 roues) qui se distinguent du fond noir. Il y a toutefois pas mal de bruits dans le masque ainsi crée et les objets sont un peu trop loin pour en tirer quelque chose. 

### 18 mai 2017

j'ai exploré l'état de l'art et de la technique pour la détection d'objet et je me rend compte qu'il y a énormément de boulot et de concept à connaître. l'intelligence artificielle , le machine learning c'est très complexe et ça prend apparemment beaucoup beaucoup  de temps pour entraîner un  système à la reconnaissance d'un model. faudra revoir les ambitions à la baisse je pense. je ne sais pas si je vais arriver au bout de ce projet. Le temps passe vite et les jours n'ont que 24 heures.
le premier exemple de structure que j'avais fait était finalement meilleur que celui que j'ai modifier hier mais il doit être  mieux expliqué au niveau de l'extraction des caractéristiques et de la classification.

### 23 mai 2017

j'ai pu commencer à utiliser l'algorithme ORB du module feature 2d d'opencv 3.2.0  pour l'extraction des caractéristiques d'une image avec python .
Pour tester la reconnaissance d'objet,j'aimerais pouvoir emprunter une web cam pour essayer de faire le matching entre une image template et un flux vidéo.

### 26 mai 2017

j'ai fait le matching entre une image enregistré et le flux vidéo provenant d'une webcam. la reconnaissance d'objet demande de faire des réglages pour pas avoir trop de faux positif mais fonctionne. l'algorithme SIFT (scale-invariant feature transform ) pour identifier les éléments similaires entre différentes images numériques dont s'inspire ORB est réputé plus performant , mais il est devenu payant donc plus disponible dans la dernière version stable d' opencv.   

### 30 mai 2017

Ecriture du rapport 

### 1 juin 2017

Discussion avec les professeurs , la solution envisagé est d'entraîner soit même un classifieur et de déterminer par statistique le seuil de reconnaissance -> Règle de décision de Bayes  
### 14 juin 2017

je lis et fais des recherches sur comment fonctionnent et sont créer les classifieurs. il y a beaucoup d'informations sur la théorie et sur les algorithmes de machine learning d'entrainement mais pas grand chose sur la pratique. je dois faire le tri . je pense revenir à la première idée et faire un haar classifieur ensuite si le temps le permet essayer la méthode HOG , sinon je vais me dissiper à vouloir faire plusieurs choses à la fois.  
### 19 juin 2017

J'ai préparé en extrayant manuellement la zone d'intérêt , une collection d'une vingtaine d'images de cycliste que j'ai pris ce week end en photo
et j'ai autour de 150 images de background que j'ai pris de la caméra . je vais surement en ajouter d'autres par la suite 
