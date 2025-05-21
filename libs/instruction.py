from loguru import logger
from numbers import Number

### Definition des variables
# Espace memoire
variable = {}
chainec = {}
sous_partie_memory = {}

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
        logger.critical(f"Erreur: La variable {var} n'est pas defini")
        exit()

def get_chainec(chaine: str):
    if is_chainec:
        if chaine.startswith(".") and chaine.endswith("."):
            if chaine in chainec:
                return chainec[chaine]
                
            logger.critical("La variable n'a pas le bon format")
    else:
        logger.critical(f"La variable {chaine} n'est pas charger")
        exit() 

#### Instruction

def definir(instruc: list): # instruc[destination, valeur]
    #print(instruc)
    destination: str = instruc[0]
    valeur: str = instruc[1]
    
    if destination.isdigit():
        logger.critical("Un nom de variable ne peut pas etre une nombre")
        exit()
    
    if destination in mots_cle:
        logger.critical("Un nom de variable ne peut pas etre un mot clé")
        exit()
    
    if is_nombre(valeur) == False and valeur.isdigit() == False: 
        logger.critical("Vous ne pouvez definir que un nombre")
        exit()
    else:
        try:
            valeur = int(valeur)
        except (ValueError, TypeError):
            valeur = float(valeur)
            
    variable[destination] = valeur

def ecrire(instruc: list): # instruc[variable]
    #print(instruc)

    if len(instruc) < 1: 
        logger.critical("Vous ne pouvez ecrire que le contenue d'une variable ou un label d'une chainec")
        exit()

    final = ""
    for i in range(len(instruc)):
        
        if is_variable(instruc[i]): 
            final += f"{get_var(instruc[i])}"
        elif is_chainec(instruc[i]):
            final += get_chainec(instruc[i])
        else:
            logger.critical("Cette variable n'existe pas")
        
        final += " "

    print(final)
        

def somme(instruc: list):
    # Que une variable a la fois
    if len(instruc) != 3:
        logger.critical("Syntaxe erreur: somme a b destination")
        exit()
    
    arg_a = instruc[0]
    arg_b = instruc[1]
    destination = instruc[2]

    if is_variable(arg_a) and is_variable(arg_b):
        a = get_var(arg_a)
        b = get_var(arg_b)
        total = a + b

        definir([destination, total])
             
    else:
        logger.critical("Syntaxe erreur: les 2 variables doivent etre des Nombres")

def soustraire(instruc: list):
    # Que une variable a la fois
    if len(instruc) != 3:
        logger.critical("Syntaxe erreur: somme a b destination")
        exit()
    
    arg_a = instruc[0]
    arg_b = instruc[1]
    destination = instruc[2]

    if is_variable(arg_a) and is_variable(arg_b):
        a = get_var(arg_a)
        b = get_var(arg_b)
        total = a - b

        definir([destination, total])
             
    else:
        logger.critical("Syntaxe erreur: les 2 variables doivent etre des Nombres")

def charger(instruc: list):
    #print(instruc)
    if len(instruc) <= 1:
        logger.critical("Syntaxe erreur: charger .dest. chaine de charactere")
        exit()
    
    destination: str = instruc[0]
    valeur: str = ' '.join(instruc[1:])

    if destination.startswith(".") and destination.endswith("."):
        chainec[destination] = valeur
    else:
        logger.critical("Le nom n'a pas le bon format")
        exit()

