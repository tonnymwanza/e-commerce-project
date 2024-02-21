from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('view_cart', views.view_cart, name='view_cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout', views.checkout, name='checkout'),
    path('profile', views.profile, name='profile'),
    path('confirmation', views.confirmation, name='confirmation'),
]