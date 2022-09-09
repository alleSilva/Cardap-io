from django.urls import path
from .views import ListMenu, DetailMenu

urlpatterns = [
    path('menu/<int:pk>/', DetailMenu.as_view()),
    path('menu', ListMenu.as_view()),
]