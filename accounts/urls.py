from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home,name = 'home'),
    path('customer/<str:pk>/',views.customer,name = 'customer'),
    path('products/',views.products,name = 'products'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('account/',views.account_settings,name= 'account'),
    path('register/',views.register_page,name='register'),
    path('user/',views.userPage,name='user-page'),
    path('create_order/<str:pk>/',views.create_Order,name = 'create_order'),
    path('update_order/<str:pk>/',views.update_Order,name = 'update_order'),
    path('delete_order/<str:pk>/',views.delete_Order,name = 'delete_order'),

    path('reset_password/',auth_views.PasswordResetView.as_view(
        template_name = 'accounts/password_reset.html'
    ),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(
        template_name = 'accounts/password_reset_sent.html'
    ),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name = 'accounts/password_reset_form.html'
    ),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name = 'accounts/password_reset_done.html'
    ),name='password_reset_complete'),
]