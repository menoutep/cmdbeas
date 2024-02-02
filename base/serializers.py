from rest_framework import serializers
from .models import Partition,AppelApi,Api,Process,UseCase,SubProcess,CallFlow,IpAdress,BackupStrategie, ServerRoom,Server,SystemeStockage,Datacenter,Departement,DeploiementCluster,Application,AppType,ModuleApplicatif,Vendor,Cluster,Rack,DatabaseServer,Database,DataDictionnary,DataDictionnaryModel,DataModel,DesktopApp,DomainName,NetworkInterface,Notifications,ConnexionBD,AppDeployment,AppServer
from .models import Url,ArchitectureDiagram,TechnicalRecoveryPlan,DataDictionnary,DataDictionnaryModel,DataModel,CallFlow,ApiDocumentation,ApiSpecification,SmppAccount,SmsShortCode,UssdShortCode,ConnexionApp,MobileApp,DesktopApp


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'
        
 

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'



class DatacenterSerializer(serializers.ModelSerializer):
    servers_rooms = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Datacenter
        fields = ['name', 'localisation', 'servers_rooms']
    


class ServerRoomSerializer(serializers.ModelSerializer):
    datacenter = DatacenterSerializer(read_only=True)
    racks = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = ServerRoom
        fields = ['name', 'datacenter', 'racks']
     


class RackSerializer(serializers.ModelSerializer):
    server_room = ServerRoomSerializer(read_only=True)
    servers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Rack
        fields = ['name','server_room','servers']


class AppTypeSerializer(serializers.ModelSerializer):
    applications = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = AppType
        fields = ['name','description','applications']
     

class ProcessSerializer(serializers.ModelSerializer):
    sub_processes = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Process
        fields = ['name','description','sub_processes']
     
class SubProcessSerializer(serializers.ModelSerializer):
    process = ProcessSerializer(read_only=True)
    uses_cases = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = SubProcess
        fields = ['name','description','processes','uses_cases']
     
class UseCaseSerializer(serializers.ModelSerializer):
    sub_process = SubProcessSerializer(read_only=True)
    appels_apis = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = UseCase
        fields = ['name','description','sub_process','appels_api']
     

class BackupStrategieSerializer(serializers.ModelSerializer):
    applications = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = BackupStrategie
        fields = ['name','applications','file']
     


      
class ApplicationSerializer(serializers.ModelSerializer):
    app_type = AppTypeSerializer(read_only=True)
    backup_strategie = BackupStrategieSerializer(read_only=True)
    modules_applicatifs = serializers.StringRelatedField(many=True, read_only=True)
    technicals_recoveries_plans = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Application
        fields = ['name','control_name','description','app_type','modules_applicatifs','replication','priority','deployement_year','backup_strategie','technicals_recoveries_plans']
     


class ModuleApplicatifSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)
    departement = DepartementSerializer(read_only=True)
    databases = serializers.StringRelatedField(many=True, read_only=True)
    notifications = serializers.StringRelatedField(many=True, read_only=True)
    apis = serializers.StringRelatedField(many=True, read_only=True)
    appels_apis = serializers.StringRelatedField(many=True, read_only=True)
    apps_servers = serializers.StringRelatedField(many=True, read_only=True)
    urls = serializers.StringRelatedField(many=True, read_only=True)
    smpps_accounts = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = ModuleApplicatif
        fields = ['name','description','application','vendor','departement','databases','notifications','apis','appels_apis','apps_servers','urls','smpps_accounts']
     

class ApiSerializer(serializers.ModelSerializer):
    module_applicatif = ModuleApplicatifSerializer(read_only=True)
    appels_apis = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Api
        fields = ['name','description','module_applicatif','appels_apis']
     
class AppelApiSerializer(serializers.ModelSerializer):
    module_applicatif = ModuleApplicatifSerializer(read_only=True)
    api = ApiSerializer(read_only=True)
    use_case = UseCaseSerializer(read_only=True)
    class Meta:
        model = AppelApi
        fields = ['name','description','module_applicatif','api','use_case','appels_apis']
    
class SystemeStockageSerializer(serializers.ModelSerializer):
    servers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = SystemeStockage
        fields = ['name','ram','rom','servers']
     


class ServerSerializer(serializers.ModelSerializer):
    sys_stockage = SystemeStockageSerializer(many=True,read_only=True)
    rack = RackSerializer(read_only=True)
    networks_interfaces = serializers.StringRelatedField(many=True, read_only=True)
    clusters = serializers.StringRelatedField(many=True, read_only=True)
    databases_servers = serializers.StringRelatedField(many=True, read_only=True)
    apps_servers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Server
        fields = ['name','type_server','sys_stockage','rack','networks_interfaces','clusters','databases_servers','apps_servers']
        depth = 9


class NetworkInterfaceSerializer(serializers.ModelSerializer):
    server = ServerSerializer(read_only=True)
    ip_addresses = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = NetworkInterface
        fields = ['name','description','server','ip_addresses']

class IpAdressSerializer(serializers.ModelSerializer):
    clusters = serializers.StringRelatedField(many=True, read_only=True)
    domains_names = serializers.StringRelatedField(many=True, read_only=True)
    interface = NetworkInterfaceSerializer(read_only=True)
    class Meta:
        model = IpAdress
        fields = ['ipv4','interface','domains_names','clusters']
      
class ClusterSerializer(serializers.ModelSerializer):
    servers = ServerSerializer(many=True,read_only=True)
    ip_address = IpAdressSerializer(read_only=True)
    databases_servers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Cluster
        fields = ['name','ip_address','servers','databases_servers']

class DeploiementClusterSerializer(serializers.ModelSerializer):
    cluster = ClusterSerializer(read_only=True)
    serveur = ServerSerializer(read_only=True)
 
    class Meta:
        model = DeploiementCluster
        fields = '__all__'
     
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
    datas_models = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Database
        fields = ['name','db_server', 'module_applicatifs', 'datas_models']
class ConnexionBDSerializer(serializers.ModelSerializer):
    module_applicatifs = ModuleApplicatifSerializer(many=True,read_only=True)
    server = ServerSerializer(read_only=True)
 
    class Meta:
        model = ConnexionBD
        fields = ['server', 'module_applicatifs', 'updated', 'created']
   
class AppServerSerializer(serializers.ModelSerializer):
    module_applicatif = ModuleApplicatifSerializer(many=True,read_only=True)
    server = ServerSerializer(read_only=True)
 
    class Meta:
        model = AppServer
        fields = ['name','description', 'module_applicatif','server', 'updated', 'created']
     

class TechnicalRecoveryPlanSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)
    class Meta:
        model = TechnicalRecoveryPlan
        fields = ['name','description', 'application','file']
     
class DataDictionnarySerializer(serializers.ModelSerializer):
    datas_models = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = DataDictionnary
        fields = ['name','description', 'datas_models','file']
        depth = 9

class ArchitectureDiagramSerializer(serializers.ModelSerializer):
    process = ProcessSerializer(read_only=True)
    class Meta:
        model = ArchitectureDiagram
        fields = ['name','description', 'process','file']
        depth = 9

class CallFlowSerializer(serializers.ModelSerializer):
    use_case = UseCaseSerializer(read_only=True)
    class Meta:
        model = CallFlow
        fields = ['name','description', 'use_case','file']
        depth = 9

class ApiSpecificationSerializer(serializers.ModelSerializer):
    api = ApiSerializer(read_only=True)
    apis_documentations = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = ApiSpecification
        fields = ['name','description', 'api','apis_documentations','file']
        depth = 9

class ApiDocumentationSerializer(serializers.ModelSerializer):
    apis_specifications = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = ApiDocumentation
        fields = ['name','description','apis_specifications','file']
        depth = 9

class DataModelSerializer(serializers.ModelSerializer):
    data_dictionnary = DataDictionnarySerializer(many=True,read_only=True)
    database = DatabaseSerializer(read_only=True)
    class Meta:
        model = DataModel
        fields = ['name','description','database','data_dictionnary','file']
        depth = 9

class DataDictionnaryModelSerializer(serializers.ModelSerializer):
    data_dictionnary = DataDictionnarySerializer(read_only=True)
    data_model = DataModelSerializer(read_only=True)
    class Meta:
        model = DataDictionnaryModel
        fields = ['name','description','data_model','data_dictionnary','file']
        depth = 9

class DomainNameSerializer(serializers.ModelSerializer):
    urls = serializers.StringRelatedField(many=True, read_only=True)
    ip_adress = IpAdressSerializer(read_only=True)
    class Meta:
        model = DomainName
        fields = ['name','description','ip_adress','urls']
     
class UrlSerializer(serializers.ModelSerializer):
    module_applicatif = ModuleApplicatifSerializer(read_only=True)
    domain_name = DomainNameSerializer(read_only=True)
    connexions_apps = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Url
        fields = ['name','description','ip_adress','module_applicatif','connexions_apps']
     
class SmppAccountSerializer(serializers.ModelSerializer):
    sms_short_codes = serializers.StringRelatedField(many=True, read_only=True)
    module_applicatif = ModuleApplicatifSerializer(read_only=True)
    class Meta:
        model = SmppAccount
        fields = ['name','code','module_applicatif','sms_short_codes']
     
class SmsShortCodeSerializer(serializers.ModelSerializer):
    smpp_account = SmppAccountSerializer(read_only=True)
    class Meta:
        model = SmsShortCode
        fields = ['name','code','smpp_account']
     
class UssdShortCodeSerializer(serializers.ModelSerializer):
    url = UrlSerializer(read_only=True)
    class Meta:
        model = UssdShortCode
        fields = ['name','code','url']

class MobileAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileApp
        fields = ['name','description']
     
class DesktopAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileApp
        fields = ['name','description']
     
class ConnexionAppSerializer(serializers.ModelSerializer):
    mobile_app = MobileAppSerializer(read_only=True)
    desktop_app = DatabaseSerializer(read_only=True)
    url = UrlSerializer(read_only=True)
    class Meta:
        model = ConnexionApp
        fields = ['name','description','database','data_dictionnary','file']
        depth = 9
