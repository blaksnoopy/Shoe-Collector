from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoes_index, name='index'),
    path('shoes/<int:shoe_id>/', views.shoes_detail, name='detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoes_update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoes_delete'),
    path('shoes/<int:shoe_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('stores/', views.StoreList.as_view(), name='stores_index'),
    path('stores/<int:pk>/', views.StoreDetail.as_view(), name='stores_detail'),
    path('stores/create/', views.StoreCreate.as_view(), name='stores_create'),
    path('stores/<int:pk>/update/', views.StoreUpdate.as_view(), name='stores_update'),
    path('stores/<int:pk>/delete/', views.StoreDelete.as_view(), name='stores_delete'),
]