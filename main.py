"""
main.py
Programme principal permettant d'interpréter du Frasm (.frasm)
Utilisation : python3 main.py fichier
"""
from pathlib import Path
import sys
from libs.parser import *
from libs.logger import FrasmExecutionError

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

try:
    while running:
        pointeur += 1
        if pointeur == len(contenue_lecture):
            running = False

        try:
            ligne = contenue_lecture[pointeur]
        except IndexError:
            logger.critical("Execution : dépassement de la mémoire du programme → fin du fichier atteinte sans 'fin'")
            exit(1)

        # Ligne commentaire
        if ligne.startswith('#') or ligne.strip() == "":
            continue

        instruc = ligne.strip().split(' ')
        #print(instruc)

        # Execution erreur
        # Cas ou on trouve un format de sous partie
        if len(instruc) == 1 and instruc[0].endswith(":") and instruc[0][0].isupper():
            error_and_exit("Execution",f"Transition non terminée avant la section '{instruc[0]}' → 'revenir' ou 'fin' attendu.")

        #print(memoire.est_initialisation)
        if memoire.est_initialisation:
            pointeur, running = executer_initialisation(instruc, pointeur, contenue_lecture)
        else:
            pointeur, running = executer_instruction(instruc, pointeur, contenue_lecture)

except FrasmExecutionError as e:
    logger.critical(str(e))
    raise  # pour afficher aussi la ligne exacte
except Exception as e:
    logger.exception("Erreur inattendue")
    raise

logger.success("Fin du programme")
