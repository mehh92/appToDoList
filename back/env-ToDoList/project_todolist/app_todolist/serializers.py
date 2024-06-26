from rest_framework import serializers
from .models import Utilisateur, Todolist, Tache, Suggestion

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'email', 'nom', 'prenom', 'password']

    def create(self, validated_data):
        return Utilisateur.objects.create_user(**validated_data)

class TodolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ['id', 'titre', 'date_creation', 'description', 'utilisateur']

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = ['id', 'titre', 'statut', 'todolist']

class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ['id', 'titre', 'description']
