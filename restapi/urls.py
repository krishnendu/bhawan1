from django.urls import path
from . import views

urlpatterns = [
    path('auth/',views.authenticated, name='authenticated'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('user/',views.users_list, name='users_list'),
    path('user/switchnames/',views.switch_name, name='switch_name'),
    path('user/<str:token>/',views.switch, name='user_switches'),


]