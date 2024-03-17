# forms.py
from django import forms
from .models import ConnexionBD,AppServer,AppelApi,Api,ModuleApplicatif,Departement,AppType,Process,UseCase,CallFlow,SubProcess,Api,Datacenter,ServerRoom,Rack,Cluster,SystemeStockage,Server,Partition,DeploiementCluster,Database,DatabaseServer,DataDictionnary,DataDictionnaryModel,DataModel,DesktopApp,DomainName,ArchitectureDiagram, UssdShortCode,Vendor,Application,BackupStrategie,NetworkInterface,Notifications,IpAdress
from base.models import PRIORITY_CHOICES,NAME_APP_TYPE_CHOICES
from .validators import validate_pdf_magic
from .models import AppDeployment, BackupStrategie,TechnicalRecoveryPlan,ApiSpecification,ApiDocumentation,Url,SmsShortCode,SmppAccount,MobileApp,DesktopApp,ConnexionApp


NAME_SERVER_TYPE_CHOICES = (
    ('virtuel','virtuel'),
    ('physique','physique'),
)
############# START APPLICATION MODULE FORMS ###############################
class DepartementForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du departement",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du departement'}),      
        )
    description = forms.CharField(
        label="Description du departement",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )

    class Meta:
        model = Departement
        fields = ['name', 'description']
        

class DepartementUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du departement",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du departement'}),      
        )
    description = forms.CharField(
        label="Description du departement",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Departement
        fields = ['name', 'description']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance



class VendorForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du vendor",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du vendor'}),      
        )
    description = forms.CharField(
        label="Description du vendor",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )

    class Meta:
        model = Vendor
        fields = ['name', 'description']
        

class VendorUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du vendor",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du vendor'}),      
        )
    description = forms.CharField(
        label="Description du vendor",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Vendor
        fields = ['name', 'description']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance

class AppTypeForm(forms.ModelForm):
    name = forms.ChoiceField(
        label="Nom du type",
        choices=NAME_APP_TYPE_CHOICES,  
        widget=forms.Select(attrs={'class': 'form-control','placeholder': 'priorité  application'}),
    )
    description = forms.CharField(
        label="Description",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )

    class Meta:
        model = AppType
        fields = ['name', 'description']
        

class AppTypeUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du type",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du apptype'}),      
        )
    description = forms.CharField(
        label="Description du type",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = AppType
        fields = ['name', 'description']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance



class ApplicationForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de l'application",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Entrez le nom de l'application "}),      
        )
    description = forms.CharField(
        label="Description de l'application",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )
    replication = forms.IntegerField(
        label="nombre de replication",
              
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'nombre de replication application'})
        )
    priority = forms.ChoiceField(
        label="Priorité",
        choices=PRIORITY_CHOICES,  
        widget=forms.Select(attrs={'class': 'form-control','placeholder': 'priorité  application'}),
    )
    control_name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de code de l'application",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Entrez le nom de code de l'application "}),      
        )
    deployement_year = forms.DateTimeField(
        label = "date de deploiement",
        widget=forms.DateTimeInput(attrs={'class':'form-control','type': 'datetime-local','placeholder':'Entrez la date de deployement '}),
        initial = "1960-01-01",
        help_text = "Vous devez avoir au moins 18 ans",
    )
    app_type = forms.ModelChoiceField(
        queryset=AppType.objects.all(),
        label='type application',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un type application'}),
    )
    backup_strategie = forms.ModelChoiceField(
        queryset=BackupStrategie.objects.all(),
        label='strategie backup',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une strategie backup'}),
    )

    class Meta:
        model = Application
        fields = ['name', 'description','replication','control_name','deployement_year','app_type','backup_strategie']
        

class ApplicationUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de l'application",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Entrez le nom de l'application "}),      
        )
    description = forms.CharField(
        label="Description de l'application",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )
    replication = forms.IntegerField(
        label="nombre de replication",
              
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'nombre de replication application'})
        )
    priority = forms.ChoiceField(
        label="Priorité",
        choices=PRIORITY_CHOICES,  
        widget=forms.Select(attrs={'class': 'form-control','placeholder': 'priorité  application'}),
    )
    control_name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de code de l'application",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Entrez le nom de code de l'application "}),      
        )
    deployement_year = forms.DateTimeField(
        label = "date de deploiement",
        widget=forms.DateTimeInput(attrs={'class':'form-control','type': 'datetime-local','placeholder':'Entrez la date de deployement '}),
        initial = "1960-01-01",
        help_text = "Vous devez avoir au moins 18 ans",
    )
    app_type = forms.ModelChoiceField(
        queryset=AppType.objects.all(),
        label='type application',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un type application'}),
    )
    backup_strategie = forms.ModelChoiceField(
        queryset=BackupStrategie.objects.all(),
        label='strategie backup',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une strategie backup'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )

    class Meta:
        model = Application
        fields = ['name', 'description','replication','control_name','deployement_year','app_type','backup_strategie','priority']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
    

class ModuleApplicatifForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de l'application",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Entrez le nom de l'application "}),      
        )
    description = forms.CharField(
        label="Description de l'application",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )
    
   
    application = forms.ModelChoiceField(
        queryset=Application.objects.all(),
        label='application',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une application'}),
    )
    vendor = forms.ModelChoiceField(
        queryset=Vendor.objects.all(),
        label='vendor',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une strategie backup'}),
    )
    departement = forms.ModelChoiceField(
        queryset=Departement.objects.all(),
        label='Departement',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une strategie backup'}),
    )

    class Meta:
        model = ModuleApplicatif
        fields = ['name', 'description','application','vendor','departement']
        

class ModuleApplicatifUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de l'application",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control',"placeholder":"Entrez le nom de l'application "}),      
        )
    description = forms.CharField(
        label="Description de l'application",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description','id':'message', 'style': 'height: 100px;'})
        )
    
   
    application = forms.ModelChoiceField(
        queryset=Application.objects.all(),
        label='application',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une application'}),
    )
    vendor = forms.ModelChoiceField(
        queryset=Vendor.objects.all(),
        label='vendor',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une strategie backup'}),
    )
    departement = forms.ModelChoiceField(
        queryset=Departement.objects.all(),
        label='Departement',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une strategie backup'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )

    class Meta:
        model = ModuleApplicatif
        fields = ['name', 'description','application','vendor','departement']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
   

class ConnexionBDForm(forms.ModelForm):
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='Module Applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un module applicatif'}),
    )
    database = forms.ModelChoiceField(
        queryset=Database.objects.all(),
        label='Database',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une base de donnée'}),
    )

    class Meta:
        model = ConnexionBD
        fields = ['module_applicatif', 'database']
        

class ConnexionBDUpdateForm(forms.ModelForm):
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='Module Applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un module applicatif'}),
    )
    database = forms.ModelChoiceField(
        queryset=Database.objects.all(),
        label='Database',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une base de donnée'}),
    )

    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = ConnexionBD
        fields = ['module_applicatif', 'database']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


############# END APPLICATION MODULE FORMS ###############################
class ProcessForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description du process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Entrez le lieu du process'}),      
        )

    class Meta:
        model = Process
        fields = ['name', 'description']       
class ProcessUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description du process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Entrez la description du process'}),      
        )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Process
        fields = ['name', 'description']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance

class SubProcessForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description du process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Entrez le lieu du process'}),      
        )
    process = forms.ModelChoiceField(
        queryset=Process.objects.all(),
        label='Process',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )

    class Meta:
        model = SubProcess
        fields = ['name', 'description','process']    
class SubProcessUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description du process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Entrez la description du process'}),      
        )
    process = forms.ModelChoiceField(
        queryset=Process.objects.all(),
        label='Process',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = SubProcess
        fields = ['name', 'description','process']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class UseCaseForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du sous process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description du sous process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le lieu du process'}),      
        )
    sub_process = forms.ModelChoiceField(
        queryset=SubProcess.objects.all(),
        label='Sous Process',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )

    class Meta:
        model = UseCase
        fields = ['name', 'description','sub_process']    
class UseCaseUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du  sous process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description du sous process",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez la description du process'}),      
        )
    sub_process = forms.ModelChoiceField(
        queryset=SubProcess.objects.all(),
        label='Sous Process',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = UseCase
        fields = ['name', 'description','sub_process']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance

class ApiForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de l'api",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description de l'api",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le lieu du process'}),      
        )
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )

    class Meta:
        model = Api
        fields = ['name', 'description','module_applicatif']    
class ApiUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de l'api",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description de l'api",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez la description du process'}),      
        )
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Api
        fields = ['name', 'description','module_applicatif']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class AppelApiForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de l'api",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description de l'api",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Entrez le lieu du process'}),      
        )
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )
    api = forms.ModelChoiceField(
        queryset=Api.objects.all(),
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )
    use_case = forms.ModelChoiceField(
        queryset=UseCase.objects.all(),
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )

    class Meta:
        model = AppelApi
        fields = ['name', 'description','module_applicatif','api','use_case']    
class AppelApiUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom de l'api",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du process'}),      
        )
    description = forms.CharField(
        max_length=150,
        min_length=4,
        label="description de l'api",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Entrez le lieu du process'}),      
        )
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )
    api = forms.ModelChoiceField(
        queryset=Api.objects.all(),
        label='api',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )
    use_case = forms.ModelChoiceField(
        queryset=UseCase.objects.all(),
        label='use case',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )


    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    
    class Meta:
        model = AppelApi
        fields = ['name', 'description','module_applicatif','api','use_case']    

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


############# START SYSTEME MODULE VIEWS ###############################

class DatacenterForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du datacenter",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du datacenter'}),      
        )
    localisation = forms.CharField(
        max_length=150,
        min_length=4,
        label="lieu du datacenter",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le lieu du datacenter'}),      
        )

    class Meta:
        model = Datacenter
        fields = ['name', 'localisation']
        

class DatacenterUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du datacenter",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du datacenter'}),      
        )
    localisation = forms.CharField(
        max_length=150,
        min_length=4,
        label="lieu du datacenter",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le lieu du datacenter'}),      
        )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Datacenter
        fields = ['name', 'localisation']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
    



class ServerRoomForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="salle serveur",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la salle serveur '}),      
        )
    datacenter = forms.ModelChoiceField(
        queryset=Datacenter.objects.all(),
        label='Datacenter',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un datacenter'}),
    )

    class Meta:
        model = ServerRoom
        fields = ['name', 'datacenter']
        

class ServerRoomUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="salle serveur",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la salle serveur '}),      
        )
    datacenter = forms.ModelChoiceField(
        queryset=Datacenter.objects.all(),
        label='Datacenter',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un datacenter'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = ServerRoom
        fields = ['name', 'datacenter']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
    

class RackForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du rack",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du rack '}),      
        )
    server_room = forms.ModelChoiceField(
        queryset=ServerRoom.objects.all(),
        label='Salle serveur',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner la salle serveur'}),
    )

    class Meta:
        model = Rack
        fields = ['name', 'server_room']
        

class RackUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du rack",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du rack '}),      
        )
    server_room = forms.ModelChoiceField(
        queryset=ServerRoom.objects.all(),
        label='ServerRoom',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner la salle serveur'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Rack
        fields = ['name', 'server_room']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
    


 
class SystemeStockageForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du systeme de stockage",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du systeme de stockage'}),      
        )
    ram = forms.IntegerField(
        label="memoire ram",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire ram en gb'})
        )
    rom = forms.IntegerField(
        label="memoire rom",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire rom en tera'})
        )

    class Meta:
        model = SystemeStockage
        fields = ['name', 'ram','rom']
        

class SystemeStockageUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du systeme de stockage",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du systeme'}),      
        )
    ram = forms.IntegerField(
        label="memoire ram",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire ram en gb'})
        )
    rom = forms.IntegerField(
        label="memoire rom",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire rom en tera'})
        )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = SystemeStockage
        fields = ['name', 'ram','rom']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance

class NetworkInterfaceForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="nom de l'interface",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la salle serveur '}),      
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description interface réseau','id':'message', 'style': 'height: 100px;'})
        )

    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Server',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un server'}),
    )

    class Meta:
        model = NetworkInterface
        fields = ['name', 'description','server']
        

class AppServerForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du app_server",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du app_server'}),      
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description interface réseau','id':'message', 'style': 'height: 100px;'})
        )
    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Serveur',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un serveur'}),
    )
    module_applicatif = forms.ModelMultipleChoiceField(
        queryset= ModuleApplicatif.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'ajoutez un ou plusieurs module applicatifs'}), 
        label='module applicatif',
    )
    class Meta:
        model = AppServer
        fields = ['name','description','server','module_applicatif']
        

class AppServerUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du app_server",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du app_server'}),      
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description interface réseau','id':'message', 'style': 'height: 100px;'})
        )
    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Serveur',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un serveur'}),
    )
    module_applicatif = forms.ModelMultipleChoiceField(
        queryset= ModuleApplicatif.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'ajoutez un ou plusieurs module applicatifs'}), 
        label='module applicatif',
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = AppServer
        fields = ['name','description','server','module_applicatif']


    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
            instance.module_applicatif.set(self.cleaned_data['module_applicatif'])
        if commit:
            instance.save()
        return instance
  


class NetworkInterfaceUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="nom de l'interface",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la salle serveur '}),      
        )
    
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description interface réseau','id':'message', 'style': 'height: 100px;'})
        )

    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Server',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un server'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = NetworkInterface
        fields = fields = ['name', 'description','server']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class IpAdressForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la salle serveur '}),      
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description interface réseau','id':'message', 'style': 'height: 100px;'})
        )

    interface = forms.ModelChoiceField(
        queryset=NetworkInterface.objects.all(),
        label='Interface Réseau',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une interface réseau'})
    )
    ipv4 = forms.GenericIPAddressField(
        protocol='ipv4',
        required=True,
        label='Adresse IPv4',
        widget = forms.TextInput(attrs={'class': 'form-control','type': 'tel', 'pattern': '^(\d{1,3}\.){3}\d{1,3}$'})
        )

    class Meta:
        model = IpAdress
        fields = ['name', 'description','interface','ipv4']
        

class IpAdressUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la salle serveur '}),      
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description interface réseau','id':'message', 'style': 'height: 100px;'})
        )

    interface = forms.ModelChoiceField(
        queryset=NetworkInterface.objects.all(),
        label='Interface Réseau',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une interface réseau'}),
    )
    ipv4 = forms.GenericIPAddressField(
        protocol='ipv4',
        required=True,
        label='Adresse IPv4',
        widget = forms.TextInput(attrs={'class': 'form-control','type': 'tel', 'pattern': '^(\d{1,3}\.){3}\d{1,3}$'}),
            
        )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = IpAdress
        fields = fields = ['name', 'description','interface','ipv4']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
    
class ServerForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du serveur",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du serveur'}), 

        )
    type_server = forms.ChoiceField(
        label="Type de serveur",
        choices=NAME_SERVER_TYPE_CHOICES,  # Remplacez 'NAME_SERVER_TYPE_CHOICES' par le vrai nom de vos choix
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    ram = forms.IntegerField(
        label="memoire ram",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire ram en gb'})
        )
    rom = forms.IntegerField(
        label="memoire rom",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire rom en tera'})
        )
    nb_processor = forms.IntegerField(
        label="nombre de processor",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'nombre de processeur'})
        )
    v_processor = forms.IntegerField(
        label="vitesse processeur",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'vitesse individuelle des processeur'})
        )
    sys_stockage = forms.ModelMultipleChoiceField(
        queryset=SystemeStockage.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'Selectionnez les systemes de stockage'}), 
        label='Systeme de stockage',
        required=False
        )
 
    rack = forms.ModelChoiceField(
        queryset=Rack.objects.all(),
        label='Rack',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Entrez le rack dans lequel se trouve le serveur'}),
    )
    

    class Meta:
        model = Server
        fields = ['name','type_server', 'ram','rom','nb_processor','v_processor','sys_stockage','rack']
        

class ServerUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du serveur",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du serveur'}), 

        )
    type_server = forms.ChoiceField(
        label="Type de serveur",
        choices=NAME_SERVER_TYPE_CHOICES,  # Remplacez 'NAME_SERVER_TYPE_CHOICES' par le vrai nom de vos choix
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    ram = forms.IntegerField(
        label="memoire ram",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire ram en gb'})
        )
    rom = forms.IntegerField(
        label="memoire rom",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire rom en tera'})
        )
    nb_processor = forms.IntegerField(
        label="nombre de processor",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'nombre de processeur'})
        )
    v_processor = forms.IntegerField(
        label="vitesse processeur",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'vitesse individuelle des processeur'})
        )
    sys_stockage = forms.ModelMultipleChoiceField(
        queryset=SystemeStockage.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'Selectionnez les systemes de stockage'}), 
        label='Systeme de stockage',
        required=False
        )
   
    rack = forms.ModelChoiceField(
        queryset=Rack.objects.all(),
        label='Rack',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Entrez le rack dans lequel se trouve le serveur'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Server
        fields = ['name','type_server','ram','rom','nb_processor','v_processor','sys_stockage','rack']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
            instance.sys_stockage.set(self.cleaned_data['sys_stockage'])
            
        if commit:
            instance.save()
        return instance

class ClusterForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du cluster",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du cluster'}),      
        )
    ip_address = forms.ModelChoiceField(
        queryset=IpAdress.objects.all(),
        label='Adresse ip',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une adresse ip'}),
    )
    servers = forms.ModelMultipleChoiceField(
        queryset= Server.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'ajoutez un ou plusieurs serveurs'}), 
        label='Serveur',
    )
    class Meta:
        model = Cluster
        fields = ['name','ip_address','servers']
        

class ClusterUpdateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom du cluster",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du cluster'}),      
        )
    ip_address = forms.ModelChoiceField(
        queryset=IpAdress.objects.all(),
        label='Adresse ip',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une adresse ip'}),
    )
    servers = forms.ModelMultipleChoiceField(
        queryset= Server.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'ajoutez un ou plusieurs serveurs'}), 
        label='Serveurs',
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Cluster
        fields = ['name','ip_address','servers']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
            instance.servers.set(self.cleaned_data['servers'])
        if commit:
            instance.save()
        return instance
  
class DeploiementClusterForm(forms.ModelForm):
    cluster = forms.ModelChoiceField(
        queryset=Cluster.objects.all(),
        label='Cluster',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le cluster'}),
    )
    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Serveur',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )


    class Meta:
        model = DeploiementCluster
        fields = ['cluster', 'server']
        

class DeploiementClusterUpdateForm(forms.ModelForm):
    cluster = forms.ModelChoiceField(
        queryset=Cluster.objects.all(),
        label='Cluster',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le cluster'}),
    )
    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Serveur',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = DeploiementCluster
        fields = ['cluster', 'server']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
 
class PartitionForm(forms.ModelForm):
    serveur = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Serveur',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un serveur'}),
    )
    stockage = forms.ModelChoiceField(
        queryset=SystemeStockage.objects.all(),
        label='Stockage',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un systeme de stockage'}),
    )

    class Meta:
        model = Partition
        fields = ['serveur', 'stockage']
        

class PartitionUpdateForm(forms.ModelForm):
    serveur = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Serveur',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un serveur'}),
    )
    stockage = forms.ModelChoiceField(
        queryset=SystemeStockage.objects.all(),
        label='Stockage',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un systeme de stockage'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Partition
        fields = ['serveur', 'stockage']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class DatabaseServerForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom du serveur",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du serveur'}), 

    )

    ram = forms.IntegerField(
    label="memoire ram",
    help_text="Minimum 4 caractères, maximum 150.",      
    widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire ram en gb'})
    )
    rom = forms.IntegerField(
    label="memoire rom",
    help_text="Minimum 4 caractères, maximum 150.",      
    widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire rom en tera'})
    )
    cluster = forms.ModelChoiceField(
        queryset=Cluster.objects.all(),
        label='Cluster',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le cluster'}),
    )
    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Serveur',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )

    class Meta:
        model = DatabaseServer
        fields = ['name','ram','rom','cluster', 'server']
            

class DatabaseServerUpdateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom du serveur",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du serveur'}), 

    )

    ram = forms.IntegerField(
    label="memoire ram",
    help_text="Minimum 4 caractères, maximum 150.",      
    widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire ram en gb'})
    )
    rom = forms.IntegerField(
    label="memoire rom",
    help_text="Minimum 4 caractères, maximum 150.",      
    widget=forms.NumberInput(attrs={'class':'form-control','placeholder': 'memoire rom en tera'})
    )
    cluster = forms.ModelChoiceField(
        queryset=Cluster.objects.all(),
        label='Cluster',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le cluster'}),
    )
    server = forms.ModelChoiceField(
        queryset=Server.objects.all(),
        label='Serveur',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = DatabaseServer
        fields = ['name','ram','rom','cluster', 'server']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
class DatabaseForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom de la base de donnée",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du serveur'}), 

    )
    module_applicatifs = forms.ModelMultipleChoiceField(
    queryset=ModuleApplicatif.objects.all(), 
    widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'Selectionnez les systemes de stockage'}), 
    label='Module applicatifs',
    required = False
    
    )
    db_server = forms.ModelChoiceField(
      queryset=DatabaseServer.objects.all(),
      label='Serveur de base de donnée',
      widget=forms.Select(attrs={'class': 'form-control','placeholder':'Entrez le serveur de bd qui heberge la base de donnée'}),
    )
    class Meta:
      model = Database
      fields = ['name','db_server','module_applicatifs']
    

class DatabaseUpdateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom de la base de donnée",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du serveur'}), 

    )
    module_applicatifs = forms.ModelMultipleChoiceField(
    queryset=ModuleApplicatif.objects.all(), 
    widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'Selectionnez les systemes de stockage'}), 
    label='Module applicatifs',
    required = False
    )
    db_server = forms.ModelChoiceField(
    queryset=DatabaseServer.objects.all(),
    label='Serveur de base de donnée',
    widget=forms.Select(attrs={'class': 'form-control','placeholder':'Entrez le rack dans lequel se trouve le serveur'}),
    )
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Database
        fields = ['name','db_server','module_applicatifs']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance.historical_change_reason = historical_change_reason
            instance.module_applicatifs.set(self.cleaned_data['module_applicatifs'])
            
        if commit:
            instance.save()
        return instance
    

############# END SYSTEME MODULE FORMS ###############################
#################Documentation forms###################
    
class BackupStrategieCreateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom de la strategie",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la backup strategie'}), 

    )
    file = forms.FileField(
        label="fichier pdf",
        allow_empty_file= False,
        help_text="selectionner un fichier pdf",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez un fichier pdf a la backup strategie'}),
         
        )

    class Meta:
        model = BackupStrategie
        fields = ['name', 'file']
class BackupStrategieUpdateForm(BackupStrategieCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = BackupStrategie
        fields = ['name', 'file']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
class TechnicalRecoveryPlanCreateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom du plan",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du plan de reprise tecnique'}), 
    )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description plan de reprise technique', 'style': 'height: 100px;'})
        )
    application = forms.ModelChoiceField(
        queryset=Application.objects.all(),
        label='Application',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une application'}),
    )
    file = forms.FileField(
        label="fichier pdf",
        allow_empty_file= False,
        help_text="selectionner un fichier pdf",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez un fichier pdf a la backup strategie'}),
         
        )

    class Meta:
        model = TechnicalRecoveryPlan
        fields = ['name','description','application' ,'file']
class TechnicalRecoveryPlanUpdateForm(TechnicalRecoveryPlanCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = TechnicalRecoveryPlan
        fields = ['name','description','application','file']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class DataDictionnaryCreateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom du dictionnaire de données",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du dictionnaire de données'}), 

    )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description dictionnaire de données', 'style': 'height: 100px;'})
        )

    file = forms.FileField(
        label="fichier pdf",
        allow_empty_file= False,
        help_text="selectionner un fichier pdf",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez un fichier pdf a la backup strategie'}),
         
        )

    class Meta:
        model = DataDictionnary
        fields = ['name','description' ,'file']
class DataDictionnaryUpdateForm(DataDictionnaryCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = DataDictionnary
        fields = ['name','description','file']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class ArchitectureDiagramCreateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom du diagramme",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du diagramme d\'architecture'}), 
    )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description du diagramme d\'architecture', 'style': 'height: 100px;'})
        )
    process = forms.ModelChoiceField(
        queryset=Process.objects.all(),
        label='Process',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )
    file = forms.FileField(
        label="fichier pdf",
        allow_empty_file= False,
        help_text="selectionner un fichier pdf",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez un fichier pdf a la backup strategie'}),
         
        )

    class Meta:
        model = ArchitectureDiagram
        fields = ['name','description','process' ,'file']
class ArchitectureDiagramUpdateForm(ArchitectureDiagramCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = ArchitectureDiagram
        fields = ['name','description','process','file']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance



class CallFlowCreateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom du call flow",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du call flow'}), 
    )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description du call flow', 'style': 'height: 100px;'})
        )
    use_case = forms.ModelChoiceField(
        queryset=UseCase.objects.all(),
        label='use case',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un use case'}),
    )
    file = forms.FileField(
        label="fichier pdf",
        allow_empty_file= False,
        help_text="selectionner un fichier pdf",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez un fichier pdf a la backup strategie'}),
         
        )

    class Meta:
        model = CallFlow
        fields = ['name','description','use_case' ,'file']
class CallFlowUpdateForm(CallFlowCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = CallFlow
        fields = ['name','description','use_case','file']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance




class ApiSpecificationCreateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom ",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la spécification'}), 
    )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description interface réseau','id':'message', 'style': 'height: 100px;'})
        )
    api = forms.ModelChoiceField(
        queryset=Api.objects.all(),
        label='Api',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une api'}),
    )
    file = forms.FileField(
        label="fichier pdf",
        allow_empty_file= False,
        help_text="selectionner un fichier pdf",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez un fichier pdf a la backup strategie'}),
         
        )

    class Meta:
        model = ApiSpecification
        fields = ['name','description','api' ,'file']
class ApiSpecificationUpdateForm(ApiSpecificationCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = ApiSpecification
        fields = ['name','description','api','file']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
  



class ApiDocumentationCreateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom ",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom de la documentation api'}), 
    )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description de la documentation api', 'style': 'height: 100px;'})
        )
    api_specification = forms.ModelChoiceField(
        queryset=ApiSpecification.objects.all(),
        label='api spécification',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )
    file = forms.FileField(
        label="fichier pdf",
        allow_empty_file= False,
        help_text="selectionner un fichier pdf",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez un fichier pdf a la backup strategie'}),
        
        )

    class Meta:
        model = ApiDocumentation
        fields = ['name','description','api_specification' ,'file']
class ApiDocumentationUpdateForm(ApiDocumentationCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = ApiDocumentation
        fields = ['name','description','api_specification' ,'file']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance



class DataModelCreateForm(forms.ModelForm):
    name = forms.CharField(
    max_length=150,
    min_length=4,
    label="Nom ",
    help_text="Minimum 4 caractères, maximum 150.",
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du modele de données'}), 
    )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description du modèle de donnée', 'style': 'height: 100px;'})
        )
    data_dictionnary = forms.ModelMultipleChoiceField(
        queryset= DataDictionnary.objects.all(), 
        widget=forms.SelectMultiple(attrs={'class':'form-control','style': 'height: 100px;','placeholder':'ajoutez un ou plusieurs dictionnaire de données'}), 
        label='Dictionnaire de donnée',
    )
    database = forms.ModelChoiceField(
        queryset=Database.objects.all(),
        label='database',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )

    file = forms.FileField(
        label="fichier pdf",
        allow_empty_file= False,
        help_text="selectionner un fichier pdf",
        widget=forms.ClearableFileInput(attrs={'class':'form-control','placeholder':'Ajoutez un fichier pdf a la backup strategie'}),
         
        )

    class Meta:
        model = DataModel
        fields = ['name','description','database','data_dictionnary' ,'file']
class DataModelUpdateForm(DataModelCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = DataModel
        fields = ['name','description','database','data_dictionnary' ,'file']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
            instance.data_dictionnary.set(self.cleaned_data['data_dictionnary'])
        if commit:
            instance.save()
        return instance



class DataDictionnaryModelCreateForm(forms.ModelForm):

    data_model = forms.ModelChoiceField(
        queryset=DataModel.objects.all(),
        label='modele de donnée',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )
    data_dictionnary = forms.ModelChoiceField(
        queryset=DataDictionnary.objects.all(),
        label='dictionnaire de donnée',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner le serveur'}),
    )

    class Meta:
        model = DataDictionnaryModel
        fields = ['data_model','data_dictionnary']
class DataDictionnaryModelUpdateForm(DataDictionnaryModelCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = DataDictionnaryModel
        fields = ['data_model','data_dictionnary']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance
class DomainNameCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du nom de domaine'}), 
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description du  nom de domaine', 'style': 'height: 100px;'})
        )
    ip_adress = forms.ModelChoiceField(
        queryset=IpAdress.objects.all(),
        label='adresse ip',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une adresse ip'}),
    )

    class Meta:
        model = DomainName
        fields = ['name','description','ip_adress']
class DomainNameUpdateForm(DomainNameCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = DomainName
        fields = ['name','description','ip_adress']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class UrlCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du nom de domaine'}), 
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description du  nom de domaine', 'style': 'height: 100px;'})
        )
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un module applicatif'}),
    )
    domain_name = forms.ModelChoiceField(
        queryset=DomainName.objects.all(),
        label='Nom de domaine',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un nom de domaine'}),
    )

    class Meta:
        model = Url
        fields = ['name','description','module_applicatif','domain_name']
class UrlUpdateForm(UrlCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = Url
        fields = ['name','description','module_applicatif','domain_name']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance.historical_change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class SmppAccountCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du nom de domaine'}), 
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description du  nom de domaine', 'style': 'height: 100px;'})
        )
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un module applicatif'}),
    )


    class Meta:
        model = SmppAccount
        fields = ['name','description','module_applicatif']
class SmppAccountUpdateForm(SmppAccountCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = SmppAccount
        fields = ['name','description','module_applicatif']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance.historical_change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class SmsShortCodeCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du nom de domaine'}), 
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description du  compte smpp', 'style': 'height: 100px;'})
        )
    code = forms.CharField(
        max_length=150,
        min_length=4,
        label="code",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom code du compte smpp'}), 
        )
    smpp_account = forms.ModelChoiceField(
        queryset=SmppAccount.objects.all(),
        label='Compte smpp',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un compte smpp'}),
    )


    class Meta:
        model = SmsShortCode
        fields = ['name','description','smpp_account','code']
class SmsShortCodeUpdateForm(SmsShortCodeCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = SmsShortCode
        fields = ['name','description','smpp_account','code']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance.historical_change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class UssdShortCodeCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom du nom de domaine'}), 
        )
    description = forms.CharField(
        label="Description ",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description du  compte smpp', 'style': 'height: 100px;'})
        )
    code = forms.CharField(
        max_length=150,
        min_length=4,
        label="code",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Entrez le nom code du compte smpp'}), 
        )
    url = forms.ModelChoiceField(
        queryset=Url.objects.all(),
        label='url',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une url'}),
    )


    class Meta:
        model = UssdShortCode
        fields = ['name','description','url','code']
class UssdShortCodeUpdateForm(UssdShortCodeCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = UssdShortCode
        fields = ['name','description','url','code']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance.historical_change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class MobileAppCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nom application mobile'}),      
        )
    description = forms.CharField(
        label="Description",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description application mobile','id':'message', 'style': 'height: 100px;'})
        )

    class Meta:
        model = MobileApp
        fields = ['name', 'description']
        

class MobileAppUpdateForm(MobileAppCreateForm):

    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = MobileApp
        fields = ['name', 'description']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance

class DesktopAppCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=150,
        min_length=4,
        label="Nom",
        help_text="Minimum 4 caractères, maximum 150.",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nom application bureau'}),      
        )
    description = forms.CharField(
        label="Description",
        help_text="Minimum 4 caractères, maximum 150.",      
        widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'description application bureau','id':'message', 'style': 'height: 100px;'})
        )

    class Meta:
        model = DesktopApp
        fields = ['name', 'description']
        

class DesktopAppUpdateForm(DesktopAppCreateForm):

    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = DesktopApp
        fields = ['name', 'description']

    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance._change_reason = historical_change_reason
        if commit:
            instance.save()
        return instance


class ConnexionAppCreateForm(forms.ModelForm):
    mobile_app = forms.ModelChoiceField(
        queryset=MobileApp.objects.all(),
        label='Application Mobile',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une application mobile'}),
    )
    desktop_app = forms.ModelChoiceField(
        queryset=DesktopApp.objects.all(),
        label='Application Bureau',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une application bureau'}),
    )
    url = forms.ModelChoiceField(
        queryset=Url.objects.all(),
        label='url',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une url'}),
    )

    class Meta:
        model = ConnexionApp
        fields = ['desktop_app','mobile_app','url']
class ConnexionAppUpdateForm(ConnexionAppCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = ConnexionApp
        fields = ['desktop_app','mobile_app','url']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance.historical_change_reason = historical_change_reason
            
        if commit:
            instance.save()
        return instance

class AppDeploymentCreateForm(forms.ModelForm):
    module_applicatif = forms.ModelChoiceField(
        queryset=ModuleApplicatif.objects.all(),
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un module applicatif'}),
    )
    app_server = forms.ModelChoiceField(
        queryset=AppServer.objects.all(),
        label="Serveur d'application",
        widget=forms.Select(attrs={'class': 'form-control','placeholder':"Selectionner un serveur d'application"}),
    )
    class Meta:
        model = AppDeployment
        fields = ['module_applicatif','app_server']
    
class AppDeploymentUpdateForm(AppDeploymentCreateForm):
    historical_change_reason = forms.CharField(
        label="Raison du changement historique",
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Raison du changement historique', 'style': 'height: 100px;'}),
    )
    class Meta:
        model = AppDeployment
        fields = ['module_applicatif','app_server']
    def save(self, commit=True):
        instance = super().save(commit=False)
        historical_change_reason = self.cleaned_data.get('historical_change_reason', None)

        if historical_change_reason:
            # Ajoutez une explication à la sauvegarde historique
            instance.historical_change_reason = historical_change_reason
            
        if commit:
            instance.save()
        return instance




#################end documentation forms#############################