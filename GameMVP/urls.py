"""
Definition of urls for GameMVP.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
#from api.models import CartCount
#CartUserCount=CartCount()

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    path('game/',views.game,name="game"),
    path('product/',views.product,name="product"),

    path('Cart/',views.Cart,name="Cart"),
  path('Checkout/',views.Checkout,name="Checkout"),
  path('MyGames/',views.MyGames,name="MyGames"),
  path('PayGames/',views.PayGames,name="PayGames"),
  

    path('NewAccount/',views.NewAccount, name='NewAccount'),
    path('admin/', admin.site.urls),

   path("ajax/RemoveCartGame/",views.RemoveCartGame,name='RemoveCartGame'),
]
