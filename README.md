# LineaLang

**LineaLang** est un langage de programmation type assembleur minimaliste entièrement en français, conçu pour être simple, lisible, et exécuté à l'aide d'une machine virtuelle en Python.

---

## Objectif

Créer un langage éducatif pour comprendre :
- la création d'un langage interprété
- la logique d'exécution ligne par ligne
- la gestion des variables, instructions, sauts, et conditions

---

## Syntaxe de base
Le programme est structurer en différente section
Chaque instruction doit être sur une ligne.  
Les mots-clé sont sensibles à la casse, ils doivent être ecrits en minuscule.  
Les labels ne peuvent pas avoir d'espace et doivent finir par `:`  

### Section du programme

| Section         | Usage                     |   exigence    |
|----------------|----------------------------------| ------- |
| `Principal:`        | Section principal du programme | oui |
| `Sous-partie:`  | permet de definir une chainec | non |

### Instructions disponibles

| Mot-clé         | Description                     |
|----------------|----------------------------------|
| `definir a 10`        | affecter un nombre à une variable |
| `charger nom_de_chaine chaine de charactere`  | permet de definir une chainec | 
| `somme a b total`  | addition de deux variables        |
| `soustraire a b total`  | soustraire de deux variables       |
| `ecrire a`     | afficher la valeur d’une variable ou directement un chaine de charactere |
| `si a == 10 (instruction)` | condition et saut                |
| `sinon (instruction)`        | ne peut être utilisé qu'immédiatement après un "si"         |
| `aller label`        | saut inconditionnel              |
| `fin`        | arret du programme              |

### Instrution detaillé

Chaque instruction est relative à une ligne.  



### Variable
On peut definir seulement des nombres (entier ou décimaux) dans les variables (instruction: definir)  
Les chaines de characteres sont chargés dans les chainec (load .nom.)  
Les binaires sont disponible via `.Vrai.` et `.Faux.`.  
Chaque nom de variable ou chainec est unique.  
Les commentaires s'ecrivent avec `#`.  
On ne peut `ecrire` que des `variables` ou `chainec`.  
Les `chainec` sont des chaines de characteres réferencé grâce à un label commencant par un `.` et finissant par un `.`  
Les labels ne comportent pas d'espace.  

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

### Condition
Les seuls conditions actuelles sont `==` et `!=`.

### Exemple
Exemple de programme LineaLang :
```
definir a 10
definir b 5
somme a b total
si total == 10 aller afficher_total
sinon aller afficher_fin

afficher_total:
charger .afficher. 10 + 5 = 
ecrire .afficher. total
aller afficher_fin

afficher_fin:
charger .fin_.
ecrire .fin_.
fin
```

---
## Memoire
Le programme gere sa memoire grace à un tableau python.  
Il y a une partie pour la gestion des variables et une autre pour la gestion des chainec.  

---

## Installation
Ce projet ne nécessite aucune dépendance. Utilisez Python 3.12 ou supérieur.

## Exécution

```bash
python3 main.py mon_programme.lina
```

## Dossiers

- `programmes/` : Contient des exemples de programmes en LineaLang (.lina)
- `docs/` : Contient la documentation et les spécifications du langage
- `libs/` : Contient les spécifications du langage


## À venir

- avoir un espace avec les chaines de caracteres et utiliser leur label -> chainec
- avoir des parties dans le programmes [code, chainec, const]
- Gestion des chaînes de caractères
- Création de PyLang, fin de phrase via un `.`
- Création du compilateur PyLang -> LineaLang

## Auteur
Projet personnel développé par Wanako, dans le but d’apprendre à concevoir un langage.