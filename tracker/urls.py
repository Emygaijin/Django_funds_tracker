from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('institutions/', views.institution, name='schools'),
    path('details/<str:name>',views.details, name='details'),
    path('client_institutions/', views.client_institution, name='clients'),
    path('update/<str:name>',views.update, name='update'),
    path('choice/', views.choice, name='choice'),
    path('statistics/<str:institution_name>/total/', views.institution_total, name='institution_total'),
    path('income_total/', views.income_total, name='income_total'),
]