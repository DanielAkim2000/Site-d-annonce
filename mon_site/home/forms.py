from django import forms
from .models import home

Choix_Region = [
    ('Casablanca - Settat', 'Casablanca - Settat'),
    ('Marrakech - Safi', 'Marrakech - Safi'),
    ( 'Tanger - Tétouan - Al Hoceima',  'Tanger - Tétouan - Al Hoceima'),
    ('L\'Oriental','L\'Oriental'),
    ('Rabat - Salé - Kénitra','Rabat - Salé - Kénitra'),
    ('Beni Mellal - Khénifra','Beni Mellal - Khénifra'),
    ('Drâa - Tafilalet','Drâa - Tafilalet'),
    ('Souss -Massa','Guelmim - Oued Noun'),
    ('Laâyoune - Saguia al Hamra','Laâyoune - Saguia al Hamra'),
    ('Dakhla - Oued Ed-Dahab','Dakhla - Oued Ed-Dahab'),

]

Choix_catego= [
  ('Véhicules','Véhicules'),
  ('Appareils électroniques','Appareils électroniques'),
  ('Vêtements','Vêtements'),
  ('Immobilier','Immobilier'),
  ('Petites annonces','Petites annonces'),
  ('Loisirs','Loisirs'),
  ('Musique','Musique'),
  ('Sports','Sports'),
]
class new_articlesForm(forms.ModelForm):
  titre = forms.CharField(label='Titre:' , widget=forms.TextInput(attrs={
    'class':'form-control'
  }))
  description = forms.CharField(label='Description:' ,widget=forms.Textarea(attrs={
    'class':'form-control'
  }))
  prix = forms.IntegerField(label='Prix:' , widget=forms.NumberInput(attrs={
    'class':'form-control',
  }))
  region = forms.CharField(label='Région:' ,widget=forms.Select(choices=Choix_Region,attrs={
    'class':'form-control'
  }))
  image_url = forms.ImageField(label='Photo de l\'article', widget=forms.FileInput(attrs={
    'class':'form-control',
    }))  
  categories = forms.CharField(label='Catégorie:' ,widget=forms.Select(choices=Choix_catego,attrs={
    'class':'form-control'
  }))  
  class Meta:
      model = home
      fields = ['titre','description','image_url','region','prix','categories',]
