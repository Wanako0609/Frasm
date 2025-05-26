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


#### Tableau des instructions minimalistes

| Mot-clé                                        | Description                                                    |
|------------------------------------------------|----------------------------------------------------------------|
| `definir a 10`                                 | affecter un nombre à une variable                              |
| `charger .nom_de_chaine. chaine de charactere` | permet de definir une chainec                                  | 
| `ecrire a`                                     | afficher la valeur d’une variable ou d'une chaine de caractere |
| `si a == 10 (instruction)`                     | condition                                                      |
| `aller label`                                  | saut inconditionnel                                            |
| `fin`                                          | arret du programme                                             |


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


afficher_fin:
charger .fin_. Fin du programme
ecrire .fin_.
fin
```
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