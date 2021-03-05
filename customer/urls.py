from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('viewDashboard/', views.viewDashboard, name='viewDashboard'),
    path('logout/', views.logut, name='logout'),
]
