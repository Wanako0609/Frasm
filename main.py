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
                error_and_exit("create_sous_partie", f"Il y a 2 sections {contenue[i]}")

    #if "Initialisation:" in sous_partie_memory:
    #    return get_sous_partie("Initialisation:")
    #print(sous_partie_memory)
    return get_sous_partie("Principale")


def get_sous_partie(partie):
    #print(partie)
    if partie in sous_partie_memory:
        #print("Pointeur = ", sous_partie_memory[partie])
        #print(partie, sous_partie_memory[partie])
        return sous_partie_memory[partie]
    error_and_exit("get_sous_partie", f"Erreur : Partie {partie} pas trouvé")
    return None

def aller(dest, pointeur_value):
    if len(dest) != 1:
        error_and_exit("aller","Syntaxe error: l'instruction aller [destination]")

    destination = dest[0]

    pile_sous_partie.append(pointeur_value)
    #print("log sous partie",pile_sous_partie)
    return get_sous_partie(destination)


def revenir():
    if len(pile_sous_partie) == 0:
        error_and_exit("revenir","Vous n'etes pas rentrer dans une sous partie")

    return pile_sous_partie.pop()

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
pointeur = create_sous_partie(contenue_lecture)
running = True

while running:
    pointeur += 1
    #print(pointeur)
    if pointeur == len(contenue_lecture):
        running = False

    ligne = contenue_lecture[pointeur]
    instruc = ligne.strip().split(' ')
    # print(instruc)

    # Ligne commentaire
    if ligne.startswith('#'):
        continue
    # Execution erreur
    # Cas ou on trouve un format de sous partie
    if len(instruc) == 1 and instruc[0].endswith(":") and instruc[0][0].isupper():
        error_and_exit("Main", "Execution erreur, avez vous bien utiliser revenir ?")

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
            #print("chargement")
        case "aller":
            pointeur = aller(instruc[1:], pointeur)
        case "revenir":
            pointeur = revenir()
            #print("Revenir a ", pointeur)
            #print("Prochaine instruction :", contenue_lecture[pointeur].strip().split(' '))
        case "fin":
            running = False
            #print("fin appeler")
        case "":
            pass
        case _:
            error_and_exit("Main", f"Instruction {instruc[0]} inconnu")

logger.success("Fin du programme")
