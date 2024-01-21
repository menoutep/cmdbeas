from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
import json
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from base.models import Process,SubProcess,UseCase,Api,AppelApi,ServerRoom,Server,IpAdress,SystemeStockage,Datacenter,Departement,DeploiementCluster,Application,AppType,ModuleApplicatif,Vendor,Cluster,Rack,DatabaseServer,Database,DataDictionnary,DataDictionnaryModel,DataModel,DesktopApp,DomainName,NetworkInterface,Notifications,ConnexionBD,AppDeployment,AppServer
from accounts.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Departement,Partition
from django.views import View
from django.db.models import Q
from base.serializers import AppelApiSerializer,ApiSerializer,UseCaseSerializer,ProcessSerializer,SubProcessSerializer,DatacenterSerializer,ServerRoomSerializer,DepartementSerializer,DatabaseSerializer,DatabaseServerSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import ProcessForm,UseCaseUpdateForm,UseCaseForm,SubProcessForm,AppelApiForm,ApiForm,ApiUpdateForm,SubProcessUpdateForm,ProcessUpdateForm,AppelApiUpdateForm,IpAdressForm,IpAdressUpdateForm,NetworkInterfaceForm,NetworkInterfaceUpdateForm,DepartementForm,DepartementUpdateForm,AppTypeForm,AppTypeUpdateForm,DatacenterForm,DatacenterUpdateForm,ServerRoomForm,ServerRoomUpdateForm,RackForm,RackUpdateForm,ClusterForm,ClusterUpdateForm,SystemeStockageForm,SystemeStockageUpdateForm,ServerForm,ServerUpdateForm,DeploiementClusterUpdateForm,DeploiementClusterForm,PartitionForm,PartitionUpdateForm,DatabaseServerForm,DatabaseServerUpdateForm,DatabaseForm,DatabaseUpdateForm,VendorUpdateForm,VendorForm,ApplicationForm,ApplicationUpdateForm,ModuleApplicatifForm,ModuleApplicatifUpdateForm
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServerRoom
from .serializers import ServerRoomSerializer,NetworkInterfaceSerializer,IpAdressSerializer,ServerSerializer,VendorSerializer,DatacenterSerializer,DepartementSerializer,DeploiementClusterSerializer,PartitionSerializer,ClusterSerializer,SystemeStockageSerializer,ApplicationSerializer,ModuleApplicatifSerializer,AppTypeSerializer,RackSerializer,BackupStrategieSerializer

@login_required
def index(request):
    user = User.objects.get(email=request.user.email,username=request.user.username)
    if user.departement.name == "systeme" : 
        return render(request, 'systeme/index.html')
    
    if user.departement.name == "application" : 
        return render(request, 'application/index.html')
    
    if user.departement.name == "networking" : 
        return render(request, 'network/index.html')
    
    if user.departement.name == "integration" : 
        return render(request, 'integration/index.html')
   
    return render(request, 'base/index.html')

# views.py
######################Networking views#############
class NetworkInterfaceListView(ListView):
    model = NetworkInterface
    template_name = 'network/network_interface_list.html'
    context_object_name = 'network_interfaces'

class NetworkInterfaceDetailView(DetailView):
    model = NetworkInterface
    template_name = 'network/network_interface_detail.html'
    context_object_name = 'network_interface'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = NetworkInterfaceSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class NetworkInterfaceCreateView(CreateView):
    model = NetworkInterface
    form_class = NetworkInterfaceForm
    template_name = 'network/network_interface_form.html'
    success_url = reverse_lazy('base:network_interface-list')
class NetworkInterfaceUpdateView(UpdateView):
    model = NetworkInterface
    form_class = NetworkInterfaceUpdateForm
    template_name = 'network/network_interface_form.html'
    success_url = reverse_lazy('base:network_interface-list')
class NetworkInterfaceDeleteView(DeleteView):
    model = NetworkInterface
    template_name = 'network/network_interface_confirm_delete.html'
    success_url = reverse_lazy('base:network_interface-list')

class IpAdressListView(ListView):
    model = IpAdress
    template_name = 'network/ip_adress_list.html'
    context_object_name = 'ip_adresses'

class IpAdressDetailView(DetailView):
    model = IpAdress
    template_name = 'network/ip_adress_detail.html'
    context_object_name = 'ip_adress'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = IpAdressSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class IpAdressCreateView(CreateView):
    model = IpAdress
    form_class = IpAdressForm
    template_name = 'network/ip_adress_form.html'
    success_url = reverse_lazy('base:ip_adress-list')
class IpAdressUpdateView(UpdateView):
    model = IpAdress
    form_class = IpAdressUpdateForm
    template_name = 'network/ip_adress_form.html'
    success_url = reverse_lazy('base:ip_adress-list')

class IpAdressDeleteView(DeleteView):
    model = IpAdress
    template_name = 'network/ip_adress_confirm_delete.html'
    success_url = reverse_lazy('base:ip_adress-list')

#######################END NETWORKING VIEWS###################################
############# START APPLICATION MODULE VIEWS ###############################


class DepartementListView(ListView):
    model = Departement
    template_name = 'application/departement_list.html'
    context_object_name = 'departements'

class DepartementDetailView(DetailView):
    model = Departement
    template_name = 'application/departement_detail.html'
    context_object_name = 'departement'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DepartementSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class DepartementCreateView(CreateView):
    model = Departement
    form_class = DepartementForm
    template_name = 'application/departement_form.html'
    success_url = reverse_lazy('base:departement-list')
class DepartementUpdateView(UpdateView):
    model = Departement
    form_class = DepartementUpdateForm
    template_name = 'application/departement_form.html'
    success_url = reverse_lazy('base:departement-list')
class DepartementDeleteView(DeleteView):
    model = Departement
    template_name = 'application/departement_confirm_delete.html'
    success_url = reverse_lazy('base:departement-list')

class AppTypeListView(ListView):
    model = AppType
    template_name = 'application/apptype_list.html'
    context_object_name = 'apptypes'

class AppTypeDetailView(DetailView):
    model = AppType
    template_name = 'application/apptype_detail.html'
    context_object_name = 'apptype'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = AppTypeSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context


class AppTypeCreateView(CreateView):
    model = AppType
    form_class = AppTypeForm
    template_name = 'application/apptype_form.html'
    success_url = reverse_lazy('base:apptype-list')
class AppTypeUpdateView(UpdateView):
    model = AppType
    form_class = AppTypeUpdateForm
    template_name = 'application/apptype_form.html'
    success_url = reverse_lazy('base:apptype-list')

class AppTypeDeleteView(DeleteView):
    model = AppType
    template_name = 'application/apptype_confirm_delete.html'
    success_url = reverse_lazy('base:apptype-list')


class VendorListView(ListView):
    model = Vendor
    template_name = 'application/vendor_list.html'
    context_object_name = 'vendors'
    def get(self, request, *args, **kwargs):
       
        
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Vendor.objects.all()

        # Vérifier le type du paramètre et trier en conséquence
        if q : 
          module_applicatif = get_object_or_404(ModuleApplicatif, name__icontains=q)
          queryset = Vendor.objects.filter(
                              Q(name__icontains=q) |
                              Q(description__icontains=q) |          
                              Q(moduleapplicatif__pk=module_applicatif.pk))
        # Passer le queryset trié au template
        
        context = {'vendors': queryset}
        return render(request, self.template_name, context)

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'application/vendor_detail.html'
    context_object_name = 'vendor'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = VendorSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            modules_applicatifs = ModuleApplicatif.objects.filter(vendor=self.object)
            applications_set = set(module.application for module in ModuleApplicatif.objects.filter(vendor=self.object))
            applications = list(applications_set)
            context['modules'] = modules_applicatifs
            context['applications'] = applications
            return context
            #    

class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'application/vendor_form.html'
    success_url = reverse_lazy('base:vendor-list')

class VendorUpdateView(UpdateView):
    model = Vendor
    form_class = VendorUpdateForm
    template_name = 'application/vendor_form.html'
    success_url = reverse_lazy('base:vendor-list')

class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'application/vendor_confirm_delete.html'
    success_url = reverse_lazy('base:vendor-list')



class ModuleApplicatifListView(ListView):
    model = ModuleApplicatif
    template_name = 'application/module_applicatif_list.html'
    context_object_name = 'module_applicatifs'

class ModuleApplicatifDetailView(DetailView):
    model = ModuleApplicatif
    template_name = 'application/module_applicatif_detail.html'
    context_object_name = 'module_applicatif'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ModuleApplicatifSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ModuleApplicatifCreateView(CreateView):
    model = ModuleApplicatif
    form_class = ModuleApplicatifForm
    template_name = 'application/module_applicatif_form.html'
    success_url = reverse_lazy('base:module_applicatif-list')
class ModuleApplicatifUpdateView(UpdateView):
    model = ModuleApplicatif
    form_class = ModuleApplicatifUpdateForm
    template_name = 'application/module_applicatif_form.html'
    success_url = reverse_lazy('base:module_applicatif-list')
class ModuleApplicatifDeleteView(DeleteView):
    model = ModuleApplicatif
    template_name = 'application/module_applicatif_confirm_delete.html'
    success_url = reverse_lazy('base:module_applicatif-list')


class ApplicationListView(View):
    template_name = 'application/application_list.html'

    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        parametre = request.GET.get('parametre')
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Application.objects.all()

        # Vérifier le type du paramètre et trier en conséquence
        if parametre:
            if parametre == 'in_house':
            # Afficher les applications liées à un objet Cluster
                queryset = queryset.filter(app_type__name=parametre)
            elif parametre == 'Vendor':
            # Afficher les applications liées à un objet Server
                queryset = queryset.filter(app_type__name=parametre)
    
            # Afficher les applications liées à un objet Server
            
        elif q : 
            if ModuleApplicatif.objects.filter(Q(name__icontains=q)| Q(departement__name__icontains=q)| Q(vendor__name__icontains=q)).exists():
                queryset = [module.application for module in ModuleApplicatif.objects.filter(Q(name__icontains=q)| Q(departement__name__icontains=q)| Q(vendor__name__icontains=q))]
            else :
                queryset = Application.objects.filter(
                                Q(name__icontains=q) |
                                Q(description__icontains=q) |          
                                Q(app_type__name__icontains=q)|
                                Q(vendor__name__icontains=q))  
        # Passer le queryset trié au template
        print(queryset)
        context = {'applications': queryset}
        return render(request, self.template_name, context)
class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'application/application_detail.html'
    context_object_name = 'application'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer l'historique de la relation many-to-many 'cluster'
        print(self.object)
        databases = []
        databases_servers = []
        application_servers = []
        modules = ModuleApplicatif.objects.filter(application=self.object)
        for module in modules:
            connexion_bd = ConnexionBD.objects.filter(module_applicatif=module)
            for con in connexion_bd:
                database = Database.objects.get(id=con.database_id)#
                print(f"base de donnée : {database}")
                if database not in databases:
                    databases.append(database)
                    if database.db_server not in databases_servers:
                        databases_servers.append(database.db_server)
            connexion_app = AppDeployment.objetcs.filter(module_applicatif=module)
            for con_app in connexion_app:
                application_servers = AppServer.objects.filter(id=con_app.app_server.id).distinct()
                print(f"base de donnée : {application_servers}")
        serializer = ApplicationSerializer(self.object)
        serializer_data=json.dumps(serializer.data)
        context['serializer_data'] = serializer_data
        context['modules'] = modules
        context['databases'] = databases
        context['db_servers'] = databases_servers
        context['app_servers'] = application_servers
        

        return context
class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'application/application_form.html'
    success_url = reverse_lazy('base:application-list')

class ApplicationUpdateView(UpdateView):
    model = Application
    form_class = ApplicationUpdateForm
    template_name = 'application/application_form.html'
    success_url = reverse_lazy('base:application-list')
  
class ApplicationDeleteView(DeleteView):
    model = Application
    template_name = 'application/application_confirm_delete.html'
    success_url = reverse_lazy('base:application-list')


############# END APPLICATION MODULE VIEWS ###############################
####################### Start INTEGRATION ############
class ProcessListView(ListView):
    model = Process
    template_name = 'integration/process_list.html'
    context_object_name = 'processes'
class ProcessDetailView(DetailView):
    model = Process
    template_name = 'integration/process_detail.html'
    context_object_name = 'process'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ProcessSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ProcessCreateView(CreateView):
    model = Process
    form_class = ProcessForm
    template_name = 'integration/process_form.html'
    success_url = reverse_lazy('base:process-list')
class ProcessUpdateView(UpdateView):
    model = Process
    form_class = ProcessUpdateForm
    template_name = 'integration/process_form.html'
    success_url = reverse_lazy('base:process-list')
class ProcessDeleteView(DeleteView):
    model = Process
    template_name = 'integration/process_confirm_delete.html'
    success_url = reverse_lazy('base:process-list')
class SubProcessListView(ListView):
    model = SubProcess
    template_name = 'integration/sub_process_list.html'
    context_object_name = 'sub_processes'
class SubProcessDetailView(DetailView):
    model = SubProcess
    template_name = 'integration/sub_process_detail.html'
    context_object_name = 'sub_process'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = SubProcessSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class SubProcessCreateView(CreateView):
    model = SubProcess
    form_class = SubProcessForm
    template_name = 'integration/sub_process_form.html'
    success_url = reverse_lazy('base:sub_process-list')
class SubProcessUpdateView(UpdateView):
    model = SubProcess
    form_class = SubProcessUpdateForm
    template_name = 'integration/sub_process_form.html'
    success_url = reverse_lazy('base:sub_process-list')
class SubProcessDeleteView(DeleteView):
    model = SubProcess
    template_name = 'integration/sub_process_confirm_delete.html'
    success_url = reverse_lazy('base:sub_process-list')
class UseCaseListView(ListView):
    model = UseCase
    template_name = 'integration/use_case_list.html'
    context_object_name = 'use_cases'
class UseCaseDetailView(DetailView):
    model = UseCase
    template_name = 'integration/use_case_detail.html'
    context_object_name = 'use_case'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = UseCaseSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class UseCaseCreateView(CreateView):
    model = UseCase
    form_class = UseCaseForm
    template_name = 'integration/use_case_form.html'
    success_url = reverse_lazy('base:use_case-list')
class UseCaseUpdateView(UpdateView):
    model = UseCase
    form_class = UseCaseUpdateForm
    template_name = 'integration/use_case_form.html'
    success_url = reverse_lazy('base:use_case-list')
class UseCaseDeleteView(DeleteView):
    model = UseCase
    template_name = 'integration/use_case_confirm_delete.html'
    success_url = reverse_lazy('base:use_case-list')
class ApiListView(ListView):
    model = Api
    template_name = 'integration/api_list.html'
    context_object_name = 'apis'
class ApiDetailView(DetailView):
    model = Api
    template_name = 'integration/api_detail.html'
    context_object_name = 'api'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ApiSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ApiCreateView(CreateView):
    model = Api
    form_class = ApiForm
    template_name = 'integration/api_form.html'
    success_url = reverse_lazy('base:api-list')
class ApiUpdateView(UpdateView):
    model = Api
    form_class = ApiUpdateForm
    template_name = 'integration/api_form.html'
    success_url = reverse_lazy('base:api-list')
class ApiDeleteView(DeleteView):
    model = Api
    template_name = 'integration/api_confirm_delete.html'
    success_url = reverse_lazy('base:api-list')
class AppelApiListView(ListView):
    model = AppelApi
    template_name = 'integration/appel_api_list.html'
    context_object_name = 'appel_apis'
class AppelApiDetailView(DetailView):
    model = AppelApi
    template_name = 'integration/appel_api_detail.html'
    context_object_name = 'appel_api'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = AppelApiSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class AppelApiCreateView(CreateView):
    model = AppelApi
    form_class = AppelApiForm
    template_name = 'integration/appel_api_form.html'
    success_url = reverse_lazy('base:appel_api-list')
class AppelApiUpdateView(UpdateView):
    model = AppelApi
    form_class = AppelApiUpdateForm
    template_name = 'integration/appel_api_form.html'
    success_url = reverse_lazy('base:appel_api-list')
class AppelApiDeleteView(DeleteView):
    model = AppelApi
    template_name = 'integration/appel_api_confirm_delete.html'
    success_url = reverse_lazy('base:appel_api-list')

#####################End INTEGRATION VIEWS#################
############# START SYSTEME MODULE VIEWS ###############################

class DatacenterListView(ListView):
    model = Datacenter
    template_name = 'systeme/datacenter_list.html'
    context_object_name = 'datacenters'
class DatacenterDetailView(DetailView):
    model = Datacenter
    template_name = 'systeme/datacenter_detail.html'
    context_object_name = 'datacenter'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DatacenterSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class DatacenterCreateView(CreateView):
    model = Datacenter
    form_class = DatacenterForm
    template_name = 'systeme/datacenter_form.html'
    success_url = reverse_lazy('base:datacenter-list')
class DatacenterUpdateView(UpdateView):
    model = Datacenter
    form_class = DatacenterUpdateForm
    template_name = 'systeme/datacenter_form.html'
    success_url = reverse_lazy('base:datacenter-list')
class DatacenterDeleteView(DeleteView):
    model = Datacenter
    template_name = 'systeme/datacenter_confirm_delete.html'
    success_url = reverse_lazy('base:datacenter-list')


class ServerRoomListView(ListView):
    model = ServerRoom
    template_name = 'systeme/server_room_list.html'
    context_object_name = 'server_rooms'

class ServerRoomDetailView(DetailView):
    model = ServerRoom
    template_name = 'systeme/server_room_detail.html'
    context_object_name = 'server_room'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ServerRoomSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ServerRoomCreateView(CreateView):
    model = ServerRoom
    form_class = ServerRoomForm
    template_name = 'systeme/server_room_form.html'
    success_url = reverse_lazy('base:server_room-list')
class ServerRoomUpdateView(UpdateView):
    model = ServerRoom
    form_class = ServerRoomUpdateForm
    template_name = 'systeme/server_room_form.html'
    success_url = reverse_lazy('base:server_room-list')

class ServerRoomDeleteView(DeleteView):
    model = ServerRoom
    template_name = 'systeme/server_room_confirm_delete.html'
    success_url = reverse_lazy('base:server_room-list')

class RackListView(ListView):
    model = Rack
    template_name = 'systeme/rack_list.html'
    context_object_name = 'racks'

class RackDetailView(DetailView):
    model = Rack
    template_name = 'systeme/rack_detail.html'
    context_object_name = 'rack'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = RackSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class RackCreateView(CreateView):
    model = Rack
    form_class = RackForm
    template_name = 'systeme/rack_form.html'
    success_url = reverse_lazy('base:rack-list')


class RackUpdateView(UpdateView):
    model = Rack
    form_class = RackUpdateForm
    template_name = 'systeme/rack_form.html'
    success_url = reverse_lazy('base:rack-list')

class ClusterListView(ListView):
    model = Cluster
    template_name = 'systeme/cluster_list.html'
    context_object_name = 'clusters'

class ClusterDetailView(DetailView):
    model = Cluster
    template_name = 'systeme/cluster_detail.html'
    context_object_name = 'cluster'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ClusterSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ClusterCreateView(CreateView):
    model = Cluster
    form_class = ClusterForm
    template_name = 'systeme/cluster_form.html'
    success_url = reverse_lazy('base:cluster-list')

class ClusterUpdateView(UpdateView):
    model = Cluster
    form_class = ClusterUpdateForm
    template_name = 'systeme/cluster_form.html'
    success_url = reverse_lazy('base:cluster-list')

class ClusterDeleteView(DeleteView):
    model = Cluster
    template_name = 'systeme/cluster_confirm_delete.html'
    success_url = reverse_lazy('base:cluster-list')
class SystemeStockageListView(ListView):
    model = SystemeStockage
    template_name = 'systeme/systeme_stockage_list.html'
    context_object_name = 'systeme_stockages'

class SystemeStockageDetailView(DetailView):
    model = SystemeStockage
    template_name = 'systeme/systeme_stockage_detail.html'
    context_object_name = 'systeme_stockage'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            partitions = Partition.objects.filter(stockage=self.object)
            serveurs_liés = [partition.serveur for partition in partitions]
            print(f"nos partitions : {partitions}")
            print(f"nos serveurs liées : {serveurs_liés}")
            serializer = SystemeStockageSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            context['partitions'] = partitions
            context['serveurs'] = serveurs_liés
            return context
            # Récupérer l'historique de la relation many-to-many 'cluster'
         
class SystemeStockageCreateView(CreateView):
    model = SystemeStockage
    form_class = SystemeStockageForm
    template_name = 'systeme/systeme_stockage_form.html'
    success_url = reverse_lazy('base:systeme_stockage-list')
class SystemeStockageUpdateView(UpdateView):
    model = SystemeStockage
    form_class = SystemeStockageUpdateForm
    template_name = 'systeme/systeme_stockage_form.html'
    success_url = reverse_lazy('base:systeme_stockage-list')

class SystemeStockageDeleteView(DeleteView):
    model = SystemeStockage
    template_name = 'systeme/systeme_stockage_confirm_delete.html'
    success_url = reverse_lazy('base:systeme_stockage-list')

class ServerListView(View):
    template_name = 'systeme/server_list.html'

    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        parametre = request.GET.get('parametre')
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Server.objects.all()

        # Vérifier le type du paramètre et trier en conséquence
        if parametre:
            if Server.objects.filter(type_server=parametre).exists():
                # Si le paramètre correspond à un type de serveur, trier par type de serveur
                queryset = queryset.filter(type_server=parametre)
            elif Rack.objects.filter(name=parametre).exists():
                # Si le paramètre est un nom de rack, trier par rack
                queryset = queryset.filter(rack__name=parametre)
            elif Datacenter.objects.filter(name=parametre).exists():
                # Si le paramètre est un nom de datacenter, trier par datacenter
                queryset = queryset.filter(rack__datacenter__name=parametre)
        elif q : 
          queryset = Server.objects.filter(
                              Q(name__icontains=q) |
                              Q(rack__name__icontains=q) |          
                              Q(rack__server_room__name__icontains=q)|
                              Q(rack__server_room__datacenter__localisation__icontains=q)|
                              Q(type_server__icontains=q)|
                              Q(sys_stockage__name__icontains=q))  
        # Passer le queryset trié au template
        context = {'servers': queryset}
        return render(request, self.template_name, context)

class ServerDetailView(DetailView):
    model = Server
    template_name = 'systeme/server_detail.html'
    context_object_name = 'server'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer l'historique de la relation many-to-many 'cluster'
        print(self.object)
        serializer = ServerSerializer(self.object)
        serializer_data=json.dumps(serializer.data)
        context['serializer_data'] = serializer_data
        partitions = self.object.sys_stockage.all()
        #clusters = self.object.cluster.all()
        context['partitions'] = partitions
        #context['clusters'] = clusters
        
        print(f"les partitions : {partitions}")
        #print(f"les clusters : {clusters}")
        
        return context

class ServerCreateView(CreateView):
    model = Server
    form_class = ServerForm
    template_name = 'systeme/server_form.html'
    success_url = reverse_lazy('base:server-list')


class ServerUpdateView(UpdateView):
    model = Server
    form_class = ServerUpdateForm
    template_name = 'systeme/server_form.html'
    success_url = reverse_lazy('base:server-list')
  
class ServerDeleteView(DeleteView):
    model = Server
    template_name = 'systeme/server_confirm_delete.html'
    success_url = reverse_lazy('base:server-list')

class DeploiementClusterListView(ListView):
    model = DeploiementCluster
    template_name = 'systeme/deploiement_cluster_list.html'
    context_object_name = 'deploiement_clusters'
class DeploiementClusterDetailView(DetailView):
    model = DeploiementCluster
    template_name = 'systeme/deploiement_cluster_detail.html'
    context_object_name = 'deploiement_cluster'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DeploiementClusterSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class DeploiementClusterCreateView(CreateView):
    model = DeploiementCluster
    form_class = DeploiementClusterForm
    template_name = 'systeme/deploiement_cluster_form.html'
    success_url = reverse_lazy('base:deploiement_cluster-list')
class DeploiementClusterUpdateView(UpdateView):
    model = DeploiementCluster
    form_class = DeploiementClusterUpdateForm
    template_name = 'systeme/deploiement_cluster_form.html'
    success_url = reverse_lazy('base:deploiement_cluster-list')
class DeploiementClusterDeleteView(DeleteView):
    model = DeploiementCluster
    template_name = 'systeme/deploiement_cluster_confirm_delete.html'
    success_url = reverse_lazy('base:deploiement_cluster-list')


class PartitionListView(View):
    template_name = 'systeme/partition_list.html'

    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        parametre = request.GET.get('parametre')
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Partition.objects.all()

        # Vérifier le type du paramètre et trier en conséquence
        if parametre:
            if Server.objects.filter(type_server=parametre).exists():
                # Si le paramètre correspond à un type de serveur, trier par type de serveur
                queryset = queryset.filter(type_server=parametre)
            elif Rack.objects.filter(name=parametre).exists():
                # Si le paramètre est un nom de rack, trier par rack
                queryset = queryset.filter(rack__name=parametre)
            elif Datacenter.objects.filter(name=parametre).exists():
                # Si le paramètre est un nom de datacenter, trier par datacenter
                queryset = queryset.filter(rack__datacenter__name=parametre)
        elif q : 
          queryset = Partition.objects.filter(
                              Q(serveur__name__icontains=q) |
                              Q(serveur__rack__name__icontains=q) |          
                              Q(serveur__rack__server_room__name__icontains=q)|
                              Q(serveur__rack__server_room__datacenter__localisation__icontains=q)|
                              Q(serveur__type_server__icontains=q)|
                              Q(stockage__name__icontains=q))  # Ajout pour filtrer par nom de système de stockage
                                
        # Passer le queryset trié au template
        context = {'partitions': queryset}
        return render(request, self.template_name, context)
class PartitionDetailView(DetailView):
    model = Partition
    template_name = 'systeme/partition_detail.html'
    context_object_name = 'partition'  
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = PartitionSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class PartitionCreateView(CreateView):
    model = Partition
    form_class = PartitionForm
    template_name = 'systeme/partition_form.html'
    success_url = reverse_lazy('base:partition-list')
class PartitionUpdateView(UpdateView):
    model = Partition
    form_class = PartitionUpdateForm
    template_name = 'systeme/partition_form.html'
    success_url = reverse_lazy('base:partition-list')
class PartitionDeleteView(DeleteView):
    model = Partition
    template_name = 'systeme/partition_confirm_delete.html'
    success_url = reverse_lazy('base:partition-list')

class DatabaseServerListView(View):
    template_name = 'systeme/database_server_list.html'

    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        parametre = request.GET.get('parametre')
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = DatabaseServer.objects.all()

        # Vérifier le type du paramètre et trier en conséquence
        if parametre:
          if parametre == 'cluster':
          # Afficher les databases liées à un objet Cluster
            queryset = queryset.filter(cluster__isnull=False)
          elif parametre == 'server':
          # Afficher les databases liées à un objet Server
            queryset = queryset.filter(server__isnull=False)
        elif q : 
          if Database.objects.filter(name__icontains=q).exists():
          # Si le paramètre correspond à un type de serveur, trier par type de serveur
            queryset = queryset.filter(name__icontains=q)
          else:
            queryset = DatabaseServer.objects.filter(
                              Q(server__name__icontains=q) |
                              Q(server__rack__name__icontains=q) |          
                              Q(server__rack__server_room__name__icontains=q)|
                              Q(rack__server_room__datacenter__localisation__icontains=q)|
                              Q(server__type_server__icontains=q)|
                              Q(server__sys_stockage__name__icontains=q) | 
                              Q(cluster__name__icontains=q) )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'database_servers': queryset}
        return render(request, self.template_name, context)
class DatabaseServerDetailView(DetailView):
    model = DatabaseServer
    template_name = 'systeme/database_server_detail.html'
    context_object_name = 'database_server'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer l'historique de la relation many-to-many 'cluster'
        print(self.object)
        databases = Database.objects.filter(db_server=self.object)
        modules_lies = []
        for db in databases:
            for conDB in ConnexionBD.objects.filter(database=db):
                if conDB.module_applicatif not in modules_lies:
                    modules_lies.append(conDB.module_applicatif) 
        serializer = DatabaseServerSerializer(self.object)
        serializer_data=json.dumps(serializer.data)
        context['serializer_data'] = serializer_data
        context['databases'] = databases
        context['modules'] = modules_lies
        
            
        
        return context
class DatabaseServerCreateView(CreateView):
    model = DatabaseServer
    form_class = DatabaseServerForm
    template_name = 'systeme/database_server_form.html'
    success_url = reverse_lazy('base:database_server-list')
class DatabaseServerUpdateView(UpdateView):
    model = DatabaseServer
    form_class = DatabaseServerUpdateForm
    template_name = 'systeme/database_server_form.html'
    success_url = reverse_lazy('base:database_server-list')
class DatabaseServerDeleteView(DeleteView):
    model = DatabaseServer
    template_name = 'systeme/database_server_confirm_delete.html'
    success_url = reverse_lazy('base:database_server-list')


class DatabaseListView(View):
    template_name = 'systeme/database_list.html'

    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        parametre = request.GET.get('parametre')
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Database.objects.all()

        # Vérifier le type du paramètre et trier en conséquence
        if parametre:
          if parametre == 'Oracle':
          # Afficher les databases liées à un objet Cluster
            queryset = queryset.filter(name__icontains=parametre)
          elif parametre == 'MySQL':
          # Afficher les databases liées à un objet Server
            queryset = queryset.filter(name__icontains=parametre)
          elif parametre == 'SqlServer':
          # Afficher les databases liées à un objet Server
            queryset = queryset.filter(name__icontains=parametre)
          elif parametre == 'PostgreSQL':
          # Afficher les databases liées à un objet Server
            queryset = queryset.filter(name__icontains=parametre)
        elif q : 

          queryset = Database.objects.filter(
                            Q(db_server__server__name__icontains=q) |
                            Q(db_server__server__rack__name__icontains=q) |          
                            Q(db_server__server__rack__server_room__name__icontains=q)|
                            Q(db_server__rack__server_room__datacenter__localisation__icontains=q)|
                            Q(db_server__server__type_server__icontains=q)|
                            Q(db_server__server__sys_stockage__name__icontains=q) | 
                            Q(name__icontains=q) |
                            Q(db_server__name__icontains=q) |  # Ajout pour filtrer par nom de système de stockage
                            
                            Q(module_applicatifs__name__icontains=q)|
                            Q(module_applicatifs__application__name__icontains=q))  
        # Passer le queryset trié au template
        print(queryset)
        context = {'databases': queryset}
        return render(request, self.template_name, context)
class DatabaseDetailView(DetailView):
    model = Database
    template_name = 'systeme/database_detail.html'
    context_object_name = 'database'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Récupérer l'historique de la relation many-to-many 'cluster'
        print(self.object)
        applications_lies = []
        for module in self.object.module_applicatifs.all():
            application = module.application
            if application not in applications_lies:
                applications_lies.append(application)

        
        serializer = DatabaseSerializer(self.object)
        serializer_data=json.dumps(serializer.data)
        context['serializer_data'] = serializer_data      
        context['applications'] = applications_lies
        return context
class DatabaseCreateView(CreateView):
    model = Database
    form_class = DatabaseForm
    template_name = 'systeme/database_form.html'
    success_url = reverse_lazy('base:database-list')

class DatabaseUpdateView(UpdateView):
    model = Database
    form_class = DatabaseUpdateForm
    template_name = 'systeme/database_form.html'
    success_url = reverse_lazy('base:database-list')
  
class DatabaseDeleteView(DeleteView):
    model = Database
    template_name = 'systeme/database_confirm_delete.html'
    success_url = reverse_lazy('base:database-list')

############# END SYSTEME MODULE VIEWS ###############################



def departementApi(request, departement_id):
    departement = Departement.objects.get(id=departement_id) 
    data = {
        "nom": {
            "value": departement.name,
            "url": reverse('base:departement-api', args=[departement.pk]),
            "icon":"mdi mdi-desktop-tower",
        },
        "description": {"value": departement.description, "url": "#","icon":"mdi mdi-desktop-tower",},
        "created": {"value": departement.created, "url": "#","icon":"mdi mdi-desktop-tower",},
        "updated": {"value": departement.updated, "url": "#","icon":"mdi mdi-desktop-tower",},
    }
    return JsonResponse(data)


def serverRoomApi(request,id):

    server_room = ServerRoom.objects.get(pk=id)
    serializer = ServerRoomSerializer(server_room)
    return Response(serializer.data)
# views.py


class serverRoomApiView(APIView):
    def get(self, request, id):
        try:
            server_room = ServerRoom.objects.get(pk=id)
            serializer = ServerRoomSerializer(server_room)
            return Response(serializer.data)
        except ServerRoom.DoesNotExist:
            return Response({"error": "ServerRoom not found"}, status=status.HTTP_404_NOT_FOUND)

class DatacenterApiView(APIView):
    def get(self, request, id):
        try:
            server_room = Datacenter.objects.get(pk=id)
            serializer = DatacenterSerializer(server_room)
            return Response(serializer.data)
        except ServerRoom.DoesNotExist:
            return Response({"error": "ServerRoom not found"}, status=status.HTTP_404_NOT_FOUND)

def home(request):
    server = Server.objects.get(pk=1)
    serializer = ServerSerializer(server)
    print(serializer.data)
    serializer_data=json.dumps(serializer.data)
    #print(serializer_data)
    context={"serializer_data":serializer_data}
    return render(request, 'application/test2.html',context)  


