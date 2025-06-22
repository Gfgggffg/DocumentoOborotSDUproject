from django.urls import path
from . import views

urlpatterns = [
    path('', views.glavnaya, name='glavnaya'),
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('documents/', views.document_processing, name='document_processing'),
    path('download-template/', views.download_excel_template, name='download_template'),
]