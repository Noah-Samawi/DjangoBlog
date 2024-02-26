from . import views
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
