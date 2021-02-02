from django.urls import path, include
from . import views

urlpatterns = [
    path('category/<str:slug>/', views.PostListByCategory.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]
