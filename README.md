# FRASM

**FRASM** (abréviation de FRAASM : "France Assembleur") est un langage de programmation type assembleur minimaliste entièrement en français, conçu pour être simple, lisible, et exécuté à l'aide d'une machine virtuelle en Python.

---

## Objectif

### Personnel
Créer un langage simple pour comprendre :
- la création d'un langage interprété
- la gestion des variables, instructions, sauts, et conditions

### Language
Créer un langage éducatif accessible à un large public en brisant la barierre de la langue.
Implémentation simple et logique d'opération.  
Mise en oeuvre de pseudo code

---

## Syntaxe de base
Le programme est structuré en différente section, dont la section `Principal:`, dans le quel se trouve la partie principal du programme.  
Chaque instruction est sur une ligne.  
Les mots-clé sont sensibles à la casse, ils doivent être ecrits en minuscule.  
Les labels ne peuvent pas avoir d'espace et doivent finir par `:`  

### Section du programme

| Section          | Usage                                            | exigence |
|------------------|--------------------------------------------------|----------|
| `Principale:`    | Section principale du programme                  | oui      |
| `Initialisation:` | Section d'initialisation (`revenir` obligatoire) | non      |
| `Sous_partie:`   | Section secondaire du programme                  | non      |
| `revenir`        | Permet de revenir à la fonction d'origine        | non      | 

#### Regle des sections
Les sections doivent commencer par une lettre majuscule et finir par `:`.  
Tout comme les noms de variable, elles ne comportent pas d'espace.
Pour sortir d'une sous_partie, il faut utiliser `revenir`  
La section `initialisation` ne peut contenir que des chargements ou definition  
Chaque nom de section doit etre unique

### Instructions disponibles

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

#### Regle des instrutions
Chaque instruction est sur une ligne.  
Elles commencent par le mot clé en minuscule.  



#### Regle des variables
On peut definir seulement des nombres (entier ou décimaux) dans les variables (instruction: definir)    
Chaque nom de variable ou chainec est unique et ne comporte pas d'espace.  
Les commentaires s'ecrivent avec `#`.  
On ne peut `ecrire` que des `variables` ou `chainec`.  
Les chaines de characteres sont chargés dans les chainec (load .nom.) 
Les `chainec` sont des chaines de characteres réferencé grâce à un label commencant par un `.` et finissant par un `.`  
Les binaires sont disponibles via `Vrai` et `Faux`. 


#### Mots Clés
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

#### Condition
Les seuls operateurs (op) disponibles sont : 
- `==`
- `!=`
- `>`
- `<`
- .chaine. op .dif_chaine.

#### Exemple
Exemple de programme FRASM :
```
Principal:
definir a 10
definir b 5
somme a b total
ecrire total
si total > 10 aller plus_10
sinon aller moins_10

Plus_10:
charger .afficher. 10 + 5 = 
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

---
## Installation
Ce projet ne nécessite aucune dépendance. Utilisez Python 3.12 ou supérieur.

## Exécution

```bash
python3 main.py mon_programme.frasm
```

## Dossiers

- `programmes/` : Contient des exemples de programmes en FRASM (.frasm)
- `docs/` : Contient la documentation et les spécifications du langage
- `libs/` : Contient les spécifications du langage

## À venir
- avoir des parties dans le programmes [code, chainec, const]
- Gestion des chaînes de caractères
- Création de PyLang, fin de phrase via un `.`
- Création du compilateur PyLang -> FRASM

## Auteur
Projet personnel développé par Wanako, dans le but d’apprendre à concevoir un langage.