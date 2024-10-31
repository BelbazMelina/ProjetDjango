from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
       path('collection/1/', views.collection_detail, name='collection_detail'),
   ]
