
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
       path ("about/",views.about, name="about"),
       path('collection/<int:n>/', views.collection_detail, name='collection_detail'),#5
       path('all/', views.collection_list, name='collection_list'), #6 Nouvelle route pour la liste des collections
       path('new/', views.new_collec, name='new_collec'),#7
       path('delete/<int:n>/', views.collection_delete, name='collection_delete'),#8 Route pour la suppression
       path('edit/<int:id>/', edit_collection, name='edit_collection'),      
]
