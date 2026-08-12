from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_form, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addexpenses/', views.add_expenses, name='addexpenses'),
    path('editexpenses/<int:pk>/', views.update_expenses, name='editexpenses'),
    # path('viewexpenses/<int:pk>/', views.view_single, name='viewexpenses'),
    path('deletexpenses/<int:pk>/', views.delete_expenses, name='deletexpenses'),
    
    
    path('total/', views.total_expenses, name='totalexpenses'),
]
