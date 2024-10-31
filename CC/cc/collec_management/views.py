
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from .models import Collec
from datetime import date

# Create your views here.
 

       
def about(request):
    return render(request,'collec_management/presentation.html')

    #QUESTION 5
def collection_detail(request, n):
       collection = get_object_or_404(Collec, id=n)
       return render(request
       ,'collec_management/collection_detail.html'
       , {'collection': collection})
#Q6

def collection_list(request):
  collections = Collec.objects.all()
  context = {'collections': collections}
  return render(request, 'collec_management/collection_list.html', context)

#Q7

def new_collec(request):
    if request.method == 'POST':
        form = CollecForm(request.POST)
        if form.is_valid():
            collec = form.save(commit=False)
            collec.date_creation = date.today()
            collec.save()
            return redirect('collection_list')
    else:
        form = CollecForm()
    return render(request, 'new_collec.html', {'form': form})

#Q8
def collection_delete(request, n):
  collection = get_object_or_404(Collec, id=n)
  
  if request.method == 'POST':
      collection.delete()
      return redirect('collection_list') 

 
  return render(request, 'collec_management/collection_confirm_delete.html', {'collection': collection})

