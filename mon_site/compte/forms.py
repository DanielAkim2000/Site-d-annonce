from home.forms import new_articlesForm
from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .models import Profil
# forms creations
Choix_Sex = [
  ('HOMME','Homme'),
  ('FEMME','Femme'),
]
class LoginForm(AuthenticationForm):
 username = forms.CharField(label='Nom d\'utilisateur' , widget=forms.TextInput(attrs={
    'class':'form-control'
  }))
 password = forms.CharField(label='Mot de passe' , widget=forms.PasswordInput(attrs={
    'class':'form-control'
  }))

class UserForm(UserCreationForm):
   username = forms.CharField(label='Nom d\'utilisateur' , widget=forms.TextInput(attrs={
    'class':'form-control'
  }))
   password1 = forms.CharField(label='Mot de passe' ,help_text='*Ce mot de passe doit contenir au minimum 8 caractères.', widget=forms.PasswordInput(attrs={
    'class':'form-control'
  }))
   email = forms.CharField(label='Email' ,help_text='*Veuillez saisir une adresse non assignée à un compte', widget=forms.EmailInput(attrs={
    'class':'form-control'
  }))
   password2 = forms.CharField(label='Confirmation Mot de passe' ,help_text='*Entrez à nouveau le mot de passe', widget=forms.PasswordInput(attrs={
    'class':'form-control'
  }))
   first_name = forms.CharField(label='Prénom' , widget=forms.TextInput(attrs={
    'class':'form-control'
  }))
   last_name = forms.CharField(label='Nom' , widget=forms.TextInput(attrs={
    'class':'form-control'
  }))
   class Meta:
     model = User
     fields = ('username','email','first_name','last_name','password1','password2')

class ProfilForm(forms.ModelForm):
    date_naissance = forms.DateField(label='Date de naissance:' , widget=forms.DateInput(attrs={
    'class':'form-control',
    'type' : 'date',
  }))
    tel = forms.CharField(label='Numéro de télephone:' , widget=forms.NumberInput(attrs={
    'class':'form-control',
    'type': 'tel',
  }))
    photo_profil = forms.ImageField(label='Photo de profil:', widget=forms.FileInput(attrs={
     'class':'form-control',
  }))
    sex = forms.CharField(label='Sexe:' ,widget=forms.Select(choices=Choix_Sex,attrs={
    'class':'form-control'
  }))
    class Meta:
       model = Profil 
       fields = ['date_naissance','tel','photo_profil','sex']


class compteForm(UserCreationForm):
   username = forms.CharField(label='Nom d\'utilisateur' , widget=forms.TextInput(attrs={
    'class':'form-control',
    'disabled' : 'disabled',
  }))
   email = forms.CharField(label='Email' , widget=forms.TextInput(attrs={
    'class':'form-control',
    'disabled' : 'disabled',
  }))
   first_name = forms.CharField(label='Prénom' , widget=forms.TextInput(attrs={
    'class':'form-control',
    'disabled' : 'disabled',
  }))
   last_name = forms.CharField(label='Nom' , widget=forms.TextInput(attrs={
    'class':'form-control',
    'disabled' : 'disabled',
   }))
   date_joined = forms.CharField(label='Date d\'inscription' , widget=forms.TextInput(attrs={
    'class':'form-control',
    'disabled' : 'disabled',
   }))
   password1 = forms.CharField(label='Mot de passe' , widget=forms.PasswordInput(attrs={
    'class':'form-control',
    'disabled' : 'disabled',
  }))
   password2 = forms.CharField(label='Mot de passe' , widget=forms.PasswordInput(attrs={
    'class':'form-control',
    'disabled' : 'disabled',
  }))
   class Meta:
        model = User
        fields = ['username','email','first_name','last_name','date_joined','password1','password2']

      
class comptePForm(forms.ModelForm):
    date_naissance = forms.DateField(label='Date de naissance:' , widget=forms.TextInput(attrs={
    'class':'form-control',
    'type' : 'date',
    'disabled' : 'disabled',
  }))
    tel = forms.CharField(label='Numéro de télephone:' , widget=forms.NumberInput(attrs={
    'class':'form-control',
    'type': 'tel',
    'disabled' : 'disabled',
  }))
    sex = forms.CharField(label='Sexe:' ,widget=forms.TextInput(attrs={
    'class':'form-control',
    'disabled' : 'disabled',
  }))    
    class Meta:
        model = Profil 
        exclude = ['photo_profil','user']