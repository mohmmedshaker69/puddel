from django.urls import path

from . import views

app_name='convesetion'

urlpatterns=[
    
    path('new/<int:item_pk>/', views.new_convesetion, name='new'),
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    
]