from django.urls import path
from . import views

urlpatterns = [
    path('',views.FoodListView.as_view(), name='list'),
    
]