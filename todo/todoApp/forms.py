from django import forms
from .models import ToDoModel
class ToDoForm(forms.ModelForm):
    class Meta:
        # Form, ToDoModel modelinin yapisina gore calissin.
        model=ToDoModel

        # Kullanicinin görevin tanimini yapacagi TextField nesnesi gozuksun..
        fields=['task']

        # TextField nesnesine template'in Bootstrap ozelliklerinin yansimasi icin attribute tanimlamalari
        widgets={
            'task':forms.TextInput(attrs={'id':'form1','class':'form-control','placeholder':'Yapılacak görevi giriniz.'})
        }