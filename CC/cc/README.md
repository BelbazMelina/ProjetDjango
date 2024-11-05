# Membres du groupe :
- Belbaz Belkais Melina: belkais-melina.belbaz@etu.univ-orleans.fr
- HIBAT ALLAH MAZER : hibat-allah.mazer@etu.univ-orleans.fr
- zenasni amina : amina.zenasni@etu.univ-orleans.fr
<<<<<<< HEAD
=======


>>>>>>> 4e9d6aa53b81c6260c10b96914480076547946dc
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
<<<<<<< HEAD
# ajout de fichier json 
(django) [ dell | ~/workspace/cc ] python manage.py loaddata examples
Installed 12 object(s) from 1 fixture(s)
# Vérification : vérifier que les collections ont bien été ajoutées :

- python manage.py shell
- Puis dans le shell :

- from myapp.models import Collec
- Collec.objects.all()
=======
>>>>>>> 9f33fbe47055acf0594a62b187d6b205f125af9b

## Question 5
- Création de la vue `collection_detail` et du template `collec_details.html`

## Question 6
- Création de la vue `collection_list` et du template `collection_list.html`
## Question 8
- Création de la vue `collection_delete` et du template `collection_confirm_delete.html`

