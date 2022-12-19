from django.urls import path
from . import views

urlpatterns = [

   path('login/', views.userLogin , name='login'),
   path('logout/', views.userLogout , name='logout'),
   path('signup/', views.userSignup , name='signup')
   
]
