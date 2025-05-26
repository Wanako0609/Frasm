# FRASM

**FRASM** (abréviation de FRAASM : "France Assembleur") est un langage de programmation de type assembleur, minimaliste et entièrement en français.  
Il est conçu pour être simple, lisible et exécuté à l'aide d'une machine virtuelle en Python.

---

## Objectifs

### Personnel
Créer un langage simple pour comprendre :
- la création d’un langage interprété
- la gestion des variables, instructions, sauts et conditions

### Langage
Proposer un langage éducatif accessible à un large public, en brisant la barrière de la langue.  
Offrir une implémentation claire, basée sur des opérations logiques simples.  
FRASM s’inspire du pseudo-code et facilite l’apprentissage des bases de la programmation.

---

## Syntaxe de base

Le programme est structuré en différentes sections, dont la section `Principal:`, dans laquelle se trouve la partie principale du programme.  

### Instructions minimales

| Mot-clé                                         | Description                                                   |
|------------------------------------------------|---------------------------------------------------------------|
| `definir a 10`                                  | Affecte un nombre à une variable                              |
| `charger .nom_de_chaine. chaîne de caractères` | Définit une chaîne de caractères référencée (`chainec`)       |
| `ecrire a`                                      | Affiche la valeur d’une variable ou d’une chaîne de caractères |
| `si a == 10 (instruction)`                      | Condition (égalité ou différence)                             |
| `aller label`                                   | Saut inconditionnel vers un label                             |
| `fin`                                           | Arrête l’exécution du programme                               |

---

## Exemple de programme FRASM

```frasm
Principal: # Section principale obligatoire
definir a 10 # a = 10
definir b 5  # b = 5
somme a b total # total = a + b
ecrire total # affiche 15
si total > 10 aller Plus_10 
sinon aller Moins_10

Plus_10:
charger .afficher. 10 + 5 = 
ecrire .afficher.
ecrire total
aller Fin_Affichage

Moins_10:
charger .afficher. 10 - 5 = 
ecrire .afficher.
ecrire total
aller Fin_Affichage

Fin_Affichage:
charger .fin_. Fin du programme
ecrire .fin_.
fin
```

**Résultat attendu :**

```
15
10 + 5 = 15
Fin du programme
```

---

## Installation

Ce projet ne nécessite aucune dépendance.
Utilisez Python 3.12 ou supérieur.

---

## Exécution

```bash
python3 main.py mon_programme.frasm
```

---

## Organisation des dossiers

* `programmes/` : contient des exemples de programmes en FRASM (`.frasm`)
* `docs/` : contient la documentation et les spécifications du langage
* `libs/` : contient les composants internes du langage (machine virtuelle, instructions, etc.)

---

## À venir

* Création de PyLang, un langage plus haut niveau compilé vers FRASM
* Fin de ligne via un `.` dans PyLang
* Création du compilateur PyLang → FRASM

---

## Auteur

Projet personnel développé par Wanako, dans le but d’apprendre à concevoir un langage de programmation simple et pédagogique.
