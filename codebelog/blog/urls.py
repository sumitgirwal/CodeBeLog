from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='home'),
    
    path('create/', views.createPost , name='create_post'),
    path('update/<int:pk>', views.updatePost , name='update_post'),
    path('delete/<int:pk>', views.deletePost , name='delete_post'),
    path('my-post/', views.myPost, name='my_post'),
    path('likepost/', views.likePost, name='like_post'),

    # check slug after check above urls
    path('<slug:slug>/', views.viewPost , name='view_post'),
]
