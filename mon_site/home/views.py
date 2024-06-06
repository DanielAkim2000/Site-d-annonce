from django.shortcuts import render
from .models import home
from .forms import new_articlesForm
from django.shortcuts import redirect
from django.db.models import Q
from django.core.paginator import Paginator
from compte.models import Profil


def index(request): 
      if request.user.is_authenticated:
          return redirect('index2') 
          
      articles = home.objects.order_by('-id').all()
      paginator = Paginator(articles, 10)
      page_number = request.GET.get('page')
     
      page_object = paginator.get_page(page_number)
      articles_number = home.objects.count()
      message = f'{articles_number} articles :'
      
      if articles_number ==1 :
             message = f'{articles_number} article:'
      
      context = {
            'articles':page_object, 
            'articles_number':articles_number,
      }
      return render(request,'pages/home/index.html',context)


def article(request ,id):
      article = home.objects.get(id=id)
      profil = Profil.objects.get(user=article.user_id)
      context = {
            'article':article,
            'profil':profil,
      }
      return render(request,'pages/home/article.html',context)

def rechercher_article2(request):
      recherche2 = request.GET.get('recherche2')
      articles = home.objects.order_by('-id').filter(Q(titre__icontains=recherche2) |
                                    Q(description__icontains=recherche2 ))
      articles_number = articles.count()
      
      message = f'{articles_number} résultats :'
      
      if articles_number ==1 :
             message = f'{articles_number} résultat:'
      
      context = {
            'articles':articles, 
            'articles_number':articles_number,
            'message':message
      }
      return render(request,'pages/home/rechercher_article2.html',context)      

def recherche_categories2(request,categories):
      article = home.objects.order_by('-id').filter(categories=categories)
      articles_number = article.count()
      
      message = f'{articles_number} résultats :'
      
      if articles_number ==1 :
             message = f'{articles_number} résultat:'
      
      context = {
            'article':article, 
            'articles_number':articles_number,
            'message':message,
      }
      return render(request,'pages/home/recherche_categories.html',context)

