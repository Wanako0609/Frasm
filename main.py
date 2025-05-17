"""
main.py
Programme principal permettant d'interpréter du Linealang (.linea)
Utilisation : python3 main.py fichier.lina
"""

from pathlib import Path
import sys
from loguru import logger

# logger.add(sys.stderr, format="{level} | {message}")

def parsing(ligne: str):
    pass

def fixer(instruc: list):
    print(instruc)
    nom_var: str = instruc[0]
    valeur: str = instruc[1]
    
    if nom_var.isdigit():
        logger.critical("Un nom de variable ne peut pas etre une nombre")
        exit()
    
    if valeur.isdigit() == False: # Ajouter le test sur les chainec
        logger.critical("Vous ne pouvez fixer que un nombre ou un label de chainec")
        exit()

    variable[nom_var] = valeur

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

# Espace memoire
variable = {}
chainec = {}

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
        
    instruc = ligne.split(' ')

    match instruc[0]:
        case "fixer":
            fixer(instruc[1:])
        case "somme":
            print("somme")
        case "ecrire":
            print("ecrire")
        case "fin":
            running = False
        case _:
            pass

logger.success("Fin du programme")
