import sys
import os
import django
import requests
from bs4 import BeautifulSoup
from app_todolist.models import Suggestion

# Récupère le chemin du répertoire du fichier scrapper.py
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Ajoute le chemin vers le répertoire parent du projet Django
sys.path.append(BASE_DIR)

# Définit le module de configuration Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_todolist.settings")

# Initialise Django
django.setup()

url = 'https://todoist.com/fr/inspiration/category/goals'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titres = soup.find_all('h2', class_='Z2j5FoeQ_umI7vX0SmxF') 
descriptions = soup.find_all('p', class_='Z2j5FoeQ_umI7vX0SmxF')

for titre, description in zip(titres, descriptions):
    Suggestion.objects.create(
        titre=titre.text.strip(),
        description=description.text.strip()
)
