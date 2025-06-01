# Documentation France Assembleur

**FRASM** (abréviation de FRAASM : "France Assembleur") est un langage de programmation de type assembleur, minimaliste et entièrement en français, conçu pour être simple, lisible, et exécuté à l'aide d'une machine virtuelle en Python.

---

## Syntaxe du langage

### Généralités

Un programme est composé de différentes sections. Seule la section `Principale:` est obligatoire.  
Chacune de ces sections est composée d'instructions, avec **une instruction par ligne** (voir tableau des instructions).

---

### Sections du programme

Le langage est composé de plusieurs sections permettant une meilleure organisation.  
Chaque section peut être comparée à une fonction.

La section `Initialisation:` permet de charger et de définir des variables ou des chaînes avant le début de la section `Principale:`.

#### Tableau des sections

| Section           | Usage                                            | Exigence |
|-------------------|--------------------------------------------------|----------|
| `Principale:`     | Section principale du programme                  | oui      |
| `Initialisation:` | Section d'initialisation (`revenir` obligatoire) | non      |
| `Sous_partie:`    | Section secondaire du programme                  | non      |
| `revenir`         | Permet de revenir à la fonction d'origine        | non      |

#### Règles des sections

- Les noms de section doivent **commencer par une majuscule** et finir par `:`
- Comme les noms de variables, ils **ne doivent pas contenir d'espaces**
- Pour sortir d’une `Sous_partie`, il faut utiliser l’instruction `revenir`
- La section `Initialisation` ne peut contenir que des instructions `definir` ou `charger`, et doit se terminer par `revenir`
- Chaque nom de section doit être **unique**

---

### Instructions

Les instructions permettent d’effectuer diverses actions (voir tableau ci-dessous).  
Chaque instruction est écrite **sur une seule ligne**.

#### Tableau des instructions

| Mot-clé                                        | Description                                                  |
|------------------------------------------------|--------------------------------------------------------------|
| `definir a 10`                                 | Affecte un nombre à une variable                             |
| `charger .nom_de_chaine. chaîne de caractères` | Définit une chaîne (`chainec`)                               |
| `caractere .nom_de_chaine. index caractere`   | Remplace un caractère à l'index donné dans une chaîne (`chainec`) |
| `somme a b total`                              | Additionne deux variables et stocke le résultat dans `total` |
| `soustraire a b total`                         | Soustrait `b` de `a` et stocke le résultat dans `total`      |
| `quotient a b total`                           | Divise `b` de `a` et stocke le résultat dans `total`         |
| `produit a b total`                            | Multiplie `b` et `a` et stocke le résultat dans `total`      |
| `ecrire a`                                     | Affiche une variable ou une chaîne (`chainec`)               |
| `si a == 10 aller ...`                         | Évalue une condition                                         |
| `sinon aller ...`                              | Instruction alternative si la condition est fausse           |
| `aller label`                                  | Saut inconditionnel                                          |
| `fin`                                          | Arrête le programme                                          |

---

##### Informations complémentaires

- Chaque nom de **variable** ou de **chainec** est **unique** et **sans espaces**
- Les commentaires commencent par `#`
- Seuls des **nombres** (entiers ou décimaux) peuvent être affectés via `definir`
- `ecrire` permet d'afficher **des variables** ou **des chaînes référencées**
- Il est possible d’afficher **plusieurs arguments** avec `ecrire` (affichage séquentiel)
- Les chaînes de caractères sont chargées avec l'instruction `charger` et référencées sous la forme `.nom.`
- Les **chainec** sont des chaînes référencées **commençant et finissant par un point** (ex : `.nom.`)
- Les valeurs booléennes sont disponibles via les mots-clés **`Vrai`** et **`Faux`**

---

#### Règles des instructions

- Une instruction = une ligne
- Chaque instruction commence par un **mot-clé en minuscule**
- La casse est **sensible** : `definir` ≠ `Definir`

---

### Mots-clés disponibles

- `definir`
- `somme`
- `soustraire`
- `ecrire`
- `si`
- `sinon`
- `aller`
- `fin`
- `charger`
- `revenir`
- `produit`
- `quotient`

---

### Opérateurs conditionnels disponibles

- `==` (égalité)
- `!=` (différent)
- `>` (supérieur)
- `<` (inférieur)
- `>=` (supérieur ou égalité)
- `<=` (inférieur ou égalité)
- `.chaine.` (égalité ou différence) `.autre_chaine.` (comparaison entre chaînes)

---

## Exemple de programme

```frasm
Principale:
definir a 10
definir b 5
soustraire a b total
si total > a aller Plus_10
sinon aller Moins_10

Plus_10:
charger .afficher. 10 + 5 =
ecrire .afficher. total
aller Afficher_fin

Moins_10:
charger .afficher. 10 - 5 =
ecrire .afficher. total
aller Afficher_fin

Afficher_fin:
charger .fin_. Fin du programme
ecrire .fin_.
fin
````

---

## Mémoire

Le programme gère sa mémoire à l’aide de différents dictionnaires Python, séparant :

* les **variables numériques**
* les **chaînes de caractères référencées** (`chainec`)
* les **booléens**

Chaque espace mémoire est indépendant afin de faciliter la gestion des types et des opérations.
