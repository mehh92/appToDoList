from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .models import Utilisateur, Todolist, Tache, Suggestion
from .serializers import UtilisateurSerializer, TodolistSerializer, TacheSerializer, SuggestionSerializer

# Utilisateurs
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    serializer = UtilisateurSerializer(utilisateur, many=False)
    return Response(serializer.data)



@api_view(['GET'])
def get_utilisateurs(request):
    utilisateurs = Utilisateur.objects.all()
    serializer = UtilisateurSerializer(utilisateurs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    serializer = UtilisateurSerializer(utilisateur, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_utilisateur(request):
    serializer = UtilisateurSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    serializer = UtilisateurSerializer(utilisateur, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, id=pk)
    utilisateur.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Todolists
@api_view(['GET'])
def get_todolists(request):
    todolists = Todolist.objects.filter(utilisateur=request.user)
    serializer = TodolistSerializer(todolists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_todolist(request, pk):
    todolist = get_object_or_404(Todolist, id=pk)
    serializer = TodolistSerializer(todolist, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_todolist(request):
    data = request.data.copy()
    data['utilisateur'] = request.user.id
    serializer = TodolistSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_todolist(request, pk):
    todolist = get_object_or_404(Todolist, id=pk)
    serializer = TodolistSerializer(todolist, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_todolist(request, pk):
    todolist = get_object_or_404(Todolist, id=pk)
    todolist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Taches
@api_view(['GET'])
def get_taches(request):
    taches = Tache.objects.filter(todolist__utilisateur=request.user)
    serializer = TacheSerializer(taches, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_tache(request, pk):
    tache = get_object_or_404(Tache, id=pk)
    serializer = TacheSerializer(tache, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_tache(request):
    serializer = TacheSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_tache(request, pk):
    tache = get_object_or_404(Tache, id=pk)
    serializer = TacheSerializer(tache, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_tache(request, pk):
    tache = get_object_or_404(Tache, id=pk)
    tache.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Suggestions
@api_view(['GET'])
def get_suggestions(request):
    suggestions = Suggestion.objects.all()
    serializer = SuggestionSerializer(suggestions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_suggestion(request, pk):
    suggestion = get_object_or_404(Suggestion, id=pk)
    serializer = SuggestionSerializer(suggestion, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_suggestion(request):
    serializer = SuggestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_suggestion(request, pk):
    suggestion = get_object_or_404(Suggestion, id=pk)
    serializer = SuggestionSerializer(suggestion, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_suggestion(request, pk):
    suggestion = get_object_or_404(Suggestion, id=pk)
    suggestion.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

