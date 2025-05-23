"""
main.py
Programme principal permettant d'interpréter du Frasm (.frasm)
Utilisation : python3 main.py fichier
"""
from pathlib import Path
import sys
from libs.instruction import *


def create_sous_partie(contenue):
    for i in range(len(contenue)):
        if contenue[i].endswith(":") and contenue[i][0].isupper():
            if not contenue[i] in sous_partie_memory:
                #print(contenue[i][:-1], " pointeur : ", i)
                sous_partie_memory[contenue[i][:-1]] = i
            else:
                logger.critical(f"Il y a 2 sections {contenue[i]}")

    #if "Initialisation:" in sous_partie_memory:
    #    return get_sous_partie("Initialisation:")
    #print(sous_partie_memory)
    return get_sous_partie("Principale")


def get_sous_partie(partie):
    #print(partie)
    if partie in sous_partie_memory:
        #print("Pointeur = ", sous_partie_memory[partie])
        return sous_partie_memory[partie]
    logger.critical(f"Erreur : Partie {partie} pas trouvé")
    exit()

def aller(dest, pointeur_value):
    if len(dest) != 1:
        logger.error("Syntaxe error: l'instruction aller ne prend que un argument")

    destination = dest[0]

    pile_sous_partie.append(pointeur_value)
    #print(pile_sous_partie)
    return get_sous_partie(destination)


def revenir():
    if len(pile_sous_partie) != 0:
        logger.critical("Vous n'etes pas rentrer dans une sous partie")
        exit()


    return pile_sous_partie.pop()


# La fin de sous partie devrait etre des que il y aura une ligne vide, si c'est la partie main on fini le programme

#### Début du programme

# Gestion des arguments
if len(sys.argv) != 2:
    logger.error("Utilisation : python3 main.py fichier.frasm")
    exit(1)

# Récupération du fichier
nom_fichier = sys.argv[1]
fichier = Path(nom_fichier)

# Vérification de l'extension
if fichier.suffix != ".frasm":
    print("Ce n'est pas un fichier .frasm")
    exit(1)

logger.info(f"Fichier interprété : {fichier.name}")

# Preparation fichier
contenu = fichier.read_text()
contenue_lecture = contenu.splitlines()

# Initialisation
pointeur = create_sous_partie(contenue_lecture) - 1
running = True
pile_sous_partie = []

while running:
    pointeur += 1
    if pointeur == len(contenue_lecture) - 1:
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
        case "aller":
            pointeur = aller(instruc[1:], pointeur)
            #print(pile_sous_partie)
        case "revenir":
            pointeur = revenir()
            print(pointeur)
        case "fin":
            running = False
        case _:
            pass

logger.success("Fin du programme")
