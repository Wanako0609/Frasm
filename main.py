"""
main.py
Programme principal permettant d'interpréter du Linealang (.linea)
Utilisation : python3 main.py fichier.lina
"""
from pathlib import Path
import sys
from libs.instruction import *

def create_sous_partie(contenue):
    for i in range(len(contenue)):
        if contenue[i].endswith(":") and contenue[i][0].isupper():
            sous_partie_memory[contenue[i]] = i
    
    return get_sous_partie("Principal:")

def get_sous_partie(partie):
    if sous_partie_memory[partie] is set:
        return sous_partie_memory[partie]
    logger.critical(f"Erreur : Partie {partie} pas trouvé")
    exit()

# La fin de sous partie devrait etre des que il y aura une ligne vide, si c'est la partie main on fini le programme

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
pointeur = create_sous_partie(contenue_lecture) -1
running = True
is_fonction = False


while (running):
    pointeur += 1 # Increase pointeur
    if pointeur == len(contenue_lecture)-1: # test fin du fichier
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
        case "soustraire":
            soustraire(instruc[1:])
        case "ecrire":
            ecrire(instruc[1:])
        case "charger":
            charger(instruc[1:])
        case "fin":
            running = False
        case "":
            if len(instruc) == 0:
                if not is_fonction:
                    running = False
                else:
                    is_fonction = False
        case _:
            pass

logger.success("Fin du programme")
