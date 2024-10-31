
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
       path ("about/",views.about, name="about"),
]
#Q5
urlpatterns = [
       path('collection/<int:n>/', views.collection_detail, name='collection_detail'),
   ]

#Q6
urlpatterns = [
  path('collection/<int:n>/', views.collection_detail, name='collection_detail'),
  path('all/', views.collection_list, name='collection_list'),  # Nouvelle route pour la liste des collections
]
#Q8
urlpatterns = [
  path('collection/<int:n>/', views.collection_detail, name='collection_detail'),
  path('all/', views.collection_list, name='collection_list'),
  path('delete/<int:n>/', views.collection_delete, name='collection_delete'),  # Route pour la suppression
]
   
