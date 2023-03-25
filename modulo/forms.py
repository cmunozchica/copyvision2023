from django.forms import ModelForm
from .models import Trabajo, Producto
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class TrabajoForm(ModelForm):
    class Meta:
        model = Trabajo
        fields = '__all__'
        widgets = {            
            'fecha': DateTimeInput(attrs={'class': 'form-control ', "style" : "width: 16em" }),
            'fechaEntrega': DateTimeInput(attrs={'class': 'form-control', "style" : "width: 16em"}),
                        
        }
       

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoFormUpdate(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {            
            'update': DateTimeInput(attrs={'class': 'form-control ', "style" : "width: 16em" }),

                        
        }

class CustomCreationForm(UserCreationForm):
    
    class Meta:
        model =User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

