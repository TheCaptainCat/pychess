# Bienvenue dans PyChess, l'IA de Qchess. #

Dépôt : https://github.com/TheCaptainCat/pychess

Il existe une version console et une version graphique.

Afin de lancer la simulation, exécutez le fichier main.py avec un interpréteur Python 3.X.

La console vous demande quelle version lancer, il est donc important de lancer le programme
depuis une console. Sur Windows, il est conseillé d'utiliser le Powershell.

## VERSION CONSOLE ##
Suivez ensuite les instructions sur la console.

## VERSION GRAPHIQUE ##
L'interface s'appuie sur la bibliothèque tkinter.
Afin de profiter de l'interface, il faut installer les packages Image et ImageTk.

### Sur Debian ###
* sudo pip3 install PIL
* sudo apt-get install python3-pil.imagetk

### Sur Windows ###
* Source de PIL : http://www.pythonware.com/products/pil/
* Vous pouvez aussi utiliser un interpréteur Python 3.6 que nous avons
        nous même installé (recommendé)
        https://framadrop.org/r/RGJcdeWHYQ#PgFe25oZkWASJuCr0HpN9eXxFORfn3BSGpICkphwZFo=

## Algorithme ##
L’algorithme implémenté est minimax, il permet de construire un arbre d’une certaine profondeur et évaluer les chances de gagner. La profondeur choisie ici est 3, elle donne de bonnes performances en termes de temps et d’intelligence. Afin d’accélérer considérablement le temps de calcul, nous utilisons l’élagage Alpha Beta.

La logique de l’algorithme se trouve dans le fichier chess.ai.probability. Cette classe représente une probabilité de mouvement d’une seule pièce.

Lorsque la probabilité est un nœud de l’arbre, elle lance récursivement l’algorithme pour chaque mouvement de chaque pièce possible de la couleur active. Une probabilité est créée pour chaque, en changeant de couleur active afin de faire jouer l’adversaire.

Afin d’éviter de copier toute la structure à chaque possibilité, seules les pièces en mouvement sont sauvegardées et remises en place au retour de la récursion.

Lorsque la probabilité est une feuille, la profondeur maximale est atteinte, on calcule le score de cette branche. Chaque pièce se voit attribuer un score, le roi ayant un score très grand devant les autres. Le score total de l’IA est calculé et on y soustrait le score total de l’adversaire. Ainsi, le but sera de maximiser l’écart entre les deux scores.

Si l’IA doit jouer, elle choisit son enfant avec le score maximal. Sinon, elle choisit son enfant avec le score minimal, supposant que l’ennemi jouera celui-là. Ainsi, l’IA maximise les minimums, en somme elle va là où elle perd le moins.
