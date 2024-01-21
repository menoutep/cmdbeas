# validators.py
# validators.py
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import mimetypes
import PyPDF2
import magic
# python-magic permet de verifier le mime réel du fichier, sur windows il y a des probleme de compatibillité pour ce package a cause de libmagic.
#mimetypes est un peu moins sur que python-magic car il verifie le mime declaré et non le mime réel . 
#python-magic ne marche que sur linux.




def validate_pdf_magic(value):
    # Valider l'extension du fichier à l'aide de FileExtensionValidator
    validateur_extension = FileExtensionValidator(allowed_extensions=['pdf'])
    try:
        validateur_extension(value)
    except ValidationError as e:
        raise ValidationError("Extension de fichier non autorisée. Seuls les fichiers PDF sont autorisés.") from e

    # Valider le type MIME réel du fichier à l'aide de python-magic
    mime = magic.Magic()
    type_mimetype = mime.from_buffer(value.read(1024))

    if not type_mimetype.startswith('application/pdf'):
        raise ValidationError("Type de fichier non autorisé. Seuls les fichiers PDF sont autorisés.")
    
    # Vérifier le contenu spécifique d'un fichier PDF
    value.seek(0)  # Revenir au début du fichier
    magic_header = value.read(4)  # Lire les 4 premiers octets

    if magic_header != b'%PDF':
        raise ValidationError("Le contenu du fichier ne correspond pas à un fichier PDF.")
    
    try:
        pdf_reader = PyPDF2.PdfReader(value)
        # = pdf_reader.metadata
        #print(meta.author)
        num_pages = len(pdf_reader.pages)
        if num_pages == 0:
            raise ValidationError("Le fichier PDF est vide.")
    except :
        raise ValidationError("Le fichier PDF est corrompu ou invalide.")
    