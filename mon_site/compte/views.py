from django.shortcuts import render
from .models import home,User,Profil
from .forms import new_articlesForm , UserForm , ProfilForm,compteForm,comptePForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator


@login_required
def index2(request): 
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
            'message':message,
            
      }
      return render(request,'pages/compte/index2.html',context)

@login_required
def article2(request ,id):
      article = home.objects.get(id=id)
      profil = Profil.objects.get(user=article.user_id)
      context = {
            'article':article,
            'profil':profil,
      }
      return render(request,'pages/compte/article2.html',context)
     
@login_required
def new_article2(request):
      if request.method == 'POST':
            form = new_articlesForm(request.POST , request.FILES )
            if form.is_valid():
             saves = form.save(commit=False)
             saves.user_id = request.user     
             form.save()
             return redirect('index2')

      else:
         form = new_articlesForm()

      context = {
            'form':form,
      }
      return render(request,'pages/compte/new_article.html',context)    

@login_required
def update_article2(request, id):    
  article = home.objects.get(id=id)
  if article.user_id == request.user:
        if request.method == 'POST':
             form = new_articlesForm(request.POST , request.FILES ,instance=article)
             if form.is_valid():
              if article.user_id == request.user:
               form.save()
               return redirect('index2')

        else:
         form = new_articlesForm(instance=article)
  else:
        raise Http404
     
  context = {
            'form':form,
            'article':article,
      }
  return render(request,'pages/compte/update_article.html',context)

@login_required
def delete_article2(request,id):
      article = home.objects.get(id=id)
      if article.user_id == request.user:
        article.delete()
        return redirect('index2')
      else:
        raise Http404  
      return render(request, 'pages/compte/delete_article.html')

def user_enregistrer(request):
    if request.user.is_authenticated:
          return redirect('index2')  
    if request.method == 'POST':
          form = UserForm(request.POST)
          profil= ProfilForm(request.POST,request.FILES)
          if form.is_valid() and profil.is_valid() :
              savef = form.save(commit=False)
              savep = profil.save(commit=False)
              savep.user = savef
              savef.save()
              savep.save()
              profil.save_m2m() 
              form.save_m2m()
              return redirect('login')   
    else:
             form = UserForm()
             profil = ProfilForm()     
             
    context = {
          'form': form,
          'profil' : profil ,
    }       
    return render(request,'pages/compte/user_enregistrer.html', context)

@login_required
def recherche_article(request):
      recherche = request.GET.get('recherche')
      article = home.objects.order_by('-id').filter(Q(titre__icontains=recherche) |
                                    Q(description__icontains=recherche ))
      articles_number = article.count()
      
      message = f'{articles_number} résultats :'
      
      if articles_number ==1 :
             message = f'{articles_number} résultat:'
      
      context = {
            'article':article, 
            'articles_number':articles_number,
            'message':message,
      }
      return render(request,'pages/compte/rechercher_article.html',context)    

@login_required
def mon_profil(request,id):
        users= User.objects.get(id=id)  
        profil = Profil.objects.get(user=users)
        form = compteForm(instance=users)
        profilF = comptePForm(instance=profil)
        articles = home.objects.filter(user_id=users.id)
        articles_number = articles.count()
        message = f'{articles_number} annonces :'  
        if articles_number ==1 :
           message = f'{articles_number} annonce:'
        context = {
              'articles':articles,
              'message':message,
              'form':form,
              'profil':profilF,
              'user':users,
              'profilpp':profil,
        } 
        return render(request,'pages/compte/mon_compte.html',context)


@login_required
def recherche_categories(request,categories):
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
      return render(request,'pages/compte/recherche_categories.html',context) 
# Create your views here.


