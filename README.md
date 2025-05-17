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
Chaque instruction doit être sur une ligne.
Les mots-clé sont sensibles à la casse, ils doivent être ecrits en minuscule.
Les labels ne peuvent pas avoir d'espace et doivent finir par `:`
Chaque nom de variable est unique.
Les commentaires s'ecrivent avec `#`.
On ne peut `ecrire` que des `variables` ou `chainec`.
Les `chainec` sont des chaines de characteres réferencé grâce à un label commencant par un `.` et finissant par un `.`
Les labels ne comportent pas d'espace.

### Instructions disponibles

| Mot-clé         | Description                     |
|----------------|----------------------------------|
| `fixer a 10`        | affecter une valeur à une variable |
| `somme a b total`  | addition de deux variables        |
| `ecrire a`     | afficher la valeur d’une variable ou directement un chaine de charactere |
| `si a == 10 (instruction)` | condition et saut                |
| `sinon (instruction)`        | ne peut être utilisé qu'immédiatement après un "si"         |
| `aller label`        | saut inconditionnel              |
| `fin`        | arret du programme              |
| `load nom_de_chaine chaine de charactere`  | permet de definir une chainec | 

### Type de variable
- Integer

### Condition
Les seuls conditions actuelles sont `==` et `!=`.

### Exemple
Exemple de programme LineaLang :
```
fixer a 10
fixer b 5
somme a b total
si total == 10 aller afficher_total
sinon aller afficher_fin

afficher_total:
ecrire total
aller afficher_fin

afficher_fin:
ecrire "fin"
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


## À venir

- avoir un espace avec les chaines de caracteres et utiliser leur label
- avoir des parties dans le programmes [code, chainec, const]
- Ajout de la soustraction
- Gestion des chaînes de caractères
- Création de PyLang, fin de phrase via un `.`
- Création du compilateur TonLang -> LineaLang

## Auteur
Projet personnel développé par Wanako, dans le but d’apprendre à concevoir un langage.