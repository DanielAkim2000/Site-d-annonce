from django.db import models
from home.models import home
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Profil')
    date_naissance = models.DateField()
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    tel = models.CharField(validators = [phoneNumberRegex], max_length = 20, unique = True)
    photo_profil = models.ImageField(upload_to='profil_img' ,null=True )
    sex = models.CharField(max_length=5)
    def __str__ (self):
      return self.user.username