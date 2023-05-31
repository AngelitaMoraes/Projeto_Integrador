from django.urls import path
from . import views

urlpatterns = [
    path('projetofinancas/', views.projetofinancas, name="projetofinancas.html")

]