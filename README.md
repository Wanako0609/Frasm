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
Initialisation:
# Chargement des chaines de characteres
charger .debut. Bonjour, merci d'utiliser France Assembleur
charger .boucle. Voici une boucle jusqu'a 10
charger .debut_boucle. Debut de la boucle
charger .i=. i=
charger .fin_boucle. La boucle est fini
# Definition des variables
definir incrementeur_1 1
definir i 0
definir max 10

revenir

# Sous partie principale
Principale:
ecrire .debut.
ecrire .boucle. .debut_boucle.
ecrire .i=. i

aller Boucle

# Condition de la boucle
Boucle:
si i >= max aller Fin_boucle
sinon aller Incrementer
fin

# Incrementation + code executer durant la boucle
Incrementer:
somme i incrementeur_1 i
ecrire .i=. i
aller Boucle

# Fin de la boucle
Fin_boucle:
ecrire .fin_boucle. .i=. i
fin
```

**Résultat attendu :**

```
Bonjour, merci d'utiliser France Assembleur 
Voici une boucle jusqu'a 10 Debut de la boucle 
i= 0 
i= 1 
i= 2 
i= 3 
i= 4 
i= 5 
i= 6 
i= 7 
i= 8 
i= 9 
i= 10 
La boucle est fini i= 10 
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
