from django.shortcuts import render,redirect
from .forms import ToDoForm

from .models import ToDoModel

# Create your views here.

def todo(request):
    tasks=ToDoModel.objects.all()
    
    if request.method=="GET":
        form=ToDoForm(request.GET)
        if form.is_valid():
            form.save()
            form=ToDoForm()
    else:
        form=ToDoForm()

    context={
        'form':form,
        'tasks':tasks
    }
    return render(request,"index.html",context)

# Sil ve Tamamlandi butonlarina tiklanildigi zaman
# bu metotlar calisacak ve kullanici tekrar temiz index.html
# sayfasina yonlendirilecek.
def delTask(request,id):
    instance=ToDoModel.objects.get(id=id)
    instance.delete()

    form=ToDoForm()
    context={
        'form':form
    }

    return redirect("/")

def completeTask(request,id):
    instance=ToDoModel.objects.get(id=id)
    instance.status='Tamamlandı'
    instance.save()
    return redirect("/")