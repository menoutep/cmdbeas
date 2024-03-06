@echo off
set "cheminEnv=C:\Users\zabreg\django\djangoapp\cmdbeas\env"

rem Vérifier si le dossier existe
if exist "%cheminEnv%" (
    rem Lancer l'environnement virtuel
    call "%cheminEnv%\Scripts\activate.bat"
    echo Environnement virtuel Python lancé.
    
    rem Exécuter la commande Django
    python manage.py runcrons
) else (
    echo Le dossier de l'environnement virtuel n'existe pas.
)
