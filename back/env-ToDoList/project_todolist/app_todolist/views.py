from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Utilisateur, Todolist, Tache, Suggestion
from .serializers import UtilisateurSerializer, TodolistSerializer, TacheSerializer, SuggestionSerializer

# Configuration Swagger pour le token d'authentification
token_param_config = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description="Token de l'utilisateur",
    type=openapi.TYPE_STRING
)

# Utilisateurs
@swagger_auto_schema(method='get', responses={200: UtilisateurSerializer(many=True)}, manual_parameters=[token_param_config])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: UtilisateurSerializer}, manual_parameters=[token_param_config])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    serializer = UtilisateurSerializer(utilisateur, many=False)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=UtilisateurSerializer, responses={201: UtilisateurSerializer, 400: 'Bad Request'})
@api_view(['POST'])
def create_utilisateur(request):
    serializer = UtilisateurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=UtilisateurSerializer, responses={200: UtilisateurSerializer, 400: 'Bad Request'}, manual_parameters=[token_param_config])
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    serializer = UtilisateurSerializer(utilisateur, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @swagger_auto_schema(method='delete', responses={204: 'No Content'}, manual_parameters=[token_param_config])
# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_utilisateur(request, pk):
#     utilisateur = get_object_or_404(Utilisateur, id=pk)
#     utilisateur.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

# Todolists
@swagger_auto_schema(method='get', responses={200: TodolistSerializer(many=True)}, manual_parameters=[token_param_config])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_todolists(request):
    todolists = Todolist.objects.filter(utilisateur=request.user)
    serializer = TodolistSerializer(todolists, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: TodolistSerializer}, manual_parameters=[token_param_config])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_todolist(request, pk):
    todolist = get_object_or_404(Todolist, id=pk, utilisateur=request.user)
    serializer = TodolistSerializer(todolist, many=False)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=TodolistSerializer, responses={201: TodolistSerializer, 400: 'Bad Request'}, manual_parameters=[token_param_config])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_todolist(request):
    data = request.data.copy()
    data['utilisateur'] = request.user.id
    serializer = TodolistSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @swagger_auto_schema(method='put', request_body=TodolistSerializer, responses={200: TodolistSerializer, 400: 'Bad Request'}, manual_parameters=[token_param_config])
# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update_todolist(request, pk):
#     todolist = get_object_or_404(Todolist, id=pk, utilisateur=request.user)
#     serializer = TodolistSerializer(todolist, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, manual_parameters=[token_param_config])
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_todolist(request, pk):
    todolist = get_object_or_404(Todolist, id=pk, utilisateur=request.user)
    todolist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Taches
@swagger_auto_schema(method='get', responses={200: TacheSerializer(many=True)}, manual_parameters=[token_param_config])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_taches(request):
    taches = Tache.objects.filter(todolist__utilisateur=request.user)
    serializer = TacheSerializer(taches, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: TacheSerializer}, manual_parameters=[token_param_config])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tache(request, pk):
    tache = get_object_or_404(Tache, id=pk, todolist__utilisateur=request.user)
    serializer = TacheSerializer(tache, many=False)
    return Response(serializer.data)

@swagger_auto_schema(method='get', responses={200: TacheSerializer(many=True)}, manual_parameters=[token_param_config])
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_taches_par_statut(request, todolist_id, statut):
    taches = Tache.objects.filter(todolist__id=todolist_id, statut=statut, todolist__utilisateur=request.user)
    serializer = TacheSerializer(taches, many=True)
    return Response(serializer.data)

@swagger_auto_schema(method='post', request_body=TacheSerializer, responses={201: TacheSerializer, 400: 'Bad Request'}, manual_parameters=[token_param_config])
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_tache(request):
    serializer = TacheSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=TacheSerializer, responses={200: TacheSerializer, 400: 'Bad Request'}, manual_parameters=[token_param_config])
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_tache(request, pk):
    tache = get_object_or_404(Tache, id=pk, todolist__utilisateur=request.user)
    serializer = TacheSerializer(tache, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, manual_parameters=[token_param_config])
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_tache(request, pk):
    tache = get_object_or_404(Tache, id=pk, todolist__utilisateur=request.user)
    tache.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Suggestions
@swagger_auto_schema(method='get', responses={200: SuggestionSerializer(many=True)})
@api_view(['GET'])
def get_suggestions(request):
    suggestions = Suggestion.objects.all()
    serializer = SuggestionSerializer(suggestions, many=True)
    return Response(serializer.data)

# @swagger_auto_schema(method='get', responses={200: SuggestionSerializer})
# @api_view(['GET'])
# def get_suggestion(request, pk):
#     suggestion = get_object_or_404(Suggestion, id=pk)
#     serializer = SuggestionSerializer(suggestion, many=False)
#     return Response(serializer.data)

# @swagger_auto_schema(method='post', request_body=SuggestionSerializer, responses={201: SuggestionSerializer, 400: 'Bad Request'})
# @api_view(['POST'])
# def create_suggestion(request):
#     serializer = SuggestionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @swagger_auto_schema(method='put', request_body=SuggestionSerializer, responses={200: SuggestionSerializer, 400: 'Bad Request'})
# @api_view(['PUT'])
# def update_suggestion(request, pk):
#     suggestion = get_object_or_404(Suggestion, id=pk)
#     serializer = SuggestionSerializer(suggestion, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @swagger_auto_schema(method='delete', responses={204: 'No Content'})
# @api_view(['DELETE'])
# def delete_suggestion(request, pk):
#     suggestion = get_object_or_404(Suggestion, id=pk)
#     suggestion.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)