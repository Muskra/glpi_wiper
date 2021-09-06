## Project description:
This Python3 program let you massively remove objects from the glpi RestAPI.
This program is free of charge and can be forked by anyone who want's to.
There is no warranty of any king and i am not responsible of any kind of damage made by the program.

***
## Dependencies:
### Python'n modules:
os, sys, configparser, requests
### Into GLPI:
To make it work activate the RestAPI that provide GLPI, and generate the tokens needed by the program.

### Usage:
You need to create a config.ini file (if not created) into the root of the program (where main.py is).

### Available options:

### Mandatory Options:
### [Server]
***
#### Content:
```
# HTTP link of the glpi server:
url=http://adress.example.subdomain.domain/glpi

# N/B: You can also use IP address. Do not forget the /glpi at the end of the link 
# example: http://192.168.1.55/glpi

# User token to authenticate to RestAPI:
user_token=VOTRE_TOKEN

# And the application one:
app_token=TOKEN_APPLICATION
```
### [Object-Type]
***
#### Content:
```
# Device type you want to remove:
device=Computer

# N/B: Type that exists by default: Computer, Monitor, NetworkEquipment, Peripheral, Phone, Printer, Software
```
### Optionals:

### [Options]
***
#### Content:
```
# If you want to remove the trashbin items, 0 is default and 1 means deleted ones.
is_deleted=0

# By default the program will iterate through a default range of items: 0-10000 (0 to 10000).
# You can specify a specific number of items as needed.
# This option can't exceed the max_range option.
# example: 42-4577
items_range=0-10000

# The option below will determinate the maximum range the wiper will act. 
# Do NOT forget that it will goes from the end of the range like:
# If you have items_range=0-4577 it will remove first the 4577 lasts items from the base.
# This option can't exceed 999999 items and can be further from the items_range option.
max_range=

# BEWARE the last option can be dangerous if you're not carefull when using it.
# It's needed when you remove items from the trashbin. BUT, if you use it on a range of items that are not already in the trashbin, it will erase all of them from the base. USE WITH CAUTION.
# Default value is False (True will activate it)
wipe=False
```
### Configuration example with all options:
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
