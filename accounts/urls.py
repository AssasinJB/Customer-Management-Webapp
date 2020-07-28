from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('customer/<str:pk>/',views.customer,name = 'customer'),
    path('products/',views.products,name = 'products'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.register_page,name='register'),
    path('user/',views.userPage,name='user-page'),
    path('create_order/<str:pk>/',views.create_Order,name = 'create_order'),
    path('update_order/<str:pk>/',views.update_Order,name = 'update_order'),
    path('delete_order/<str:pk>/',views.delete_Order,name = 'delete_order'),
]