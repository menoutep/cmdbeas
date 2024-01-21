from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
import re
from django_select2 import forms as s2forms
from django.contrib.auth.hashers import check_password
from crispy_forms.helper import FormHelper
from .models import User
from base.models import Departement
from django.contrib.auth.models import Permission,Group
from django import forms
from crispy_forms.layout import Layout, Field, Submit, Submit, ButtonHolder,Fieldset,Div,Column

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        min_length=4,
        label="username",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez votre username'}),
        
        )
    first_name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom ",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de l\'utilisateur'}),
        
        )
    last_name = forms.CharField(
        max_length=255,
        min_length=4,
        label="Prenoms",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le prenom de l\'utilisateur'}),
        
        )
    email = forms.EmailField(
        label="email",
        help_text="adresse mail active",
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Entrez votre nom email'}),
        
        )
    contact = forms.CharField(
        max_length=13,
        label="télephone",
        help_text="format : +2250667897876",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez votre numéro de telephone'}),
       
        )
    departement = forms.ModelChoiceField(
        queryset=Departement.objects.all(),
        label='Département',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Entrez votre departement'}),
    )
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'Selectionnez les permissions'}), 
        label='Permissions',
        required=False
        
        )
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'Selectionnez les groupes'}), 
        label='Groupes',
        required=False
        )
    is_staff = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name','last_name','contact','departement','email','user_permissions','is_staff','groups') 
        
    
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        # Exclure les champs password1 et password2
        self.fields.pop('password1')
        self.fields.pop('password2')

        
        

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@mtn.com'):
            raise forms.ValidationError('L\'adresse email doit se terminer par "@mtn.com".')
        return email

    
 
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Ancien mot de passe",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'class':'form-control','placeholder': 'ancien mot de passe ',"autocomplete": "current-password", "autofocus": True}
        ),
    )
    new_password1 = forms.CharField(
        label="Nouveau mot de passe",
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'nouveau mot de passe',"autocomplete": "new-password"}),
        strip=False,
        
    )
    new_password2 = forms.CharField(
        label="Confirmer le mot passe",
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'confirmer le mot de passe',"autocomplete": "new-password"}),
    )


    
    def clean_new_password1(self):
        new_password1 = self.cleaned_data.get("new_password1")
        history = self.user.history.all().order_by('-history_date')[:24]

        if not isinstance(new_password1, str):
            raise forms.ValidationError("Password should be a string.")
        
        if self.user.is_staff == True and len(new_password1) < 14:
            raise forms.ValidationError("Password should have at least 14 characters.")
        if self.user.is_staff == False and len(new_password1) < 12:
            raise forms.ValidationError("Password should have at least 12 characters.")
        if not re.search("[a-z]", new_password1):
            raise forms.ValidationError("Password should have at least one lower-case letter.")
        
        if not re.search("[A-Z]", new_password1):
            raise forms.ValidationError("Password should have at least one upper-case letter.")
        
        if not re.search("[0-9]", new_password1):
            raise forms.ValidationError("Password should have at least one number.")
        
        if not re.search("[_!@#$%^&*()<>?/|}{~:]", new_password1):
            raise forms.ValidationError("Password should have at least one special character.")

        for h in history:
            res = check_password(new_password1, h.password)
            if res:         
                raise forms.ValidationError("le mot de passe a déja été utilisé lors des 24 dernière réinitialisation.")
        return new_password1
    

class PermissionWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains",
        "codename__icontains",
    ]


class GroupWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains",
        
    ]


class UserWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "username__icontains",
        "email__icontains",
    ]

class PermissionForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        label='Utilisateur',
        widget=UserWidget(attrs={'class': 'form-control','placeholder':'Selectionner un utilisateur'}),
        )
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(), 
        widget=PermissionWidget(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'Selectionnez les permissions'}), 
        label='Permissions'
        )

class AdminResetUserPassword(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        label='Utilisateur',
        widget=UserWidget(attrs={'class': 'form-control','placeholder':'mail ou username'}),
        )
    



class GroupCreationForm(forms.Form):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du groupe'}),
        
    )
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=PermissionWidget(attrs={'class': 'form-control', 'id': 'permissionsSelect', 'style': 'height: 100px;'}),
        label='Permissions'
    )

class GroupAddForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        label='Utilisateur',
        widget=UserWidget(attrs={'class': 'form-control','placeholder':'Selectionner un utilisateur'}),
        )
    group = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(), 
        widget=GroupWidget(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'Selectionnez les roles'}), 
        label='Roles'
        )



class CustomUserLoginForm(forms.Form):
    
    email = forms.CharField(
        max_length=150,
        label="email",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@mtn.com'):
            raise forms.ValidationError('L\'adresse email doit se terminer par "@mtn.com".')
        return email
   