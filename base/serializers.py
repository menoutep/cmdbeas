from rest_framework import serializers
from .models import Partition,AppelApi,Api,Process,UseCase,SubProcess,CallFlow,IpAdress,BackupStrategie, ServerRoom,Server,SystemeStockage,Datacenter,Departement,DeploiementCluster,Application,AppType,ModuleApplicatif,Vendor,Cluster,Rack,DatabaseServer,Database,DataDictionnary,DataDictionnaryModel,DataModel,DesktopApp,DomainName,NetworkInterface,Notifications,ConnexionBD,AppDeployment,AppServer
from .models import Url,ArchitectureDiagram,TechnicalRecoveryPlan,DataDictionnary,DataDictionnaryModel,DataModel,CallFlow,ApiDocumentation,ApiSpecification,SmppAccount,SmsShortCode,UssdShortCode,ConnexionApp,MobileApp,DesktopApp



##################################channels#######################
class SmsShortCodeSerializer(serializers.ModelSerializer):
    smpp_account = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SmsShortCode
        fields = ['name','code','smpp_account']

class SmppAccountSerializer(serializers.ModelSerializer):
    sms_short_codes = SmsShortCodeSerializer(many=True, read_only=True)
    module_applicatif = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SmppAccount
        fields = ['name','module_applicatif','sms_short_codes']
     

     
class UssdShortCodeSerializer(serializers.ModelSerializer):
    url = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UssdShortCode
        fields = ['name','code','url']

class ConnexionAppSerializer(serializers.ModelSerializer):
    mobile_app = serializers.StringRelatedField(read_only=True)
    desktop_app = serializers.StringRelatedField(read_only=True)
    url = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ConnexionApp
        fields = ['name','description','database','data_dictionnary','file']
        depth = 9

class MobileAppSerializer(serializers.ModelSerializer):
    connexions_apps = ConnexionAppSerializer(many=True, read_only=True)
    class Meta:
        model = MobileApp
        fields = ['name','description','connexions_apps']
     
class DesktopAppSerializer(serializers.ModelSerializer):
    connexions_apps = ConnexionAppSerializer(many=True, read_only=True)
    class Meta:
        model = MobileApp
        fields = ['name','description','connexions_apps']
     


class UrlSerializer(serializers.ModelSerializer):
    module_applicatif = serializers.StringRelatedField(read_only=True)
    domain_name = serializers.StringRelatedField(read_only=True)
    connexions_apps = ConnexionAppSerializer(many=True, read_only=True)
    ussd_short_codes = UssdShortCodeSerializer(many=True, read_only=True)
    connexions_apps = ConnexionAppSerializer(many=True, read_only=True)

    class Meta:
        model = Url
        fields = ['name','description','domain_name','module_applicatif','connexions_apps']
     
##################################end##############################

###############documentation serializers################"
class BackupStrategieSerializer(serializers.ModelSerializer):
    applications = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = BackupStrategie
        fields = ['name','applications','file']
class ApiDocumentationSerializer(serializers.ModelSerializer):
    apis_specifications = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = ApiDocumentation
        fields = ['name','description','apis_specifications','file']
        depth = 9
class ApiSpecificationSerializer(serializers.ModelSerializer):
    api = serializers.StringRelatedField(read_only=True)
    apis_documentations = ApiDocumentationSerializer(many=True,read_only=True)
    class Meta:
        model = ApiSpecification
        fields = ['name','description', 'api','apis_documentations','file']
        depth = 9

class DataModelSerializer(serializers.ModelSerializer):
    data_dictionnary = serializers.StringRelatedField(many=True, read_only=True)
    database =serializers.StringRelatedField(read_only=True)
    class Meta:
        model = DataModel
        fields = ['name','description','database','data_dictionnary','file']
        depth = 9      
class DataDictionnarySerializer(serializers.ModelSerializer):
    datas_models = DataModelSerializer(many=True, read_only=True)
    class Meta:
        model = DataDictionnary
        fields = ['name','description', 'datas_models','file']
        depth = 9
class TechnicalRecoveryPlanSerializer(serializers.ModelSerializer):
    application = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = TechnicalRecoveryPlan
        fields = ['name','description', 'application','file']

class ArchitectureDiagramSerializer(serializers.ModelSerializer):
    process = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ArchitectureDiagram
        fields = ['name','description', 'process','file']
        depth = 9
class DataDictionnaryModelSerializer(serializers.ModelSerializer):
    data_dictionnary = DataDictionnarySerializer(read_only=True)
    data_model = DataModelSerializer(read_only=True)
    class Meta:
        model = DataDictionnaryModel
        fields = ['data_model','data_dictionnary']
        depth = 9
#######################end############################
####################integration process ###############

class AppelApiSerializer(serializers.ModelSerializer):
    module_applicatif = serializers.StringRelatedField(read_only=True)
    api = serializers.StringRelatedField(read_only=True)
    use_case = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = AppelApi
        fields = ['name','description','module_applicatif','api','use_case']
   
class CallFlowSerializer(serializers.ModelSerializer):
    use_case = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = CallFlow
        fields = ['name','description', 'use_case','file']
        depth = 9

class UseCaseSerializer(serializers.ModelSerializer):
    sub_process = serializers.StringRelatedField(many=True, read_only=True)
    appels_apis = AppelApiSerializer(many=True, read_only=True)
    calls_flows = CallFlowSerializer(many=True, read_only=True)
    class Meta:
        model = UseCase
        fields = ['name','description','sub_process','appels_apis']

class SubProcessSerializer(serializers.ModelSerializer):
    process = serializers.StringRelatedField(many=True, read_only=True)
    uses_cases = UseCaseSerializer(many=True, read_only=True)
    architectures_diagrams = ArchitectureDiagramSerializer(many=True, read_only=True)
    class Meta:
        model = SubProcess
        fields = ['name','description','process','uses_cases','architectures_diagrams']

class ProcessSerializer(serializers.ModelSerializer):
    sub_processes = SubProcessSerializer(many=True, read_only=True)
    class Meta:
        model = Process
        fields = ['name','description','sub_processes']
        
class ApiSerializer(serializers.ModelSerializer):
    module_applicatif = serializers.StringRelatedField(read_only=True)
    appels_apis = AppelApiSerializer(many=True, read_only=True)
    apis_specifications = ApiSpecificationSerializer(many=True, read_only=True)
    class Meta:
        model = Api
        fields = ['name','description','module_applicatif','appels_apis','apis_specifications']
     


#####################end###############################

################application serialisers#################

class NotificationsSerializer(serializers.ModelSerializer):
    module_applicatif = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Notifications
        fields = ['name','description','trigger','module_applicatif','notifications']


################end#####################################
###################Network serialisers################

class DomainNameSerializer(serializers.ModelSerializer):
    urls = UrlSerializer(many=True, read_only=True)
    ip_adress = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = DomainName
        fields = ['name','description','ip_adress','urls']

class NetworkInterfaceSerializer(serializers.ModelSerializer):
    server = serializers.StringRelatedField(many=True, read_only=True)
    ip_addresses = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = NetworkInterface
        fields = ['name','description','server','ip_addresses']

class IpAdressSerializer(serializers.ModelSerializer):
    clusters = serializers.StringRelatedField(many=True, read_only=True)
    domains_names = DomainNameSerializer(many=True, read_only=True)
    interface = NetworkInterfaceSerializer(read_only=True)
    class Meta:
        model = IpAdress
        fields = ['ipv4','interface','domains_names','clusters']
    
######################end####################################
     
##############systeme serializers####################


class ServerSerializer(serializers.ModelSerializer):
    sys_stockage = serializers.StringRelatedField(many=True, read_only=True)
    rack = serializers.StringRelatedField(read_only=True)
    networks_interfaces = serializers.StringRelatedField(many=True, read_only=True)
    clusters = serializers.StringRelatedField(many=True, read_only=True)
    databases_servers = serializers.StringRelatedField(many=True, read_only=True)
    apps_servers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Server
        fields = ['name','type_server','sys_stockage','rack','networks_interfaces','clusters','databases_servers','apps_servers']
        depth = 9
class SystemeStockageSerializer(serializers.ModelSerializer):
    servers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = SystemeStockage
        fields = ['name','ram','rom','servers']
class RackSerializer(serializers.ModelSerializer):
    server_room = serializers.StringRelatedField(read_only=True)
    servers = ServerSerializer(many=True, read_only=True)
    class Meta:
        model = Rack
        fields = ['name','server_room','servers']

class ServerRoomSerializer(serializers.ModelSerializer):
    datacenter = serializers.StringRelatedField(read_only=True)
    racks = RackSerializer(many=True, read_only=True)
    
    class Meta:
        model = ServerRoom
        fields = ['name', 'datacenter', 'racks']
     

class DatacenterSerializer(serializers.ModelSerializer):
    servers_rooms = ServerRoomSerializer(many=True, read_only=True)

    class Meta:
        model = Datacenter
        fields = ['name', 'localisation', 'servers_rooms']
    

##############end####################################

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'
        




class AppDeploymentSerializer(serializers.ModelSerializer):
    app_server = serializers.StringRelatedField(read_only=True)
    module_applicatif = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = AppDeployment
        fields = ['module_applicatif', 'app_server']
        depth = 9

class ModuleApplicatifSerializer(serializers.ModelSerializer):
    application = serializers.StringRelatedField(read_only=True)
    vendor = serializers.StringRelatedField(read_only=True)
    departement = serializers.StringRelatedField(read_only=True)
    databases = serializers.StringRelatedField(many=True, read_only=True)
    notifications = NotificationsSerializer(many=True, read_only=True)
    apis = ApiSerializer(many=True, read_only=True)
    appels_apis = AppelApiSerializer(many=True, read_only=True)
    apps_servers = serializers.StringRelatedField(read_only=True)
    apps_deployments = AppDeploymentSerializer(many=True, read_only=True)
    urls = serializers.StringRelatedField(many=True, read_only=True)
    smpps_accounts = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = ModuleApplicatif
        fields = ['name','description','apps_deployments','application','vendor','departement','databases','notifications','apis','appels_apis','apps_servers','urls','smpps_accounts']
     
class AppServerSerializer(serializers.ModelSerializer):
    module_applicatif = ModuleApplicatifSerializer(many=True,read_only=True)
    server = ServerSerializer(read_only=True)
 
    class Meta:
        model = AppServer
        fields = ['name','description', 'module_applicatif','server', 'updated', 'created']
     
      
class ApplicationSerializer(serializers.ModelSerializer):
    app_type = serializers.StringRelatedField(read_only=True)
    backup_strategie = BackupStrategieSerializer(read_only=True)
    modules_applicatifs = serializers.StringRelatedField(many=True, read_only=True)
    technicals_recoveries_plans = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Application
        fields = ['name','control_name','description','app_type','modules_applicatifs','replication','priority','deployement_year','backup_strategie','technicals_recoveries_plans']
     

class AppTypeSerializer(serializers.ModelSerializer):
    applications = ApplicationSerializer(many=True, read_only=True)
    class Meta:
        model = AppType
        fields = ['name','description','applications']


class VendorSerializer(serializers.ModelSerializer):
    modules_applicatifs = ModuleApplicatifSerializer(many=True, read_only=True)
    class Meta:
        model = Vendor
        fields = ['name','description','modules_applicatifs']




class DeploiementClusterSerializer(serializers.ModelSerializer):
    cluster = serializers.StringRelatedField(read_only=True)
    serveur = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = DeploiementCluster
        fields = ['cluster','serveur','updated','created']

class ClusterSerializer(serializers.ModelSerializer):
    deploiement_clusters = DeploiementClusterSerializer(many=True,read_only=True)
    servers = ServerSerializer()
    ip_address = IpAdressSerializer(read_only=True)
    databases_servers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Cluster
        fields = ['name','ip_address','deploiement_clusters','databases_servers','servers'] 
        #fields = '__all__'
        
        

class PartitionSerializer(serializers.ModelSerializer):
    stockage = SystemeStockageSerializer(read_only=True)
    serveur = ServerSerializer(read_only=True)
 
    class Meta:
        model = Partition
        fields = '__all__'
     
class DatabaseServerSerializer(serializers.ModelSerializer):
    cluster = ClusterSerializer(read_only=True)
    server = ServerSerializer(read_only=True)
    databases = serializers.StringRelatedField(many=True, read_only=True)
 
    class Meta:
        model = DatabaseServer
        fields = ['name','cluster', 'server', 'databases']
     
class DatabaseSerializer(serializers.ModelSerializer):
    module_applicatifs = ModuleApplicatifSerializer(many=True,read_only=True)
    db_server = DatabaseServerSerializer(read_only=True)
    datas_models = DataModelSerializer(many=True, read_only=True)
    class Meta:
        model = Database
        fields = ['name','db_server', 'module_applicatifs', 'datas_models']
class ConnexionBDSerializer(serializers.ModelSerializer):
    module_applicatifs = ModuleApplicatifSerializer(many=True,read_only=True)
    server = ServerSerializer(read_only=True)
 
    class Meta:
        model = ConnexionBD
        fields = ['server', 'module_applicatifs', 'updated', 'created']
   

class DataDictionnarySerializer(serializers.ModelSerializer):
    datas_models = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = DataDictionnary
        fields = ['name','description', 'datas_models','file']
        depth = 9















