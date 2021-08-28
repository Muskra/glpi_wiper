## Description du projet:
Ce programme développé en Python3 a pour but la suppression massive d'objets au sein d'une base GLPI.
Il nécessite l'activation de l'APIrest sur le serveur vers lequel le script enverra les requêtes.
***
## Dépendances:
### Modules Python:
os, sys, configparser, requests

### Fonctionnement:
***
Le script nécessite le remplisage d'un fichier de config situé à sa racine:
config.ini
### Différentes catégories d'options disponibles:
***
### Obligatoires:
### [Server]
***
#### Contenu:
```
Le lien http de votre serveur glpi:
url=http://adresse.exemple.local/glpi

N/B: Vous pouvez aussi saisir une adresse IP mais dois contenir à la fin le /glpi 
exemple: http://192.168.1.55/glpi

Le jeton de connexion de l'utilisateur:
user_token=VOTRE_TOKEN

Et celui de l'application:
app_token=TOKEN_APPLICATION
```
### [Object-Type]
***
#### Contenu:
```
Le type d'appareil/ou catégorie d'appareils ciblée:
device=Computer

N/B: Types d'appareils utilisables: Computer, Monitor, NetworkEquipment, Peripheral, Phone, Printer, Software
```
### Optionnelles:

### [Options]
***
#### Contenu:
```
Cible les objets de la corbeille ou non. (0 ou 1)
0 est la valeur par défaut et signifie que l'on ne cible pas la corbeille.
is_deleted=0

Vous pouvez spécifier un interval afin d'aller chercher un nombre d'objets précis à chaque itération du script. La valeur par défaut est: 0-10000
Celle-ci ne dois pas éxcéder l'option: max_range
Vous pouvez aussi la décrire comme par exemple: 42-4577
items_range=0-10000

L'option ci dessous permet de choisir combien d'objets au maximum nous allons supprimer (n'éxcédant pas 999999). ex: max_range=4577
max_range=

ATTENTION La prochaine option quand à elle permet d'outre-passer les mise en corbeille et donc de supprimer totalement tout objet traité par le script qu'ils soient dans la corbeille ou non. A utiliser avec précaution.
Valeur par défaut: False (True l'active)
wipe=False
```
### Exemple de configuration avec toutes les options réunies:
***
```
# This is the config file of GLPI_wiper
[Server]
url=http://my.url.lan/glpi
user_token=df4ef5qs57f5f
app_token=dq8z7d48q7d586qd4
[Object-Type]
device=Software
[Options]
is_deleted=0
items_range=0-1000
max_range=4577
wipe=False
``` 
