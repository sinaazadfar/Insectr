from django.urls import path
from .views import *

urlpatterns = [
    path('child/', child_list, name='child-list'),
    path('child/<int:pk>/', child_detail, name='child-detail'),
    path('layer_three/', layer_three_list, name='layer-three-list'),
    path('layer_three/<int:pk>/', layer_three_detail, name='layer-three-detail'),
    path('layer_two/', layer_two_list, name='layer-two-list'),
    path('layer_two/<int:pk>/', layer_two_detail, name='layer-two-detail'),
    path('layer_one/', layer_one_list, name='layer-one-list'),
    path('layer_one/<int:pk>/', layer_one_detail, name='layer-one-detail'),
    path('category/', category_list, name='category-list'),
    path('category/<int:pk>/', category_detail, name='category-detail'),
    path('arthropod/', arthropod_list, name='arthropod-list'),
    path('arthropod/<int:pk>/', arthropod_detail, name='arthropod-detail'),
]
