from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_equipamento/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('cadastrar_item/', views.cadastrar_item, name='cadastrar_item'),
    path('cadastrar_troca/', views.cadastrar_troca, name='cadastrar_troca'),
    path('cadastrar_contador/', views.cadastrar_contador, name='cadastrar_contador'),
    path('success/<str:page>/', views.success_view, name='success'),
]
