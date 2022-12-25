from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='home'),
    path('<slug:slug>/', views.viewPost , name='view_post'),
    path('create/', views.createPost , name='create_post'),
    path('update/<int:pk>', views.updatePost , name='update_post'),
    path('delete/<int:pk>', views.deletePost , name='delete_post'),
    path('my-post/', views.myPost, name='my_post'),
]
