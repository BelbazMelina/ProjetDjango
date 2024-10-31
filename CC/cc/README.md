Membres du groupe :
Belbaz Belkais Melina: belkais-melina.belbaz@etu.univ-orleans.fr
HIBAT ALLAH MAZER : hibat-allah.mazer@etu.univ-orleans.fr
zenasni amina amina.zenasni@etu.univ-orleans.fr

les commandes :
Question 1:
#sur terminal linux
USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) USERID=$(id -u) docker-compose up -d
#sur vs code (ouverir le contenaire crée) ensuite on ouvre le terminale vs code
(django) [ mimichaouaa | ~ ] ls
workspace
(django) [ mimichaouaa | ~ ] cd workspace
(django) [ mimichaouaa | ~/workspace ]     django-admin startproject cc
(django) [ mimichaouaa | ~/workspace ]      cd cc
(django) [ mimichaouaa | ~/workspace/cc ]     python manage.py runserver 0.0.0.0:8000 &
(django) [ mimichaouaa | ~/workspace/cc ]  python manage.py migrate
(django) [ mimichaouaa | ~/workspace/cc ]     python manage.py startapp collec_management
#ensuite on ouvre le doc cc et ensuite settings.py dans terminal linux
cd CC1
cd cc
cd cc
cd cc
cd settings.py 
#on ajoute la ligne suite 
     INSTALLED_APPS = [
         ...
         'collec_management',
     ]
     
cd ..
cd..
cd.. 
nano read.me
