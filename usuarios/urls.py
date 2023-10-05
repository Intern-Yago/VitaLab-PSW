from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"), # type: ignore
    path('login/', views.logar, name="login") # type: ignore
]