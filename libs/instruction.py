from loguru import logger
from numbers import Number

from libs.logger import error_and_exit

### Definition des variables
# Espace memoire
variable = {}
chainec = {}
sous_partie_memory = {}
pile_sous_partie = []

# Mot clé
mots_cle = ["Vrai", "Faux", "definir", "ecrire", "somme", "soustraire", "fin"]

### Définition des fonctions

def is_nombre(x):
    if isinstance(x, Number):
        return True
    else:
        return False

def is_variable(var: str): 
    if var in variable:
        return True
    return False

def is_chainec(chaine: str): 
    """
    Permet de verifier si la chaine fait partie des chaine charger
    """
    #print("test si ", chaine, " in chainec :", chainec)
    if chaine in chainec:
        return True
    return False

def get_var(var):
    """
    Il recupere un nom de variable et renvoie le nombre correspondant 
    soit int ou float
    """
    if is_variable(var):
        try:
            return int(variable[var])
        except (ValueError, TypeError):
            try:
                return float(variable[var])
            except (ValueError, TypeError):
                raise ValueError(f"{variable[var]!r} n'est pas un nombre")
    else:
        error_and_exit("get_var", f"La variable {var} n'est pas defini")
        return None

def get_chainec(chaine: str):
    if is_chainec:
        if chaine.startswith(".") and chaine.endswith("."):
            if chaine in chainec:
                return chainec[chaine]

            error_and_exit("get_chainec", f"La variable {chaine} n'a pas le bon format")
            return None
        return None
    else:
        error_and_exit("get_var", f"La chainec {chaine} n'est pas defini")
        return None

#### Instruction

def definir(instruc: list):
    if len(instruc) != 2:
        logger.critical("definir : syntaxe invalide → attendu 'definir variable valeur'")
        exit(1)

    destination = instruc[0]
    valeur = instruc[1]

    if destination.isdigit():
        logger.critical(f"definir : nom de variable invalide → '{destination}' est un nombre.")
        exit(1)

    if destination in mots_cle:
        logger.critical(f"definir : nom de variable interdit → '{destination}' est un mot-clé réservé.")
        exit(1)

    if not valeur.replace('.', '', 1).isdigit():
        logger.critical(f"definir : valeur invalide → '{valeur}' n’est pas un nombre.")
        exit(1)

    try:
        valeur = int(valeur)
    except ValueError:
        valeur = float(valeur)

    variable[destination] = valeur
    logger.info(f"definir : variable définie → {destination} = {valeur}")


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

def charger(instruc: list):
    #print(instruc)
    if len(instruc) <= 1:
        error_and_exit("charger", f"Syntaxe erreur: charger .dest. chaine de charactere")
    
    destination: str = instruc[0]
    valeur: str = ' '.join(instruc[1:])

    if destination.startswith(".") and destination.endswith("."):
        chainec[destination] = valeur
    else:
        error_and_exit("charger", f"Syntaxe erreur: charger .dest.")

