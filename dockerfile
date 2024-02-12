# Utiliser l'image officielle Python 3.9 comme base
FROM python:3.9

# Mettre en place les variables d'environnement pour éviter les avertissements de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail dans le conteneur
RUN  mkdir /app
WORKDIR /app
# Copier le contenu de l'application dans le conteneur
COPY . /app/

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt /app/
COPY cmdbeas/.env /app/cmdbeas/
# Créer un environnement virtuel et installer les dépendances
RUN python -m venv /env
ENV PATH="/env/bin:$PATH"
COPY entrypoint.sh /app/entrypoint.sh
#RUN chmod +x /app/entrypoint.sh 


RUN /env/bin/python -m pip install --upgrade pip
RUN /env/bin/pip install --no-cache-dir -r requirements.txt



# Exécuter les migrations Django

