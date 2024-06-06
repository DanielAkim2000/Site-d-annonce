from django.urls import path
from . import views as views2
from django.contrib.auth import views
from .forms import LoginForm

urlpatterns = [ 
    path('login/',views.LoginView.as_view(template_name='pages/compte/login.html',redirect_authenticated_user=True, authentication_form=LoginForm ) ,name='login'),
    path('', views2.index2, name='index2'),
    path('article2/<int:id>',views2.article2,name ='article2'),
    path('new_article2/',views2.new_article2, name='new_article2'),
    path('update_article2/<int:id>',views2.update_article2,name='update_article2'),
    path('delete_article2/<int:id>',views2.delete_article2, name='delete_article2'),
    path('logout/',views.LogoutView.as_view(template_name='pages/compte/logout.html', next_page='login') ,name='logout'),
    path('user_enregistrer/',views2.user_enregistrer,name='user_enregistrer'),
    path('rechercher_article/',views2.recherche_article,name='rechercher_article'),
    path('mon_compte/<int:id>',views2.mon_profil,name= 'mon_compte'),
    path('recherche_categories/<str:categories>',views2.recherche_categories,name ='recherche_categories'),
]