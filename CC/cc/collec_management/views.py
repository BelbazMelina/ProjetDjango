from django.shortcuts import render
<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
from .models import Collec

# Create your views here.
 

def collection_detail(request, n):
       collection = get_object_or_404(Collec, id=n)
       return render(request
       ,'collec_management/collection_detail.html'
       , {'collection': collection})
       
def about(request):
    return render(request,'collec_management/presentation.html')

    
