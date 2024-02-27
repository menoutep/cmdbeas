FROM alpine:3.19.1

# Mise à jour des paquets et installation des outils nécessaires

RUN apk update
RUN apk add --no-cache apache2 
RUN apk add --no-cache apache2-utils 
RUN apk add --no-cache apache2-dev 
RUN apk add --no-cache curl 
RUN apk add --no-cache python3 
RUN apk add --no-cache py3-pip 
RUN apk add --no-cache py3-virtualenv 
RUN apk add --no-cache vim 
RUN apk add --no-cache w3m 
RUN apk add --no-cache gcc 
RUN apk add --no-cache musl-dev 
RUN apk add --no-cache python3-dev 
RUN apk add --no-cache py3-pip
RUN rm -rf /var/cache/apk/*

RUN python3 -m venv /env

# Définition de la variable PATH pour inclure l'environnement virtuel
ENV PATH="/env/bin:$PATH"

# Installation de Django et ptvsd
RUN pip install django ptvsd mod-wsgi

# Configuration de l'environnement Python
ENV PYTHONUNBUFFERED 1

# Création du répertoire de travail
RUN mkdir /cmdbeas
WORKDIR /cmdbeas

# Copie du code de l'application dans le conteneur
COPY . /cmdbeas/
COPY /cmdbeas /var/www/localhost/htdocs/ 
RUN echo 'LoadModule wsgi_module "/env/lib/python3.11/site-packages/mod_wsgi/server/mod_wsgi-py311.cpython-311-x86_64-linux-musl.so" ' >> /etc/apache2/httpd.conf

# Direct *.wsgi scripts to mod_wsgi
RUN echo -e "\n\n\
LoadModule wsgi_module '/env/lib/python3.11/site-packages/mod_wsgi/server/mod_wsgi-py311.cpython-311-x86_64-linux-musl.so'\n\
WSGIPythonPath /usr/lib/python3.11\n\
<VirtualHost *:80>\n\
ServerName cmdbeas.com\n\
DocumentRoot /cmdbeas\n\
<Directory /cmdbeas/staticfiles>\n\
    Require all granted\n\
</Directory>\n\
<Directory /cmdbeas>\n\
    <Files wsgi.py>\n\
        Require all granted\n\
    </Files>\n\
</Directory>\n\
<Directory /cmdbeas>\n\
    Options Indexes FollowSymLinks MultiViews\n\
    AllowOverride All\n\
    Require all granted\n\
</Directory>\n\
WSGIDaemonProcess cmdbeas python-home=/env python-path=/cmdbeas:/env/lib/python3.11/site-packages\n\
WSGIProcessGroup cmdbeas\n\
WSGIScriptAlias / /cmdbeas/cmdbeas/wsgi.py\n\
WSGIApplicationGroup %{GLOBAL}\n\
ErrorLog /cmdbeas/django.log\n\
CustomLog /cmdbeas/accounts.log combined\n\
</VirtualHost>" >> /etc/apache2/httpd.conf
EXPOSE 80 3500
ENTRYPOINT ["/bin/ash"]
# Création de l'environnement virtuel

