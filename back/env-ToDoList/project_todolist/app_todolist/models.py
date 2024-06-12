from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Manager pour le modèle Utilisateur personnalisé
class MyUserManager(BaseUserManager): # Définition d'un gestionnaire d'utilisateur personnalisé qui hérite de BaseUserManager.
    def create_user(self, email, password=None, **extra_fields): # Méthode pour créer un utilisateur
        if not email: # Vérifie si l'email est vide
            raise ValueError('The Email field must be set') #Lève une exception ValueError si l'email est vide
        email = self.normalize_email(email) # Normalise l'email (remplace les majuscules par des minuscules)
        user = self.model(email=email, **extra_fields) # Crée un utilisateur avec l'email et les champs supplémentaires
        user.set_password(password) # Hash le mot de passe de l'utilisateur 
        user.save(using=self._db) # Sauvegarde l'utilisateur dans la base de données
        return user

# Modèle Utilisateur personnalisé
class Utilisateur(AbstractBaseUser): # Définition d'un modèle Utilisateur personnalisé qui hérite de AbstractBaseUser.
    email = models.EmailField(unique=True) # Champ email unique
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    #adresse = models.TextField(blank=True, null=True)

    objects = MyUserManager() # Utilisation du gestionnaire d'utilisateur personnalisé

    USERNAME_FIELD = 'email' # Champ email utilisé pour l'authentification
    REQUIRED_FIELDS = ['nom', 'prenom'] # Champs requis pour la création d'un utilisateur

    def __str__(self):
        return self.email

# Modèle Todolist
class Todolist(models.Model):
    titre = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='todolists')

    def __str__(self):
        return self.titre

# Modèle Tache
class Tache(models.Model):
    titre = models.CharField(max_length=255)
    statut = models.CharField(max_length=50)
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE, related_name='taches')

    def __str__(self):
        return self.titre

# Modèle Suggestion
class Suggestion(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titre
