from numbers import Number

from libs.logger import error_and_exit
import libs.memoire as memoire
### Définition des fonctions transverses

def is_nombre(x):
    if isinstance(x, Number):
        return True
    else:
        return False

def is_variable(var: str):
    if var in memoire.variable:
        return True
    return False

def is_chainec(chaine: str):
    """
    Permet de verifier si la chaine fait partie des chaine charger
    """
    #print("test si ", chaine, " in chainec :", chainec)
    if chaine in memoire.chainec:
        return True
    return False

def get_var(var):
    """
    Il recupere un nom de variable et renvoie le nombre correspondant
    soit int ou float
    """
    if is_variable(var):
        try:
            return int(memoire.variable[var])
        except (ValueError, TypeError):
            try:
                return float(memoire.variable[var])
            except (ValueError, TypeError):
                raise ValueError(f"{memoire.variable[var]!r} n'est pas un nombre")
    else:
        error_and_exit("get_var", f"La variable {var} n'est pas defini")
        return None

def get_chainec(chaine: str):
    if is_chainec:
        if chaine.startswith(".") and chaine.endswith("."):
            if chaine in memoire.chainec:
                return memoire.chainec[chaine]

            error_and_exit("get_chainec", f"La variable {chaine} n'a pas le bon format")
            return None
        return None
    else:
        error_and_exit("get_var", f"La chainec {chaine} n'est pas defini")
        return None

def create_sous_partie(contenue):
    for i in range(len(contenue)):
        if contenue[i].endswith(":") and contenue[i][0].isupper():
            if not contenue[i] in memoire.sous_partie_memory:
                #print(contenue[i][:-1], " pointeur : ", i)
                memoire.sous_partie_memory[contenue[i][:-1]] = i
            else:
                error_and_exit("create_sous_partie", f"Il y a 2 sections {contenue[i]}")


    if "Initialisation" in memoire.sous_partie_memory:

        memoire.est_initialisation = True
        memoire.pile_sous_partie.append(get_sous_partie("Principale"))
        return get_sous_partie("Initialisation")
    #print(sous_partie_memory)
    return get_sous_partie("Principale")


def get_sous_partie(partie):
    #print(partie)
    if partie in memoire.sous_partie_memory:
        #print("Pointeur = ", sous_partie_memory[partie])
        #print(partie, sous_partie_memory[partie])
        return memoire.sous_partie_memory[partie]
    error_and_exit("get_sous_partie", f"Erreur : Partie {partie} pas trouvé")
    return None