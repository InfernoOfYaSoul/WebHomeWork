from django.urls import path
from . import views

urlpatterns = [
    #path('', views.first_page, name='post_list'),
    path('second/', views.next_page, name='next_page'),
    path('', views.name_input, name='name_input'),
    path('', views.first_page, name = "startpage")
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]