# HOW TO DEPLOY DJANGO APPLICATION ON APACHE 2

# verifier que mod_wgsi est installé dans les module de apache 
apache2ctl -M
# installé mod_wgsi 
apt-get install libapache2-mod-wsgi-py3
# installé mod_wsgi
https://pypi.org/project/mod-wsgi/

# redémarrage du serveur Apache pour prendre en compte la nouvelle configuration
systemctl  restart apache2


# on clone le projet django depuis github
git clone https://github.com/menoutep/cmdbeas.git

# creation of a virtual environment for our project
python3 -m venv cmdbeasenv
source cmdbeasenv/bin/activate

# installation des dépendances avec pip et activation de l'environnement virtuel
pip install -r requirements.txt


# ajout des droits de lecture a l'utilisateur apache : www-data
sudo touch /etc/apache2/sites-available/cmdbeas.conf
# creation du fichier wsgi.py pour qu'il pointe vers notre application
sudo touch /etc/apache2/sites-available/cmdbeas.conf
# modification du fichier wsgi.py pour qu'il pointe vers notre application
sudo nano /etc/apache2/sites-available/cmdbeas.conf

<VirtualHost *:80>
    ServerName cmbdeas.example.com

    Alias /var/www/cmdbeas/staticfiles
    <Directory /var/www/cmdbeas/staticfiles>
        Require all granted
    </Directory>

    <Directory/var/www/cmdbeas/cmdbeas>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess cmdbeas python-home=var/www/cmdbeas cmdbeasenv python-path=/var/www/cmdbeas/cmdbeasenv/lib/python3.9:/var/www/cmdbeas/cmdbeasenv/bin/python3.9
    WSGIProcessGroup cmdbeas
    WSGIScriptAlias / /var/www/cmdbeas/cmdbeas/wsgi.py
</VirtualHost>



# ajout du site au serveur d'apache
sudo ln -s /etc/apache2/sites-available/cmdbeas.conf /
sudo a2ensite cmdbeas.conf
sudo a2dissite 000-default.conf

# redémarrage du service apache pour que les changements soient pris en compte
sudo systemctl restart apache2



