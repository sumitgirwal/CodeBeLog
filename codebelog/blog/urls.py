from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('view/<int:pk>', views.viewPost , name='view'),
    path('create/', views.createPost , name='create'),
    path('update/<int:pk>', views.updatePost , name='update'),
    path('delete/<int:pk>', views.deletePost , name='delete'),
]
