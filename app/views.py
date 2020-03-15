"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import NewAccountForm
from django.contrib.auth.models import User
from .models import Product,cart,mygames
from django.http.response import JsonResponse
import uuid 
from django.shortcuts import redirect
from datetime import date
from django.db.models import Count




def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    gameList=Product.objects.all()
    

    
    #firsttag=firstgame.tags
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'games':gameList
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def NewAccount(request):
    """Renders NewAccount Page."""
    assert isinstance(request,HttpRequest)
   # return red
    if request.method=="POST":

        NewUserInfo=NewAccountForm(request.POST)
        useremail=request.POST.get("email", "")
        userusername=request.POST.get("username", "")
        userpassword=request.POST.get("password", "")
        userpasswordconfirm=request.POST.get("passwordconfirmation", "")

        NewUser = User.objects.create_user(userusername, useremail, userpassword)
        NewUser.save()
        return redirect('/login/')


        if NewUserInfo.is_valid():
            info=NewUserInfo.fields
        else:
            return render(
            request,
            'app/NewAccount.html',
            {
                'title':"New Account",
                'message':'Setup your New Account',
                'year':datetime.now().year,
                'form':NewAccountForm()
            })
            
            
        
            #Password is good

        
        
        

    if request.method=="GET":
        return render(
        request,
        'app/NewAccount.html',
        {
            'title':"New Account",
            'message':'Setup your New Account',
            'year':datetime.now().year,
            'form':NewAccountForm()
        }
    )


def game(request):
    assert isinstance(request,HttpRequest)
    gameID=request.GET.get("id")
    SelectedGame=Product.objects.prefetch_related('tags').prefetch_related('categories').prefetch_related('gameplayimages_set').prefetch_related('youtubevideo_set').get(id=gameID)
    tags = [sub.name for sub in SelectedGame.tags.all()]
    categories=[sub.name for sub in SelectedGame.categories.all()]
    images=[sub.imageURL for sub in SelectedGame.gameplayimages_set.all()]
    youtubevideos=[sub.videourl for sub in SelectedGame.youtubevideo_set.all()]
    #SelectedGame.tags=tags
    #firsttag=SelectedGame.tags[0]
    return render(
        request,
        'app/game.html',
        {
            'title':SelectedGame.name,
            'message':'Your application description page.',
            'year':datetime.now().year,
            'game':SelectedGame,
            'categories':categories,
            'tags':tags,
            'categories':categories,
            'images':images,
            'youtubevideo':youtubevideos
        })

def product(request):
    assert isinstance(request,HttpRequest)
    gameID=request.GET.get("id")
    SelectedGame=Product.objects.prefetch_related('tags').prefetch_related('categories').prefetch_related('gameplayimages_set').prefetch_related('youtubevideo_set').get(id=gameID)
    tags = [sub.name for sub in SelectedGame.tags.all()]
    categories=[sub.name for sub in SelectedGame.categories.all()]
    images=[sub.imageURL for sub in SelectedGame.gameplayimages_set.all()]
    youtubevideos=[sub.videourl for sub in SelectedGame.youtubevideo_set.all()]
    #SelectedGame.tags=tags
    #firsttag=SelectedGame.tags[0]
    return render(
        request,
        'app/game.html',
        {
            'title':SelectedGame.name,
            'message':'Your application description page.',
            'year':datetime.now().year,
            'game':SelectedGame,
            'categories':categories,
            'tags':tags,
            'categories':categories,
            'images':images
            #'youtubevideo':youtubevideos
        })

def Cart(request):
    assert isinstance(request,HttpRequest)
    current_user = request.user
    newproduct_to_cart=request.POST.get("product", "")
    if newproduct_to_cart != None and newproduct_to_cart != '':
        getproduct=Product.objects.all().filter(id=newproduct_to_cart).first()
        alreadyexists_in_cart=cart.objects.all().filter(user=current_user,product=getproduct).first()

        if alreadyexists_in_cart == None:
            p=cart(user=current_user,product=getproduct)
            p.save()

        
    
    cartlist=cart.objects.all().filter(user=current_user).select_related('product')
    #current_user.id

    return render(
        request,
        'app/Cart.html',
        {
            'title':'My Cart',
            'message':'My Cart',
            'year':datetime.now().year,
            'cartlist':cartlist
        })

def Checkout(request):
    assert isinstance(request,HttpRequest)
    current_user=request.user
    

    cartlist=cart.objects.all().filter(user=current_user).select_related('product')
    TotalPrice=0
    for prod in cartlist:
        TotalPrice=TotalPrice+prod.product.price

    return render(
        request,
        'app/Checkout.html',
        {
            'title':'Checkout',
            'message':'Checkout',
            'year':datetime.now().year,
            'cartlist':cartlist,
            'TotalPrice':TotalPrice
        })

def PayGames(request):
    assert isinstance(request,HttpRequest)
    current_user=request.user
    #cartCheckout=request.POST.get("Cart","")
    creditcard=request.POST.get("creditcard","")
    
    cartlist=cart.objects.all().filter(user=current_user).select_related('product')

    for game in cartlist:        
        productkey=str(uuid.uuid1())
        newbuy=mygames(productkey=productkey,dateofpurchase=date.today(),product=game.product,user=current_user)
        newbuy.save()
        game.delete()   

    return redirect(MyGames)


def MyGames(request):
    assert isinstance(request,HttpRequest)
    current_user=request.user
    
    MyGames=mygames.objects.all().filter(user=current_user).select_related('product')
    return render(
        request,
        'app/MyGames.html',
        {
            'title':'My Games',
            'message':'My Games',
            'year':datetime.now().year,
            'MyGames':MyGames            
        })

def Report_Bought(request):
    assert isinstance(request,HttpRequest)
    current_user=request.user
    if current_user.is_staff ==False:
        return redirect(home)

    Bought_games=mygames.objects.all().select_related('product').select_related('user').order_by('-dateofpurchase')
    return render(
        request,
        'app/Report_bought.html',
        {
            'title':'Report Games Bought',
            'message':'Games Bought',
            'year':datetime.now().year,
            'Games':Bought_games            
        })

def Report_Chart(request):
    current_user=request.user
    if current_user.is_staff ==False:
        return redirect(home)

    labels = []
    data = []

    Bought_games=mygames.objects.all().select_related('product').order_by('-dateofpurchase')
    Bought_games_test=mygames.objects.all().select_related('product').aggregate(Count('product'))
    allgames=Product.objects.all()
    
    for game in allgames:
        labels.append(game.name)
        totalbuy=mygames.objects.all().filter(product=game).select_related('product').count()
        print(totalbuy)
        data.append(totalbuy)

        return render(
        request,
        'app/Report_chart.html',
        {
            'title':'Report Charts',
            'message':'Games Bought',
            'year':datetime.now().year,
            'labels': labels,
            'data': data,           
        })






#For AjaxCall
def RemoveCartGame(request):
    current_user = request.user
    cart_to_remove=request.POST.get('id',"")        
    if(cart_to_remove!=None and cart_to_remove!=""):
        #gamefound=Product.objects.get(id=game_to_remove)
        cartgamefound=cart.objects.get(id=cart_to_remove)
        cartgamefound.delete()
        #cart.objects.all().filter(user=current_user,product=gamefound).delete()
        return JsonResponse({'success':True, 'errorMsg':""})

    return JsonResponse({'success':False, 'errorMsg':"Error"})
            