"""
main.py
Programme principal permettant d'interpréter du Linealang (.linea)
Utilisation : python3 main.py fichier.lina
"""

from pathlib import Path
import sys
from loguru import logger
from numbers import Number

# logger.add(sys.stderr, format="{level} | {message}")

### Définition des fonctions

def is_nombre(x):
    if isinstance(x, Number):
        print(f"{x} est un nombre")
    else:
        print(f"{x} n'est pas un nombre")

def is_variable(var: str): 
    if var in variable:
        return True
    return False

def is_chainec(chaine: str): 
    if chaine in chainec:
        return True
    return False

def get_var(var):
    if var in variable:
        return variable[var]
    logger.critical(f"La variable {var} n'est pas definir")
    exit()

def get_chainec(chaine: str):
    if chaine.startswith(".") and chaine.endswith("."):
        if chaine in chainec:
            return chainec[chaine]
        logger.critical(f"La variable {chaine} n'est pas charger")
        exit() 
    
def definir(instruc: list): # instruc[destination, valeur]
    #print(instruc)
    destination: str = instruc[0]
    valeur: str = instruc[1]
    
    if destination.isdigit():
        logger.critical("Un nom de variable ne peut pas etre une nombre")
        exit()
    
    if valeur.isdigit() == False: 
        logger.critical("Vous ne pouvez definir que un nombre")
        exit()
    else:
        valeu = valeur

    variable[destination] = valeur

def ecrire(instruc: list): # instruc[variable]
    #print(instruc)

    # Que une variable a la fois
    if len(instruc) != 1:
        logger.critical("Vous ne pouvez ecrire que le contenue d'une variable ou un label d'une chainec")
        exit()
    
    # Cas variable
    if is_variable(instruc[0]): 
        print(get_var(instruc[0]))
    else:
        logger.critical("Cette variable n'existe pas")
        exit()

def somme(instruc: list):
    # Que une variable a la fois
    if len(instruc) != 3:
        logger.critical("Syntaxe erreur: somme a b destination")
        exit()
    
    arg_a = instruc[0]
    arg_b = instruc[1]
    destination = instruc[2]

    if is_variable(arg_a) and is_variable(arg_b):
        a: Number = get_var(arg_a)
        b: Number = get_var(arg_b)
        total = a + b

        definir([destination, total])
             
    else:
        logger.critical("Syntaxe erreur: les 2 variables doivent etre des Nombres")


#### Definition des variables
# Espace memoire
variable = {}
chainec = {}

# Mot clé
mots_cle = ["Vrai", "Faux", "definir", "ecrire", "somme", "fin"]

#### Début du programme

# Gestion des arguments
if len(sys.argv) != 2:
    logger.error("Utilisation : python3 main.py fichier.linea")
    exit(1)

# Récupération du fichier
nom_fichier = sys.argv[1]
fichier = Path(nom_fichier)

# Vérification de l'extension
if fichier.suffix != ".linea":
    print("Ce n'est pas un fichier .linea")
    exit(1)

logger.info(f"Fichier interprété : {fichier.name}")

# Preparation fichier
contenu = fichier.read_text()
contenue_lecture = contenu.splitlines()

# Initialisation
pointeur = -1
running = True

while (running):
    pointeur += 1 # Increase pointeur
    if pointeur > len(contenue_lecture): # test fin du fichier
        running = False

    ligne = contenue_lecture[pointeur]

    # Ligne commentaire
    if ligne.startswith('#'):
        continue
        
    instruc = ligne.strip().split(' ')

    match instruc[0]:
        case "definir":
            definir(instruc[1:])
        case "somme":
            somme(instruc[1:])
        case "ecrire":
            ecrire(instruc[1:])
        case "fin":
            running = False
        case _:
            pass

logger.success("Fin du programme")
