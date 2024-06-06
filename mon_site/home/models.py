from django.db import models
from django.contrib.auth.models import User



class home(models.Model):
    id = models.BigAutoField(primary_key=True)
    titre=models.CharField(max_length=500)
    description=models.CharField(max_length=2000)
    image_url=models.ImageField(upload_to='post_img')
    user_id= models.ForeignKey(User,on_delete=models.CASCADE) 
    region = models.CharField(max_length=100)
    prix = models.IntegerField()
    categories = models.CharField(max_length=100)
    def __str__ (self):
        return  self.titre