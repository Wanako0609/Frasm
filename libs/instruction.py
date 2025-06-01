from loguru import logger
from libs.fonction_transverse import *
from libs.logger import error_and_exit
import libs.memoire as memoire

#### Instruction du programme ################################

def definir(instruc: list):
    if len(instruc) != 2:
        logger.critical("definir : syntaxe invalide → attendu 'definir variable valeur'")
        exit(1)

    destination = instruc[0]
    valeur = instruc[1]

    if destination.isdigit():
        logger.critical(f"definir : nom de variable invalide → '{destination}' est un nombre.")
        exit(1)

    if destination in memoire.mots_cle:
        logger.critical(f"definir : nom de variable interdit → '{destination}' est un mot-clé réservé.")
        exit(1)

    if not is_nombre(valeur) and not valeur.replace('.', '', 1).isdigit():
        logger.critical(f"definir : valeur invalide → '{valeur}' n’est pas un nombre.")
        exit(1)

    try:
        valeur = int(valeur)
    except ValueError:
        valeur = float(valeur)

    memoire.variable[destination] = valeur
    #logger.info(f"definir : variable définie → {destination} = {valeur}")


def ecrire(instruc: list): # instruc[variable]
    #print(instruc)

    if len(instruc) < 1:
        error_and_exit("ecrire", f"Syntaxe erreur, ecrire [var ou chainec]")

    final = ""
    for i in range(len(instruc)):
        
        if is_variable(instruc[i]): 
            final += f"{get_var(instruc[i])}"
        elif is_chainec(instruc[i]):
            final += get_chainec(instruc[i])
        else:
            error_and_exit("ecrire", f"Cette variable n'existe pas : {instruc[i]}")
        
        final += " "

    print(final)
        

def somme(instruc: list):
    # Que une variable a la fois
    if len(instruc) != 3:
        error_and_exit("somme", f"Syntaxe erreur: somme a b destination")
    
    arg_a = instruc[0]
    arg_b = instruc[1]
    destination = instruc[2]

    if is_variable(arg_a) and is_variable(arg_b):
        a = get_var(arg_a)
        b = get_var(arg_b)
        total = a + b

        definir([destination, total])
             
    else:
        error_and_exit("somme", f"Syntaxe erreur: les 2 variables doivent etre des Nombres")


def produit(instruc: list):
    if len(instruc) != 3:
        error_and_exit("produit", f"Syntaxe erreur: produit a b destination")

    arg_a = instruc[0]
    arg_b = instruc[1]
    destination = instruc[2]

    if is_variable(arg_a) and is_variable(arg_b):
        a = get_var(arg_a)
        b = get_var(arg_b)
        total = a * b

        definir([destination, total])

    else:
        error_and_exit("produit", f"Syntaxe erreur: les 2 variables doivent etre des Nombres")

def soustraire(instruc: list):
    # Que une variable a la fois
    if len(instruc) != 3:
        error_and_exit("soustraire", f"Syntaxe erreur: soustraire a b destination")

    arg_a = instruc[0]
    arg_b = instruc[1]
    destination = instruc[2]

    if is_variable(arg_a) and is_variable(arg_b):
        a = get_var(arg_a)
        b = get_var(arg_b)
        total = a - b

        definir([destination, total])
             
    else:
        error_and_exit("soustraire", f"Syntaxe erreur: les 2 variables doivent etre des Nombres")


def quotient(instruc: list):
    # Que une variable a la fois
    if len(instruc) != 3:
        error_and_exit("quotient", f"Syntaxe erreur: quotient a b destination")

    arg_a = instruc[0]
    arg_b = instruc[1]
    destination = instruc[2]

    if is_variable(arg_a) and is_variable(arg_b):
        a = get_var(arg_a)
        b = get_var(arg_b)
        total = a / b

        definir([destination, total])

    else:
        error_and_exit("quotient", f"Syntaxe erreur: les 2 variables doivent etre des Nombres")

def charger(instruc: list):
    #print(instruc)
    if len(instruc) <= 1:
        error_and_exit("charger", f"Syntaxe erreur: charger .dest. chaine de charactere")
    
    destination: str = instruc[0]
    valeur: str = ' '.join(instruc[1:])

    if destination.startswith(".") and destination.endswith("."):
        memoire.chainec[destination] = valeur
    else:
        error_and_exit("charger", f"Syntaxe erreur: charger .dest.")

def aller(dest, pointeur_value):
    if len(dest) != 1:
        error_and_exit("aller","Syntaxe error: l'instruction aller [destination]")

    destination = dest[0]

    memoire.pile_sous_partie.append(pointeur_value)
    #print("log sous partie",pile_sous_partie)
    return get_sous_partie(destination)


def revenir():
    if len(memoire.pile_sous_partie) == 0:
        error_and_exit("revenir","Vous n'etes pas rentrer dans une sous partie")
    if memoire.est_initialisation:
        memoire.est_initialisation = False
    return memoire.pile_sous_partie.pop()

def si(instruc):
    if len(instruc) <= 3:
        error_and_exit("si", "Syntaxe invalide → attendu : si a OP b (instruction)")

    arg_a = instruc[0]
    op = instruc[1]
    arg_b = instruc[2]

    # Cas : comparaison entre chaînes référencées (.a. != .b.)
    if arg_a.startswith(".") and arg_a.endswith(".") and arg_b.startswith(".") and arg_b.endswith("."):
        if op not in memoire.operateurs_chaines:
            error_and_exit("si", f"Opérateur '{op}' non valide pour une comparaison de chaînes.")
        if not is_chainec(arg_a) or not is_chainec(arg_b):
            error_and_exit("si", f"Une des chaînes n'est pas définie : {arg_a}, {arg_b}")

        chaine1 = get_chainec(arg_a)
        chaine2 = get_chainec(arg_b)

        resultat = memoire.operateurs_chaines[op](chaine1, chaine2)
        #logger.info(f"si : comparaison de chaînes → {chaine1} {op} {chaine2} = {resultat}")
        return resultat


    # Cas : comparaison entre variables numériques
    if not is_variable(arg_a) or not is_variable(arg_b):
        error_and_exit("si", f"Les arguments '{arg_a}' et/ou '{arg_b}' ne sont pas des variables.")

    if op not in memoire.operateurs_nombres:
        error_and_exit("si", f"Opérateur '{op}' non supporté.")

    a = get_var(arg_a)
    b = get_var(arg_b)

    resultat = memoire.operateurs_nombres[op](a, b)
    #logger.info(f"si : comparaison numérique → {a} {op} {b} = {resultat}")
    return resultat

def caractere(instruc: list):
    if len(instruc) != 3:
        error_and_exit("caractere", "Syntaxe : caractere .chaine. index nouveau_char")

    nom_chaine = instruc[0]
    index_str = instruc[1]
    nouveau_char = instruc[2]

    if not is_chainec(nom_chaine):
        error_and_exit("caractere", f"La chaine {nom_chaine} n'existe pas")

    if not index_str.isdigit():
        error_and_exit("caractere", "L'index doit être un entier positif")

    index = int(index_str)
    ancienne_valeur = chainec[nom_chaine]

    if index >= len(ancienne_valeur):
        error_and_exit("caractere", "Index hors limites")

    if len(nouveau_char) != 1:
        error_and_exit("caractere", "Le nouveau caractère doit être un seul caractère")

    # Remplacement caractère par caractère
    nouvelle_chaine = ancienne_valeur[:index] + nouveau_char + ancienne_valeur[index+1:]
    chainec[nom_chaine] = nouvelle_chaine

