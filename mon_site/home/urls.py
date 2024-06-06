from django.urls import path
from . import views

urlpatterns = [ 
     path('', views.index, name='index'),
     path('article/<int:id>',views.article,name ='article'),
     path('rechercher_article2/',views.rechercher_article2,name ='rechercher_article2'),
     path('recherche_categories2/<str:categories>',views.recherche_categories2,name ='recherche_categories2'),
 ]