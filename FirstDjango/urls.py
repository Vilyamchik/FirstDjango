from MainApp import views
from django.urls import path



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('item/<int:item_id>/', views.get_item, name='get_item'),
    path('items/', views.get_items, name='get_items'),
]


