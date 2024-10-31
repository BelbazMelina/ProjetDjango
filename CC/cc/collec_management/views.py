from django.shortcuts import render,redirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Collec
from django.views.generic.edit import UpdateView

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

#Q8
def collection_delete(request, n):
  collection = get_object_or_404(Collec, id=n)
  
  if request.method == 'POST':
      collection.delete()
      return redirect('collection_list') 

 
  return render(request, 'collec_management/collection_confirm_delete.html', {'collection': collection})
    

def edit_collection(request, id):
    collection = get_object_or_404(Collec, pk=id)
    if request.method == 'POST':
        form = CollecForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('collection_list', id=collection.id)
    else:
        form = CollecForm(instance=collection)
    return render(request, 'edit_collection.html', {'form': form})
