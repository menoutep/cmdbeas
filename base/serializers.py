from rest_framework import serializers
from .models import AppelApi,Api,Process,UseCase,SubProcess,CallFlow,IpAdress,BackupStrategie, ServerRoom,Server,SystemeStockage,Datacenter,Departement,DeploiementCluster,Application,AppType,ModuleApplicatif,Vendor,Cluster,Rack,DatabaseServer,Database,DataDictionnary,DataDictionnaryModel,DataModel,DesktopApp,DomainName,NetworkInterface,Notifications,ConnexionBD,AppDeployment,AppServer

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'
        
 

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'



class DatacenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datacenter
        fields = '__all__'
    


class ServerRoomSerializer(serializers.ModelSerializer):
    datacenter = DatacenterSerializer(read_only=True)
    class Meta:
        model = ServerRoom
        fields = ['id', 'name', 'datacenter', 'updated', 'created']
     


class RackSerializer(serializers.ModelSerializer):
    server_room = ServerRoomSerializer(read_only=True)
    class Meta:
        model = Rack
        fields = '__all__'
     

class AppTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppType
        fields = '__all__'
     

class ProcessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Process
        fields = '__all__'
     
class SubProcessSerializer(serializers.ModelSerializer):
    process = ProcessSerializer(read_only=True)
    class Meta:
        model = SubProcess
        fields = '__all__'
     
class UseCaseSerializer(serializers.ModelSerializer):
    sub_process = SubProcessSerializer(read_only=True)
    class Meta:
        model = UseCase
        fields = '__all__'
     

class BackupStrategieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BackupStrategie
        fields = '__all__'
     


      
class ApplicationSerializer(serializers.ModelSerializer):
    app_type = AppTypeSerializer(read_only=True)
    backup_strategie = BackupStrategieSerializer(read_only=True)
    class Meta:
        model = Application
        fields = '__all__'
     


class ModuleApplicatifSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)
    departement = DepartementSerializer(read_only=True)
    class Meta:
        model = ModuleApplicatif
        fields = '__all__'
     

class ApiSerializer(serializers.ModelSerializer):
    module_applicatif = ModuleApplicatifSerializer(read_only=True)

    class Meta:
        model = Api
        fields = '__all__'
     
class AppelApiSerializer(serializers.ModelSerializer):
    module_applicatif = ModuleApplicatifSerializer(read_only=True)
    api = ApiSerializer(read_only=True)
    use_case = UseCaseSerializer(read_only=True)
    class Meta:
        model = AppelApi
        fields = '__all__'
    
class SystemeStockageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SystemeStockage
        fields = '__all__'
     




    

class ServerSerializer(serializers.ModelSerializer):
    sys_stockage = SystemeStockageSerializer(many=True,read_only=True)
   
    rack = RackSerializer(read_only=True)
    class Meta:
        model = Server
        fields = '__all__'
        depth=5


class NetworkInterfaceSerializer(serializers.ModelSerializer):
    server = ServerSerializer(read_only=True)
    class Meta:
        model = NetworkInterface
        fields = ['name','description','server','updated','created']

class IpAdressSerializer(serializers.ModelSerializer):

    interface = NetworkInterfaceSerializer(read_only=True)
    class Meta:
        model = IpAdress
        fields = '__all__'
      
class ClusterSerializer(serializers.ModelSerializer):
    servers = ServerSerializer(many=True,read_only=True)
    ip_address = IpAdressSerializer(read_only=True)
    class Meta:
        model = Cluster
        fields = '__all__'
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
        model = DeploiementCluster
        fields = '__all__'
     
class DatabaseServerSerializer(serializers.ModelSerializer):
    cluster = ClusterSerializer(read_only=True)
    server = ServerSerializer(read_only=True)
 
    class Meta:
        model = DatabaseServer
        fields = ['name','ram','rom','cluster', 'server', 'updated', 'created']
     
class DatabaseSerializer(serializers.ModelSerializer):
    module_applicatifs = ModuleApplicatifSerializer(many=True,read_only=True)
    db_server = DatabaseServerSerializer(read_only=True)
 
    class Meta:
        model = Database
        fields = ['name','db_server', 'module_applicatifs', 'updated', 'created']
     