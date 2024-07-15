
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_expense, name='add_expense'),
    path('monthly_summary/', views.monthly_summary, name='monthly_summary'),
    path('yearly_summary/', views.monthly_summary, name='monthly_summary')
]
   