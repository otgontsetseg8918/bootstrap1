from django.urls import path, include
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up),
    path('account/', views.account)
]