# Documentation France Assembleur
**FRASM** (abréviation de FRAASM : "France Assembleur") est un langage de programmation type assembleur minimaliste entièrement en français, conçu pour être simple, lisible, et exécuté à l'aide d'une machine virtuelle en Python.

## Syntaxe du langague

### Généralité

Un programme est composé de différente sections. Seule la section `Principale` est obligatoire.
Chaqu'une de ce section sont composé d'instruction. Il y a une instruction par ligne (cf instruction).

### Section du programme

Le language est composé de plusieur section permettant une meilleur organisation. Chaque section peut etre comparé à des fonctions.

La section `Initialisation:` permet de charger et definir des variables et chainec avant le début de la section `Principale`.

#### Tableau des sections

| Section          | Usage                                            | exigence |
|------------------|--------------------------------------------------|----------|
| `Principale:`    | Section principale du programme                  | oui      |
| `Initialisation:` | Section d'initialisation (`revenir` obligatoire) | non      |
| `Sous_partie:`   | Section secondaire du programme                  | non      |
| `revenir`        | Permet de revenir à la fonction d'origine        | non      | 

#### Regle des sections

Les sections doivent commencer par une lettre majuscule et finir par `:`.  
Tout comme les noms de variable, elles ne comportent pas d'espace.
Pour sortir d'une sous_partie, il faut utiliser `revenir`.  
La section `initialisation` ne peut contenir que des chargements ou definition et doit finir par un `revenir`.    
Chaque nom de section doit etre unique.  

### Instruction

Les instruction permettent d'effectuer diverse actions (cf tableau des instructions)  
Chaque instruction est sur une ligne.  

#### Tableau des instructions

| Mot-clé                                        | Description                                                    |
|------------------------------------------------|----------------------------------------------------------------|
| `definir a 10`                                 | affecter un nombre à une variable                              |
| `charger .nom_de_chaine. chaine de charactere` | permet de definir une chainec                                  | 
| `somme a b total`                              | addition de deux variables                                     |
| `soustraire a b total`                         | soustraction de deux variables                                 |
| `ecrire a`                                     | afficher la valeur d’une variable ou d'une chaine de caractere |
| `si a == 10 (instruction)`                     | condition                                                      |
| `sinon (instruction)`                          | ne peut être utilisé qu'immédiatement après un "si"            |
| `aller label`                                  | saut inconditionnel                                            |
| `fin`                                          | arret du programme                                             |

##### Information complémentaire

Chaque nom de variable ou chainec est unique et ne comporte pas d'espace.  
Les commentaires s'ecrivent avec `#`.
On peut definir seulement des nombres (entier ou décimaux) dans les variables (instruction: `definir`)    
On ne peut `ecrire` que des `variables` ou `chainec`.
On peut mettre plusieur argument à ecrire ce qui permettra d'afficher chaque valeur l'une après l'autre    
Les chaines de characteres sont chargés dans les chainec (`load` .nom.) 
Les `chainec` sont des chaines de characteres réferencé grâce à un label commencant par un `.` et finissant par un `.`  (Exemple .nom.)
Les binaires sont disponibles via `Vrai` et `Faux`. 

#### Regle des instrutions
Chaque instruction est sur une ligne.  
Elles commencent par le mot clé en minuscule.  

### Mots Clés

Les mots clés disponiblent sont : 
- definir
- somme
- soustraire
- ecrire
- si
- aller
- fin
- charger
- revenir

Les mots-clé sont sensibles à la casse, ils doivent être ecrits en minuscule.  

#### Opérateur de Condition

Les seuls operateurs (op) disponibles sont : 
- `==`
- `!=`
- `>`
- `<`
- .chaine. (op) .dif_chaine.  

--- 

## Programme d'exemple

Exemple de programme en FRASM :
```

Principal: # Section Principal obligatoire
definir a 10 # a = 10
definir b 5 # b = 5
somme a b total # total = a + b
ecrire total # affiche total (15)
si total > 10 aller plus_10 
sinon aller Moins_10

Plus_10:
charger .afficher. 10 + 5 = 
ecrire .afficher. total
aller afficher_fin

Moins_10:
charger .afficher. 10 - 5 = 
ecrire .afficher. total
aller afficher_fin

afficher_fin:
charger .fin_. Fin du programme
ecrire .fin_.
fin
```

--- 
## Memoire
Le programme gere sa memoire grace à différent dictionnaire python.  