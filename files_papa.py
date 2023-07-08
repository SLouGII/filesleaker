# Je préfère la librairie pathlib pour manipuler les fichiers. Mais c'est personnel.
from pathlib import Path

# argv fait partie du module sys, il permet de récupérer la ligne de commande
# on peut importer tout le module (import sys) ou juste ce qu'on veut comme ça
# argv c'est une variable de type liste qui contient tout ce que tu as mis en ligne de commande
# donc si je dis # python files_papa.py argument1 argument2, argv contient :
# ['files_papa.py', 'argument1', 'argument2']
from sys import argv

# Récupération du nom de dossier passé en paramètre
# En python, dans les listes, on commence a compter a partir de 0, donc le premier élément est argv[0], 
# Dans ce cas ci, le premier element est le nom du programme (voir ligne 8)
parameter_directory = argv[1]

# Le second parametre permet de dire a ton programme si il doit donner juste les noms des fichiers ou donner plus de détails.
# Ce parametre prends la valeur Y ou N
parameter_details = argv[2]

# Ici, je déclare l'objet directory path en utilisant Path du module pathlib (voir ligne 2), 
# L'objet de type path conteint plein de fonctions utiles
directory = Path(parameter_directory)

# Je vérifie si le folder existe ET est un dossier
# si je déclare un fichier et que je veux tester si c'est un fichier, alors c'est variable.is_file()
if ( not directory.is_dir() ) :
    # Si il n'existe pas, je lance une erreur de type FileNotFound
    # Remarques que ici, je compose une chaine de caractère en utilisant le f"".  En mettant f devant les quotes, on peut mettre des variables
    # ou n'importe quoi entre {} donc tu as des chaines de caractère dynamiques. pour quoi str() ? parce que directory est un objet de type Path, 
    # on ne peut pas l'afficher comme ça, donc je spécifie bien qu'il doit être converti en str (string)
    raise FileNotFoundError (f"Erreur : Le dossier {directory} n'existe pas.")


# Petit tour de passe passe pour afficher les tailles de manière plus lisibles.
# je t'expliquerais comment ça marche. J'appelle cette fonction dans la boucle a la ligne 75 pour affichier la taille du fichier
def bytes_to_readable ( bytes:int )-> str :
    for unit in ['b', 'kb', 'mb', 'gb', 'tb']:
        if bytes < 1024.0:
            return "%3.1f %s" % (bytes, unit)
        bytes /= 1024.0

# Afficher le message customisé
print(f"Contenu du dossier {directory}.")

# Ici, une boucle for, mais avant, tu remarques qu'il y a un appel a la fonction iterdir() de l'objet directory (Objet de type Path)
# La fonction iterdir est ce qu'on appelle un itérateur, il va renvoyer le nom de tous les fichiers dans le directory
# Donc la boucle fonctionne comme ça, on attribue a file la valeur de tout ce qui est dans directory.  ça marche aussi avec les listes.

for file in directory.iterdir() :
    type = 'Dossier' if file.is_dir() else 'Fichier'
    print(f"{type}  - {bytes_to_readable(file.stat().st_size)}  - {file}")

