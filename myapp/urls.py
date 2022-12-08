from django.urls import path,include
from . import views
urlpatterns=[path('',views.Home,name='Home'),
    path('login',views.login,name='login'),
    path('SignUp',views.SignUp,name='SignUp'),
    path('cart',views.cart1,name='cart'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about')]
    # path('setsession',views.setsession),
    # path('getsession',views.getsession)]