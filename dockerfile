FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils apache2-dev 
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN apt-get install w3m -y
RUN pip install --upgrade pip
RUN pip install django ptvsd
ENV PYTHONUNBUFFERED 1
RUN mkdir /cmdbeas/
WORKDIR /cmdbeas/

COPY . /cmdbeas/
RUN apt-get install -y python3-venv
RUN python3 -m venv /env
ENV PATH="/env/bin:$PATH"

RUN /env/bin/python3 -m pip install --upgrade pip
RUN /env/bin/pip install --no-cache-dir -r requirements.txt
RUN /env/bin/pip install  pip install mod-wsgi
COPY ./apache/cmdbeas.conf /etc/apache2/sites-available/


RUN chmod 664 /cmdbeas/db.sqlite3
RUN chmod 775 /cmdbeas/cmdbeas
RUN chmod 777 /cmdbeas
RUN chown :www-data /cmdbeas/db.sqlite3
RUN chown :www-data /cmdbeas/cmdbeas
RUN a2dissite 000-default.conf
#RUN echo "LoadModule wsgi_module '/usr/lib/apache2/modules/mod_wsgi.so'" >> /etc/apache2/mods-enabled/wsgi.load
RUN echo 'LoadModule wsgi_module "/env/lib/python3.10/site-packages/mod_wsgi/server/mod_wsgi-py310.cpython-310-x86_64-linux-gnu.so"' > /etc/apache2/mods-available/wsgi.load
RUN echo 'WSGIPythonHome "/usr"' >> /etc/apache2/mods-available/wsgi.load

RUN a2ensite cmdbeas.conf
RUN a2enmod proxy
RUN echo $USER
RUN a2enmod wsgi
RUN a2enmod proxy_http
RUN a2enmod proxy_balancer
RUN a2enmod lbmethod_byrequests
EXPOSE 80 3500
#RUN source /env/bin/activate 
RUN python3 manage.py makemigrations && python manage.py migrate

# Commande pour créer un superutilisateur Django
# Créer un superutilisateur Django avec un mot de passe spécifié

# Lancement d'Apache après la création du superutilisateur
#ENTRYPOINT ["/bin/bash", "-c", "apache2ctl -D FOREGROUND"]
ENTRYPOINT ["/bin/bash"]



