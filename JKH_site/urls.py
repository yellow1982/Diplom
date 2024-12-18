from django.urls import path
from .views import *
app_name = 'JKH_site'

urlpatterns = [

    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    path('', home_page, name='home_page'),
    path('logout/', user_logout, name='logout'),
    path('info/', info, name='info'),
    path('trades/', trades, name='trades'),
    path('trades/<slug:slug>/', trades, name='trades'),
    path('my_products/', my_products, name='my_products'),
    path('product_adding/', product_adding, name='product_adding'),
    path('product_delete/<int:id>/', product_delete, name='product_delete')

]



