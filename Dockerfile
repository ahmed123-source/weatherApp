# Utilisez l'image de base Python 3.8
FROM python:3.8

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers de l'application dans le conteneur
COPY . /app
    
# Installez les dépendances depuis requirements.txt
RUN pip install -r requirements.txt

# Exposez le port sur lequel l'application fonctionnera
EXPOSE 5000

# Démarrez votre application Flask
CMD ["python", "app.py"]