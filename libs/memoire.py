import operator

### Definition des variables
# Espace memoire
variable = {}
chainec = {}
sous_partie_memory = {}
pile_sous_partie = []
est_initialisation = False

# Mot clé
mots_cle = ["Vrai", "Faux", "definir", "ecrire", "somme", "soustraire", "fin", "revenir", "si", "sinon", "produit", "quotient", "charactere"]

operateurs_nombres = {
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le
}

operateurs_chaines = {
    "==": operator.eq,
    "!=": operator.ne
}