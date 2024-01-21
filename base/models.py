from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class Departement(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)  
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords() 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Departement "
        verbose_name_plural = "Departements"

class Datacenter(models.Model):
    name = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = "Datacenter"
        verbose_name_plural = "Datacenters"


class ServerRoom(models.Model):
    name = models.CharField(max_length=200)
    datacenter = models.ForeignKey(Datacenter,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = "Salle Serveur"
        verbose_name_plural = "Salles Serveurs"

class Rack(models.Model):
    name = models.CharField(max_length=200)
    server_room = models.ForeignKey(ServerRoom,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = "Rack"
        verbose_name_plural = "Racks"

NAME_APP_TYPE_CHOICES = (
    ('in_house','In House'),
    ('vendor','Vendor'),
)

class AppType(models.Model):
    name = models.CharField(max_length=200,choices=NAME_APP_TYPE_CHOICES,default='vendor')
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        
        verbose_name = "Type de l'application"
        verbose_name_plural = "Types des applications"


class BackupStrategie(models.Model):
    name = models.CharField(max_length=255)
    file =  models.FileField(upload_to ='uploads/backup_strategie/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
    
   

    class Meta:
        
        verbose_name = "Backup strategie"
        verbose_name_plural = "Backup strategies"  


PRIORITY_CHOICES = (
    ('critical','critical'),
    ('modéré','modéré'),
    ('faible','faible')
)
class Application(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    replication = models.IntegerField()
    priority = models.CharField(max_length=200,choices=PRIORITY_CHOICES,default="faible")
    control_name = models.CharField(max_length=200)
    deployement_year = models.DateTimeField()
    app_type = models.ForeignKey(AppType,on_delete=models.RESTRICT)
    backup_strategie = models.ForeignKey(BackupStrategie,on_delete=models.RESTRICT)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
            return self.name

    class Meta:

        verbose_name = "Application"
        verbose_name_plural = "Applications"

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"
         
class ModuleApplicatif(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    application = models.ForeignKey(Application,on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor,on_delete=models.RESTRICT) 
    departement = models.ForeignKey(Departement,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Module Applicatif"
        verbose_name_plural = "Modules Applicatifs" 




class SystemeStockage(models.Model):
    name = models.CharField(max_length=200)
    ram = models.IntegerField()
    rom = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Système de stockage"
        verbose_name_plural = "Systèmes de stockages"




class Cluster(models.Model):
    name = models.CharField(max_length=200)
    #ip_address = models.ForeignKey(IpAdress,on_delete=models.SET_NULL,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"

NAME_SERVER_TYPE_CHOICES = (
    ('virtuel','virtuel'),
    ('physique','physique'),
)

class Server(models.Model):
    name = models.CharField(max_length=200)
    type_server = models.CharField(max_length=200,choices=NAME_SERVER_TYPE_CHOICES,default="physique")
    ram = models.IntegerField()
    rom = models.IntegerField()
    nb_processor = models.IntegerField()
    v_processor = models.IntegerField()
    sys_stockage = models.ManyToManyField(SystemeStockage,through="base.Partition")# creer si neccessaire les tables intermediaire pour les many to many pour chaque relation de ce type 
    cluster = models.ManyToManyField(Cluster,through="base.DeploiementCluster")
    rack = models.ForeignKey(Rack,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()# gerer apres les relations many to many
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Serveur "
        verbose_name_plural = "Serveurs"

class DeploiementCluster(models.Model):
    serveur = models.ForeignKey(Server,on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.serveur} - {self.cluster}"

    class Meta:
        verbose_name = "Deploiement cluster"
        verbose_name_plural = "Deploiements cluster"   


class Partition(models.Model):
    serveur = models.ForeignKey(Server,on_delete=models.CASCADE)
    stockage = models.ForeignKey(SystemeStockage,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.serveur} - {self.stockage}"

    class Meta:
        verbose_name = "Connexion serveur et système de stockage"
        verbose_name_plural = "Connexion serveurs et systèmes de stockages"   

class DatabaseServer(models.Model):
    name = models.CharField(max_length=200)
    ram = models.IntegerField()
    rom = models.IntegerField()
    server =  models.ForeignKey(Server,on_delete=models.SET_NULL,blank=True,null=True)
    cluster = models.ForeignKey(Cluster,on_delete=models.SET_NULL,blank=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Serveur de base de données"
        verbose_name_plural = "Serveurs de base de données"

class Database(models.Model):
    name = models.CharField(max_length=200) 
    db_server = models.ForeignKey(DatabaseServer,on_delete=models.CASCADE)
    module_applicatifs = models.ManyToManyField(ModuleApplicatif,through="ConnexionBD")# creer si neccessaire les tables intermediaire pour les many to many pour chaque relation de ce type    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Base de données"
        verbose_name_plural = "Bases de données"   


class ConnexionBD(models.Model):
    module_applicatif = models.ForeignKey(ModuleApplicatif,on_delete=models.CASCADE)
    database = models.ForeignKey(Database,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.module_applicatif} - {self.database}"

    class Meta:
        verbose_name = "Connexion module applicatif base de données "
        verbose_name_plural = "Connexion module applicatifs bases de données "   


class Notifications(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    trigger = models.CharField(max_length=200)
    notifications = models.CharField(max_length=200)
    module_applicatif = models.ForeignKey(ModuleApplicatif,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
class Api(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    module_applicatif = models.ForeignKey(ModuleApplicatif,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Api"
        verbose_name_plural = "Api's"

class Process(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Process"
        verbose_name_plural = "Process"


class SubProcess(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    process = models.ForeignKey(Process,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SubProcess"
        verbose_name_plural = "SubProcess"



class UseCase(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    sub_process = models.ForeignKey(SubProcess,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "UseCase"
        verbose_name_plural = "UseCases"


class AppelApi(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    module_applicatif = models.ForeignKey(ModuleApplicatif,on_delete=models.CASCADE)
    use_case = models.ForeignKey(UseCase,on_delete=models.CASCADE)
    api = models.ForeignKey(Api,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Appel Api"
        verbose_name_plural = "Appel Api's"



class NetworkInterface(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    server = models.ForeignKey(Server,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Interface Réseau "
        verbose_name_plural = "Interface Réseaux"


class IpAdress(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    interface = models.ForeignKey(NetworkInterface,on_delete=models.CASCADE)
    ipv4 = models.GenericIPAddressField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Adresse IP"
        verbose_name_plural = "Adresses IP"

class DomainName(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    ip_adress = models.ForeignKey(IpAdress,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Nom de domaine"
        verbose_name_plural = "Noms de domaines"


class AppServer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    server = models.ForeignKey(Server,on_delete=models.CASCADE)
    module_applicatif = models.ManyToManyField(ModuleApplicatif,through="AppDeployment")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Serveur d'application"
        verbose_name_plural = "Serveurs d'applications"



class AppDeployment(models.Model):
    module_applicatif = models.ForeignKey(ModuleApplicatif,on_delete=models.CASCADE)
    app_server = models.ForeignKey(AppServer,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.module_applicatif} - {self.app_server}"

    class Meta:
        verbose_name = "Deploiement module applicatif"
        verbose_name_plural = "Deploiements modules applicatifs "    


class MobileApp(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Application mobile"
        verbose_name_plural = "Applications mobiles"


class DesktopApp(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Application Bureau"
        verbose_name_plural = "Applications Bureaux"


class Url(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    module_applicatif = models.ForeignKey(ModuleApplicatif,on_delete=models.CASCADE)
    domain_name = models.ForeignKey(DomainName,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Url's"


class SmppAccount(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    module_applicatif = models.ForeignKey(ModuleApplicatif,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "compte smpp"
        verbose_name_plural = "comptes smpp"

class SmsShortCode(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    smpp_account = models.ForeignKey(SmppAccount,on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sms short code "
        verbose_name_plural = "Sms short codes "


class UssdShortCode(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    url = models.ForeignKey(Url,on_delete=models.CASCADE)
    code = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "USSD short code"
        verbose_name_plural = "USSD short codes"
class ConnexionApp(models.Model):
    mobile_app = models.ForeignKey(MobileApp,on_delete=models.SET_NULL,blank=True,null=True)
    desktop_app = models.ForeignKey(DesktopApp,on_delete=models.SET_NULL,blank=True,null=True)
    url = models.ForeignKey(Url,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.mobile_app} - {self.url}" if self.mobile_app else f"{self.desktop_app} - {self.url}"

    class Meta:
        verbose_name = "Connexion application et url "
        verbose_name_plural = "Connexion application et url" 



class TechnicalRecoveryPlan(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    application = models.ForeignKey(Application,on_delete=models.CASCADE)
    file =  models.FileField(upload_to ='uploads/technical_recovery_plan/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plan de reprise Technique"
        verbose_name_plural = "Plan de reprise Technique"  


class ArchitectureDiagram(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    process = models.ForeignKey(Process,on_delete=models.CASCADE)
    file =  models.FileField(upload_to ='uploads/architecture_diagram/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Plan de reprise Technique"
        verbose_name_plural = "Plan de reprise Technique"  

class CallFlow(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    use_case = models.ForeignKey(UseCase,on_delete=models.CASCADE)
    file =  models.FileField(upload_to ='uploads/call_flow/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Call Flow"
        verbose_name_plural = "Calls Flows"  

class ApiSpecification(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    api = models.ForeignKey(UseCase,on_delete=models.CASCADE)
    file =  models.FileField(upload_to ='uploads/api_specification/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Specification de l'api"
        verbose_name_plural = "Specifications des api's"


class ApiDocumentation(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    api_specification = models.ForeignKey(ApiSpecification,on_delete=models.CASCADE)
    file =  models.FileField(upload_to ='uploads/api_documentation/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Documentation de l'api"
        verbose_name_plural = "Documentations des api's"


class DataDictionnary(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    file =  models.FileField(upload_to ='uploads/data_dictionnary/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dictionnaire de données"
        verbose_name_plural = "Dictionnaires de données"


class DataModel(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(null=True, blank=True)
    database = models.ForeignKey(Database,on_delete=models.CASCADE)
    data_dictionnary = models.ManyToManyField(DataDictionnary,through="DataDictionnaryModel")
    file =  models.FileField(upload_to ='uploads/data_model/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Modèle de données"
        verbose_name_plural = "Modèles de données"
class DataDictionnaryModel(models.Model):
    data_model = models.ForeignKey(DataModel,on_delete=models.CASCADE)
    data_dictionnary = models.ForeignKey(DataDictionnary,on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.data_model} - {self.data_model}"

    class Meta:
        verbose_name = "Dictionnaire de données et modèle de données"
        verbose_name_plural = "Deploiements modules applicatifs "   
