# Membres du groupe :
- Belbaz Belkais Melina: belkais-melina.belbaz@etu.univ-orleans.fr
- HIBAT ALLAH MAZER : hibat-allah.mazer@etu.univ-orleans.fr
- zenasni amina : amina.zenasni@etu.univ-orleans.fr

# les commandes :
# Question 1:
# sur terminal linux
- USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) USERID=$(id -u) docker-compose up -d
# sur vs code (ouverir le contenaire crée) ensuite on ouvre le terminale vs code
- ls
- workspace
- cd workspace
- django-admin startproject cc
- cd cc
- python manage.py runserver 127.0.0.1:8080
- python manage.py migrate
- python manage.py startapp collec_management
# ensuite on ouvre le doc cc et ensuite settings.py dans terminal linux
# on ajoute la ligne suite 
     INSTALLED_APPS = [
         ...
         'collec_management',
     ]