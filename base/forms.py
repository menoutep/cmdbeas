# forms.py
from django import forms
from .models import AppelApi,Api,ModuleApplicatif,Departement,AppType,Process,UseCase,CallFlow,SubProcess,Api,Datacenter,ServerRoom,Rack,Cluster,SystemeStockage,Server,Partition,DeploiementCluster,Database,DatabaseServer,DataDictionnary,DataDictionnaryModel,DataModel,DesktopApp,DomainName,ArchitectureDiagram,Vendor,Application,BackupStrategie,NetworkInterface,Notifications,IpAdress
from base.models import PRIORITY_CHOICES,NAME_APP_TYPE_CHOICES


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
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
    )
    use_case = forms.ModelChoiceField(
        queryset=UseCase.objects.all(),
        label='Module applicatif',
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner un process'}),
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
        widget=forms.Select(attrs={'class': 'form-control','placeholder':'Selectionner une interface réseau'}),
    )
    ipv4 = forms.GenericIPAddressField(
        protocol='ipv4',
        required=True,
        label='Adresse IPv4',
        widget = forms.TextInput(attrs={'class': 'form-control','type': 'tel', 'pattern': '^(\d{1,3}\.){3}\d{1,3}$'}),

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
            instance.cluster.set(self.cleaned_data['cluster'])
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
            instance._change_reason = historical_change_reason
            instance.module_applicatifs.set(self.cleaned_data['module_applicatifs'])
            
        if commit:
            instance.save()
        return instance
############# END SYSTEME MODULE FORMS ###############################
