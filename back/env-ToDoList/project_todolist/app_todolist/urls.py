from django.urls import path
from .views import (
    get_utilisateurs, get_utilisateur, create_utilisateur, update_utilisateur,
    get_todolists, get_todolist, create_todolist, delete_todolist,
    get_taches, get_tache, create_tache, update_tache, delete_tache, get_taches_par_statut,
    get_suggestions
)

urlpatterns = [
    path('utilisateurs/', get_utilisateurs, name='get_utilisateurs'),
    path('utilisateurs/<int:pk>/', get_utilisateur, name='get_utilisateur'),
    path('utilisateurs/create/', create_utilisateur, name='create_utilisateur'),
    path('utilisateurs/<int:pk>/update/', update_utilisateur, name='update_utilisateur'),
    #path('utilisateurs/<int:pk>/delete/', delete_utilisateur, name='delete_utilisateur'),

    path('todolists/', get_todolists, name='get_todolists'),
    path('todolists/<int:pk>/', get_todolist, name='get_todolist'),
    path('todolists/create/', create_todolist, name='create_todolist'),
    #path('todolists/<int:pk>/update/', update_todolist, name='update_todolist'),
    path('todolists/<int:pk>/delete/', delete_todolist, name='delete_todolist'),

    path('taches/', get_taches, name='get_taches'),
    path('taches/<int:pk>/', get_tache, name='get_tache'),
    path('taches/create/', create_tache, name='create_tache'),
    path('taches/<int:pk>/update/', update_tache, name='update_tache'),
    path('taches/<int:pk>/delete/', delete_tache, name='delete_tache'),
    path('todolists/<int:todolist_id>/taches/<str:statut>/', get_taches_par_statut, name='get_taches_par_statut'),

    path('suggestions/', get_suggestions, name='get_suggestions'),
    #path('suggestions/<int:pk>/', get_suggestion, name='get_suggestion'),
    #path('suggestions/create/', create_suggestion, name='create_suggestion'),
    #path('suggestions/<int:pk>/update/', update_suggestion, name='update_suggestion'),
    #path('suggestions/<int:pk>/delete/', delete_suggestion, name='delete_suggestion'),
]
