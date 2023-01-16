from django.urls import path
from . import views

urlpatterns=[
    path("",views.todo,name='todo'),
    # URL uzerinden parametre tasinabilmesi icin <str:id> tanimlamasi gereklidir.
    path("delTask/<str:id>/",views.delTask,name='delTask'),
    path("completeTask/<str:id>/",views.completeTask,name='completeTask')
]