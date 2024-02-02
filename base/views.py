from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
import json
from base.forms import DesktopAppCreateForm,DesktopAppUpdateForm,MobileAppCreateForm,MobileAppUpdateForm,ConnexionAppCreateForm,ConnexionAppUpdateForm,UrlCreateForm,UrlUpdateForm,SmppAccountCreateForm,SmppAccountUpdateForm,SmsShortCodeCreateForm,SmsShortCodeUpdateForm,UssdShortCodeCreateForm,UssdShortCodeUpdateForm,DomainNameCreateForm,DomainNameUpdateForm,DataDictionnaryUpdateForm,DataDictionnaryCreateForm,DataDictionnaryModelCreateForm,DataDictionnaryModelUpdateForm,ApiSpecificationCreateForm,ApiSpecificationUpdateForm,BackupStrategieUpdateForm,BackupStrategieCreateForm,TechnicalRecoveryPlanCreateForm,TechnicalRecoveryPlanUpdateForm,ArchitectureDiagramCreateForm,ArchitectureDiagramUpdateForm,ApiDocumentationCreateForm,ApiDocumentationUpdateForm,CallFlowCreateForm,CallFlowUpdateForm,DataModelUpdateForm,DataModelCreateForm
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from base.models import ApiSpecification,ArchitectureDiagram,TechnicalRecoveryPlan,DataDictionnary,ApiDocumentation, BackupStrategie,ConnexionBD,Process,SubProcess,UseCase,Api,AppelApi,ServerRoom,Server,IpAdress,SystemeStockage,Datacenter,Departement,DeploiementCluster,Application,AppType,ModuleApplicatif,Vendor,Cluster,Rack,DatabaseServer,Database,DataDictionnary,DataDictionnaryModel,DataModel,DesktopApp,DomainName,NetworkInterface,Notifications,ConnexionBD,AppDeployment,AppServer
from accounts.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ConnexionApp, Departement,Partition,CallFlow,MobileApp, SmppAccount, SmsShortCode,Url, UssdShortCode
from django.views import View
from django.db.models import Q
from base.serializers import DomainNameSerializer,DataDictionnaryModelSerializer,DataDictionnarySerializer,ApiSpecificationSerializer,CallFlowSerializer,ArchitectureDiagramSerializer,ApiDocumentationSerializer,TechnicalRecoveryPlanSerializer,ConnexionBDSerializer,AppServerSerializer,AppelApiSerializer,ApiSerializer,UseCaseSerializer,ProcessSerializer,SubProcessSerializer,DataModelSerializer,DatacenterSerializer,ServerRoomSerializer,DepartementSerializer,DatabaseSerializer,DatabaseServerSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import ConnexionBDForm,ConnexionBDUpdateForm,AppServerForm,AppServerUpdateForm,ProcessForm,UseCaseUpdateForm,UseCaseForm,SubProcessForm,AppelApiForm,ApiForm,ApiUpdateForm,SubProcessUpdateForm,ProcessUpdateForm,AppelApiUpdateForm,IpAdressForm,IpAdressUpdateForm,NetworkInterfaceForm,NetworkInterfaceUpdateForm,DepartementForm,DepartementUpdateForm,AppTypeForm,AppTypeUpdateForm,DatacenterForm,DatacenterUpdateForm,ServerRoomForm,ServerRoomUpdateForm,RackForm,RackUpdateForm,ClusterForm,ClusterUpdateForm,SystemeStockageForm,SystemeStockageUpdateForm,ServerForm,ServerUpdateForm,DeploiementClusterUpdateForm,DeploiementClusterForm,PartitionForm,PartitionUpdateForm,DatabaseServerForm,DatabaseServerUpdateForm,DatabaseForm,DatabaseUpdateForm,VendorUpdateForm,VendorForm,ApplicationForm,ApplicationUpdateForm,ModuleApplicatifForm,ModuleApplicatifUpdateForm
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServerRoom
from .serializers import ConnexionAppSerializer, DesktopAppSerializer, MobileAppSerializer, ServerRoomSerializer,NetworkInterfaceSerializer,IpAdressSerializer,ServerSerializer, SmppAccountSerializer, SmsShortCodeSerializer, UrlSerializer, UssdShortCodeSerializer,VendorSerializer,DatacenterSerializer,DepartementSerializer,DeploiementClusterSerializer,PartitionSerializer,ClusterSerializer,SystemeStockageSerializer,ApplicationSerializer,ModuleApplicatifSerializer,AppTypeSerializer,RackSerializer,BackupStrategieSerializer
from django.http import FileResponse
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin

def pdf_view(request,id,type_file):
    if type_file == 'backup':
        file = BackupStrategie.objects.get(pk=id)
    elif type_file == 'technical-plan':
        file = TechnicalRecoveryPlan.objects.get(pk=id)
    elif type_file == 'achitecture-diagram':
        file = ArchitectureDiagram.objects.get(pk=id)
    elif type_file == 'call-flow':
        file = CallFlow.objects.get(pk=id)
    elif type_file == 'api-documentation':
        file = ApiDocumentation.objects.get(pk=id)
    elif type_file == 'api-specification':
        file = ApiSpecification.objects.get(pk=id)
    elif type_file == 'data-dictionnary':
        file = DataDictionnary.objects.get(pk=id)
    elif type_file == 'data-model':
        file = DataModel.objects.get(pk=id)
    
    print(id)
    file_path = file.file.path
    print(f'test : {file_path}')
    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
        return response
    




@login_required
def index(request):
    user = User.objects.get(email=request.user.email,username=request.user.username)
    if user.is_superuser :
        return render(request, 'accounts/index.html')
    else:
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
##############################"CHANNELS###################################"
class MobileAppListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_denied_message =  "Vous n'avez pas la permission d'accéder à cette page. Veuillez contacter votre administrateur"
    permission_required = "base.view_mobileapp"

    model = MobileApp
    template_name = 'channels/mobile_app_list.html'
    context_object_name = 'mobile_apps'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = MobileApp.objects.all()
        if q :
          queryset = MobileApp.objects.filter(
                            Q(name__icontains=q)
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'mobile_apps': queryset}
        return render(request, self.template_name, context)

class MobileAppDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = 'app.view_mobileapp'
    model = MobileApp
    template_name = 'channels/mobile_app_detail.html'
    context_object_name = 'mobile_app'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = MobileAppSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class MobileAppCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_mobileapp"
    model = MobileApp
    template_name = 'channels/mobile_app_form.html'
    form_class = MobileAppCreateForm
    success_url = reverse_lazy('base:mobile_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class MobileAppUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_mobileapp"
    model = MobileApp
    template_name = 'channels/mobile_app_form.html'
    form_class = MobileAppUpdateForm
    success_url = reverse_lazy('base:mobile_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class MobileAppDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_mobileapp"
    model = MobileApp
    template_name = 'channels/mobile_app_confirm_delete.html'
    success_url = reverse_lazy('mobile_app-list')

class DesktopAppListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_desktopapp"
    model = DesktopApp
    template_name = 'channels/desktop_app_list.html'
    context_object_name = 'desktop_apps'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = DesktopApp.objects.all()
        if q :
          queryset = DesktopApp.objects.filter(
                            Q(name__icontains=q)
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'desktop_apps': queryset}
        return render(request, self.template_name, context)

class DesktopAppDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_desktopapp"
    model = DesktopApp
    template_name = 'channels/desktop_app_detail.html'
    context_object_name = 'desktop_app'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DesktopAppSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class DesktopAppCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_desktopapp"
    model = DesktopApp
    template_name = 'channels/desktop_app_form.html'
    form_class = DesktopAppCreateForm
    success_url = reverse_lazy('base:desktop_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DesktopAppUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_desktopapp"
    model = DesktopApp
    template_name = 'channels/desktop_app_form.html'
    form_class = DesktopAppUpdateForm
    success_url = reverse_lazy('base:desktop_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DesktopAppDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_desktopapp"
    model = DesktopApp
    template_name = 'channels/desktop_app_confirm_delete.html'
    success_url = reverse_lazy('desktop_app-list')

class UrlListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_url"
    model = Url
    template_name = 'channels/url_list.html'
    context_object_name = 'urls'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Url.objects.all()
        if q :
          queryset = Url.objects.filter(
                            Q(name__icontains=q)|
                            Q(module_applicatif__name__icontains=q)|
                            Q(module_applicatif__name__icontains=q)|
                            Q(module_applicatif__application__name__icontains=q)|
                            Q(domain_name__name__icontains=q)|
                            Q(domain_name__ip_address__ipv4__icontains=q)
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'urls': queryset}
        return render(request, self.template_name, context)

class UrlDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_url"
    model = Url
    template_name = 'channels/url_detail.html'
    context_object_name = 'url'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = UrlSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class UrlCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_url"
    model = Url
    template_name = 'channels/url_form.html'
    form_class = UrlCreateForm
    success_url = reverse_lazy('base:url-list')
    def form_valid(self, form):
        return super().form_valid(form)

class UrlUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_url"
    model = Url
    template_name = 'channels/url_form.html'
    form_class = UrlUpdateForm
    success_url = reverse_lazy('base:url-list')
    def form_valid(self, form):
        return super().form_valid(form)

class UrlDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_url"
    model = Url
    template_name = 'channels/url_confirm_delete.html'
    success_url = reverse_lazy('url-list')

class SmppAccountListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_smppaccount"
    model = SmppAccount
    template_name = 'channels/smpp_account_list.html'
    context_object_name = 'smpp_accounts'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = SmppAccount.objects.all()
        if q :
          queryset = SmppAccount.objects.filter(
                            Q(name__icontains=q)|
                            Q(module_applicatif__name__icontains=q)|
                            Q(module_applicatif__name__icontains=q)|
                            Q(module_applicatif__application__name__icontains=q)|
                            Q(module_applicatif__application__name__icontains=q)| 
                            Q(sms_short_codes__code__icontains=q)   
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'smpp_accounts': queryset}
        return render(request, self.template_name, context)

class SmppAccountDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_smppaccount"
    model = SmppAccount
    template_name = 'channels/smpp_account_detail.html'
    context_object_name = 'smpp_account'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = SmppAccountSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class SmppAccountCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_smppaccount"
    model = SmppAccount
    template_name = 'channels/smpp_account_form.html'
    form_class = SmppAccountCreateForm
    success_smpp_account = reverse_lazy('base:smpp_account-list')
    def form_valid(self, form):
        return super().form_valid(form)

class SmppAccountUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_smppaccount"
    model = SmppAccount
    template_name = 'channels/smpp_account_form.html'
    form_class = SmppAccountUpdateForm
    success_smpp_account = reverse_lazy('base:smpp_account-list')
    def form_valid(self, form):
        return super().form_valid(form)

class SmppAccountDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_smppaccount"
    model = SmppAccount
    template_name = 'channels/smpp_account_confirm_delete.html'
    success_smpp_account = reverse_lazy('smpp_account-list')

class SmsShortCodeListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_smsshortcode"
    model = SmsShortCode
    template_name = 'channels/sms_short_code_list.html'
    context_object_name = 'sms_short_codes'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = SmsShortCode.objects.all()
        if q :
          queryset = SmsShortCode.objects.filter(
                            Q(name__icontains=q)|
                            Q(smpp_account__module_applicatif__name__icontains=q)|
                            Q(smpp_account__module_applicatif__name__icontains=q)|
                            Q(smpp_account__module_applicatif__application__name__icontains=q) |
                            Q(code__icontains=q)     
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'sms_short_codes': queryset}
        return render(request, self.template_name, context)

class SmsShortCodeDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_smsshortcode"
    model = SmsShortCode
    template_name = 'channels/sms_short_code_detail.html'
    context_object_name = 'sms_short_code'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = SmsShortCodeSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class SmsShortCodeCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_smsshortcode"
    model = SmsShortCode
    template_name = 'channels/sms_short_code_form.html'
    form_class = SmsShortCodeCreateForm
    success_sms_short_code = reverse_lazy('base:sms_short_code-list')
    def form_valid(self, form):
        return super().form_valid(form)

class SmsShortCodeUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_smsshortcode"
    model = SmsShortCode
    template_name = 'channels/sms_short_code_form.html'
    form_class = SmsShortCodeUpdateForm
    success_sms_short_code = reverse_lazy('base:sms_short_code-list')
    def form_valid(self, form):
        return super().form_valid(form)

class SmsShortCodeDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_smsshortcode"
    model = SmsShortCode
    template_name = 'channels/sms_short_code_confirm_delete.html'
    success_sms_short_code = reverse_lazy('sms_short_code-list')

class UssdShortCodeListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_ussdshortcode"
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_list.html'
    context_object_name = 'ussd_short_codes'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = UssdShortCode.objects.all()
        if q :
          queryset = UssdShortCode.objects.filter(
                            Q(name__icontains=q)|
                            Q(url__module_applicatif__name__icontains=q)|
                            Q(url__module_applicatif__name__icontains=q)|
                            Q(url__module_applicatif__application__name__icontains=q) |
                            Q(code__icontains=q)  |
                            Q(url__module_applicatif__application__description__icontains=q)  
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'ussd_short_codes': queryset}
        return render(request, self.template_name, context)

class UssdShortCodeDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_ussdshortcode"
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_detail.html'
    context_object_name = 'ussd_short_code'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = UssdShortCodeSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class UssdShortCodeCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_ussdshortcode"
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_form.html'
    form_class = UssdShortCodeCreateForm
    success_ussd_short_code = reverse_lazy('base:ussd_short_code-list')
    def form_valid(self, form):
        return super().form_valid(form)

class UssdShortCodeUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_ussdshortcode"
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_form.html'
    form_class = UssdShortCodeUpdateForm
    success_ussd_short_code = reverse_lazy('base:ussd_short_code-list')
    def form_valid(self, form):
        return super().form_valid(form)

class UssdShortCodeDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_ussdshortcode"
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_confirm_delete.html'
    success_ussd_short_code = reverse_lazy('ussd_short_code-list')

class ConnexionAppListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_connexionapp"
    model = ConnexionApp
    template_name = 'channels/connexion_app_list.html'
    context_object_name = 'connexion_apps'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = ConnexionApp.objects.all()
        if q :
          queryset = ConnexionApp.objects.filter(
                            
                            Q(url__module_applicatif__name__icontains=q)|
                            Q(url__module_applicatif__name__icontains=q)|
                            Q(url__module_applicatif__application__name__icontains=q) |
                           
                            Q(url__module_applicatif__application__description__icontains=q)  
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'connexion_apps': queryset}
        return render(request, self.template_name, context)

class ConnexionAppDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_connexionapp"
    model = ConnexionApp
    template_name = 'channels/connexion_app_detail.html'
    context_object_name = 'connexion_app'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ConnexionAppSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class ConnexionAppCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_connexionapp"
    model = ConnexionApp
    template_name = 'channels/connexion_app_form.html'
    form_class = ConnexionAppCreateForm
    success_connexion_app = reverse_lazy('base:connexion_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ConnexionAppUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_connexionapp"
    model = ConnexionApp
    template_name = 'channels/connexion_app_form.html'
    form_class = ConnexionAppUpdateForm
    success_connexion_app = reverse_lazy('base:connexion_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ConnexionAppDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_connexionapp"
    model = ConnexionApp
    template_name = 'channels/connexion_app_confirm_delete.html'
    success_connexion_app = reverse_lazy('connexion_app-list')

#################################end Channels views############################################

#################################end Channels views############################################
######################Networking views#############
class DomainNameListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_domainname"
    model = DomainName
    template_name = 'documentation/domain_name_list.html'
    context_object_name = 'data_dictionnaries'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = DomainName.objects.all()
        if q :
          queryset = DomainName.objects.filter(
                            Q(name__icontains=q) |
                            Q(urls__name__icontains=q) |          
                            Q(urls__module_applicatif__name__icontains=q) |   
                            Q(urls__module_applicatif__application__name__icontains=q) |  
                            Q(ip_adress__name__icontains=q)|
                            Q(ip_adress__ipv4__icontains=q)    
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'domain_names': queryset}
        return render(request, self.template_name, context)

class DomainNameDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_domainname"
    model = DomainName
    template_name = 'documentation/domain_name_detail.html'
    context_object_name = 'domain_name'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DomainNameSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class DomainNameCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_domainname"
    model = DomainName
    template_name = 'documentation/domain_name_form.html'
    form_class = DomainNameCreateForm
    success_url = reverse_lazy('base:domain_name-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DomainNameUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_domainname"
    model = DomainName
    template_name = 'documentation/domain_name_form.html'
    form_class = DomainNameUpdateForm
    success_url = reverse_lazy('base:domain_name-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DomainNameDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_domainname"
    model = DomainName
    template_name = 'documentation/domain_name_confirm_delete.html'
    success_url = reverse_lazy('domain_name-list')

class NetworkInterfaceListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_networkinterface"
    model = NetworkInterface
    template_name = 'network/network_interface_list.html'
    context_object_name = 'network_interfaces'

class NetworkInterfaceDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_networkinterface"
    model = NetworkInterface
    template_name = 'network/network_interface_detail.html'
    context_object_name = 'network_interface'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = NetworkInterfaceSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class NetworkInterfaceCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_networkinterface"
    model = NetworkInterface
    form_class = NetworkInterfaceForm
    template_name = 'network/network_interface_form.html'
    success_url = reverse_lazy('base:network_interface-list')
class NetworkInterfaceUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_networkinterface"
    model = NetworkInterface
    form_class = NetworkInterfaceUpdateForm
    template_name = 'network/network_interface_form.html'
    success_url = reverse_lazy('base:network_interface-list')
class NetworkInterfaceDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_networkinterface"
    model = NetworkInterface
    template_name = 'network/network_interface_confirm_delete.html'
    success_url = reverse_lazy('base:network_interface-list')

class IpAdressListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_ipadress"
    permission_denied_message = "Vous ne disposez pas des permissions requises pour acceder à cette vue.  Merci de contacter votre administrateur."
    model = IpAdress
    template_name = 'network/ip_adress_list.html'
    context_object_name = 'ip_adresses'


class IpAdressDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_ipadress"
    model = IpAdress
    template_name = 'network/ip_adress_detail.html'
    context_object_name = 'ip_adress'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = IpAdressSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class IpAdressCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_ipadress"
    model = IpAdress
    form_class = IpAdressForm
    template_name = 'network/ip_adress_form.html'
    success_url = reverse_lazy('base:ip_adress-list')
class IpAdressUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_ipadress"
    model = IpAdress
    form_class = IpAdressUpdateForm
    template_name = 'network/ip_adress_form.html'
    success_url = reverse_lazy('base:ip_adress-list')

class IpAdressDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_ipadress"
    model = IpAdress
    template_name = 'network/ip_adress_confirm_delete.html'
    success_url = reverse_lazy('base:ip_adress-list')

#######################END NETWORKING VIEWS###################################
############# START APPLICATION MODULE VIEWS ###############################


class DepartementListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_departement"
    model = Departement
    template_name = 'application/departement_list.html'
    context_object_name = 'departements'

class DepartementDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_departement"
    model = Departement
    template_name = 'application/departement_detail.html'
    context_object_name = 'departement'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DepartementSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class DepartementCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_departement"
    model = Departement
    form_class = DepartementForm
    template_name = 'application/departement_form.html'
    success_url = reverse_lazy('base:departement-list')
class DepartementUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_departement"
    model = Departement
    form_class = DepartementUpdateForm
    template_name = 'application/departement_form.html'
    success_url = reverse_lazy('base:departement-list')
class DepartementDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_departement"
    model = Departement
    template_name = 'application/departement_confirm_delete.html'
    success_url = reverse_lazy('base:departement-list')

class AppTypeListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_apptype"
    model = AppType
    template_name = 'application/apptype_list.html'
    context_object_name = 'apptypes'

class AppTypeDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_apptype"
    model = AppType
    template_name = 'application/apptype_detail.html'
    context_object_name = 'apptype'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = AppTypeSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context


class AppTypeCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_apptype"
    model = AppType
    form_class = AppTypeForm
    template_name = 'application/apptype_form.html'
    success_url = reverse_lazy('base:apptype-list')
class AppTypeUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_apptype"
    model = AppType
    form_class = AppTypeUpdateForm
    template_name = 'application/apptype_form.html'
    success_url = reverse_lazy('base:apptype-list')

class AppTypeDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_apptype"
    model = AppType
    template_name = 'application/apptype_confirm_delete.html'
    success_url = reverse_lazy('base:apptype-list')


class VendorListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_vendor"
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


class VendorDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_vendor"
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


class VendorCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_vendor"
    model = Vendor
    form_class = VendorForm
    template_name = 'application/vendor_form.html'
    success_url = reverse_lazy('base:vendor-list')

class VendorUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_vendor"
    model = Vendor
    form_class = VendorUpdateForm
    template_name = 'application/vendor_form.html'
    success_url = reverse_lazy('base:vendor-list')

class VendorDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_vendor"
    model = Vendor
    template_name = 'application/vendor_confirm_delete.html'
    success_url = reverse_lazy('base:vendor-list')

class ModuleApplicatifListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_moduleapplicatif"
    model = ModuleApplicatif
    template_name = 'application/module_applicatif_list.html'
    context_object_name = 'module_applicatifs'

class ModuleApplicatifDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_moduleapplicatif"
    model = ModuleApplicatif
    template_name = 'application/module_applicatif_detail.html'
    context_object_name = 'module_applicatif'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ModuleApplicatifSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ModuleApplicatifCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_moduleapplicatif"
    model = ModuleApplicatif
    form_class = ModuleApplicatifForm
    template_name = 'application/module_applicatif_form.html'
    success_url = reverse_lazy('base:module_applicatif-list')
class ModuleApplicatifUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_moduleapplicatif"
    model = ModuleApplicatif
    form_class = ModuleApplicatifUpdateForm
    template_name = 'application/module_applicatif_form.html'
    success_url = reverse_lazy('base:module_applicatif-list')
class ModuleApplicatifDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_moduleapplicatif"
    model = ModuleApplicatif
    template_name = 'application/module_applicatif_confirm_delete.html'
    success_url = reverse_lazy('base:module_applicatif-list')


class ApplicationListView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = "base.view_application"
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
class ApplicationDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_application"
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
            connexion_app = AppDeployment.objects.filter(module_applicatif=module)
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
class ApplicationCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_application"
    model = Application
    form_class = ApplicationForm
    template_name = 'application/application_form.html'
    success_url = reverse_lazy('base:application-list')

class ApplicationUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_application"
    model = Application
    form_class = ApplicationUpdateForm
    template_name = 'application/application_form.html'
    success_url = reverse_lazy('base:application-list')
  
class ApplicationDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_application"
    model = Application
    template_name = 'application/application_confirm_delete.html'
    success_url = reverse_lazy('base:application-list')


class AppServerListView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = "base.view_appserver"
    template_name = 'application/app_server_list.html'

    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        parametre = request.GET.get('parametre')
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = AppServer.objects.all()
        if q :  
            queryset = AppServer.objects.filter(
                            Q(name__icontains=q) |
                            Q(description__icontains=q) |          
                            Q(server__name__icontains=q)|
                            Q(module_applicatif__name__icontains=q))  
        # Passer le queryset trié au template
        print(queryset)
        context = {'app_servers': queryset}
        return render(request, self.template_name, context)
class AppServerDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_appserver"
    model = AppServer
    template_name = 'application/app_server_detail.html'
    context_object_name = 'app_server'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupérer l'historique de la relation many-to-many 'cluster'
        print(self.object)
        serializer = AppServerSerializer(self.object)
        serializer_data=json.dumps(serializer.data)
        context['serializer_data'] = serializer_data
        return context
class AppServerCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_appserver"
    model = AppServer
    form_class = AppServerForm
    template_name = 'application/app_server_form.html'
    success_url = reverse_lazy('base:app_server-list')
class AppServerUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_appserver"
    model = AppServer
    form_class = AppServerUpdateForm
    template_name = 'application/app_server_form.html'
    success_url = reverse_lazy('base:app_server-list')
  
class AppServerDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_appserver"
    model = AppServer
    template_name = 'application/app_server_confirm_delete.html'
    success_url = reverse_lazy('base:app_server-list')


class ConnexionBDListView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = "base.view_connexionbd"
    template_name = 'application/connexion_bd_list.html'

    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        parametre = request.GET.get('parametre')
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = ConnexionBD.objects.all()

        # Vérifier le type du paramètre et trier en conséquence
        
        if q : 
          queryset = ConnexionBD.objects.filter(
                              Q(module_applicatif__name__icontains=q) |
                              Q(module_applicatif__application__name__icontains=q) |          
                              Q(database__db_server__rack__server_room__name__icontains=q)|
                              Q(database__db_server__rack__server_room__datacenter__localisation__icontains=q)|
                              Q(database__db_server__type_server__icontains=q)|
                              Q(database__name__icontains=q))  # Ajout pour filtrer par nom de système de stockage
                                
        # Passer le queryset trié au template
        context = {'connexion_bds': queryset}
        return render(request, 'application/connexion_bd_list.html', context)
    

class ConnexionBDDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_connexionbd"
    model = ConnexionBD
    template_name = 'application/connexion_bd_detail.html'
    context_object_name = 'connexion_bd'  
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ConnexionBDSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ConnexionBDCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_connexionbd"
    model = ConnexionBD
    form_class = ConnexionBDForm
    template_name = 'application/connexion_bd_form.html'
    success_url = reverse_lazy('base:connexion_bd-list')
class ConnexionBDUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_connexionbd"
    model = ConnexionBD
    form_class = ConnexionBDUpdateForm
    template_name = 'application/connexion_bd_form.html'
    success_url = reverse_lazy('base:connexion_bd-list')
class ConnexionBDDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_connexionbd"
    model = ConnexionBD
    template_name = 'application/connexion_bd_confirm_delete.html'
    success_url = reverse_lazy('base:connexion_bd-list')


############# END APPLICATION MODULE VIEWS ###############################
####################### Start INTEGRATION ############
class ProcessListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_process"
    model = Process
    template_name = 'integration/process_list.html'
    context_object_name = 'processes'
class ProcessDetailView(DetailView):
    permission_required = "base.view_process"
    model = Process
    template_name = 'integration/process_detail.html'
    context_object_name = 'process'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ProcessSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ProcessCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_process"
    model = Process
    form_class = ProcessForm
    template_name = 'integration/process_form.html'
    success_url = reverse_lazy('base:process-list')
class ProcessUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_process"
    model = Process
    form_class = ProcessUpdateForm
    template_name = 'integration/process_form.html'
    success_url = reverse_lazy('base:process-list')
class ProcessDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_process"
    model = Process
    template_name = 'integration/process_confirm_delete.html'
    success_url = reverse_lazy('base:process-list')
class SubProcessListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_subprocess"
    model = SubProcess
    template_name = 'integration/sub_process_list.html'
    context_object_name = 'sub_processes'
class SubProcessDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_subprocess"
    model = SubProcess
    template_name = 'integration/sub_process_detail.html'
    context_object_name = 'sub_process'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = SubProcessSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class SubProcessCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_subprocess"
    model = SubProcess
    form_class = SubProcessForm
    template_name = 'integration/sub_process_form.html'
    success_url = reverse_lazy('base:sub_process-list')
class SubProcessUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_subprocess"
    model = SubProcess
    form_class = SubProcessUpdateForm
    template_name = 'integration/sub_process_form.html'
    success_url = reverse_lazy('base:sub_process-list')
class SubProcessDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_subprocess"
    model = SubProcess
    template_name = 'integration/sub_process_confirm_delete.html'
    success_url = reverse_lazy('base:sub_process-list')
class UseCaseListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_usecase"
    model = UseCase
    template_name = 'integration/use_case_list.html'
    context_object_name = 'use_cases'
class UseCaseDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_usecase"
    model = UseCase
    template_name = 'integration/use_case_detail.html'
    context_object_name = 'use_case'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = UseCaseSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class UseCaseCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_usecase"
    model = UseCase
    form_class = UseCaseForm
    template_name = 'integration/use_case_form.html'
    success_url = reverse_lazy('base:use_case-list')
class UseCaseUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_usecase"
    model = UseCase
    form_class = UseCaseUpdateForm
    template_name = 'integration/use_case_form.html'
    success_url = reverse_lazy('base:use_case-list')
class UseCaseDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_usecase"
    model = UseCase
    template_name = 'integration/use_case_confirm_delete.html'
    success_url = reverse_lazy('base:use_case-list')
class ApiListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_api"
    model = Api
    template_name = 'integration/api_list.html'
    context_object_name = 'apis'
class ApiDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_api"
    model = Api
    template_name = 'integration/api_detail.html'
    context_object_name = 'api'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ApiSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ApiCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_api"
    model = Api
    form_class = ApiForm
    template_name = 'integration/api_form.html'
    success_url = reverse_lazy('base:api-list')
class ApiUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_api"
    model = Api
    form_class = ApiUpdateForm
    template_name = 'integration/api_form.html'
    success_url = reverse_lazy('base:api-list')
class ApiDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_api"
    model = Api
    template_name = 'integration/api_confirm_delete.html'
    success_url = reverse_lazy('base:api-list')
class AppelApiListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_appelapi"
    model = AppelApi
    template_name = 'integration/appel_api_list.html'
    context_object_name = 'appel_apis'
class AppelApiDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_appelapi"
    model = AppelApi
    template_name = 'integration/appel_api_detail.html'
    context_object_name = 'appel_api'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = AppelApiSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class AppelApiCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_appelapi"
    model = AppelApi
    form_class = AppelApiForm
    template_name = 'integration/appel_api_form.html'
    success_url = reverse_lazy('base:appel_api-list')
class AppelApiUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_appelapi"
    model = AppelApi
    form_class = AppelApiUpdateForm
    template_name = 'integration/appel_api_form.html'
    success_url = reverse_lazy('base:appel_api-list')
class AppelApiDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_appelapi"
    model = AppelApi
    template_name = 'integration/appel_api_confirm_delete.html'
    success_url = reverse_lazy('base:appel_api-list')

#####################End INTEGRATION VIEWS#################
############# START SYSTEME MODULE VIEWS ###############################

class DatacenterListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_datacenter"
    model = Datacenter
    template_name = 'systeme/datacenter_list.html'
    context_object_name = 'datacenters'

    def get(self, request, *args, **kwargs):  
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Datacenter.objects.all()
        # Vérifier le type du paramètre et trier en conséquence
        if q : 
          queryset = Datacenter.objects.filter(
                              Q(name__icontains=q) |
                              Q(servers_rooms__name__icontains=q) |          
                              Q(servers_rooms__racks__name__icontains=q)|
                              Q(servers_rooms__racks__servers__name__icontains=q)).distinct().order_by('created')
                              
        # Passer le queryset trié au template
        context = {'datacenters': queryset}
        return render(request, self.template_name, context)


class DatacenterDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_datacenter"
    model = Datacenter
    template_name = 'systeme/datacenter_detail.html'
    context_object_name = 'datacenter'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DatacenterSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class DatacenterCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_datacenter"
    model = Datacenter
    form_class = DatacenterForm
    template_name = 'systeme/datacenter_form.html'
    success_url = reverse_lazy('base:datacenter-list')
class DatacenterUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_datacenter"
    model = Datacenter
    form_class = DatacenterUpdateForm
    template_name = 'systeme/datacenter_form.html'
    success_url = reverse_lazy('base:datacenter-list')
class DatacenterDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_datacenter"
    model = Datacenter
    template_name = 'systeme/datacenter_confirm_delete.html'
    success_url = reverse_lazy('base:datacenter-list')


class ServerRoomListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_serverroom"
    model = ServerRoom
    template_name = 'systeme/server_room_list.html'
    context_object_name = 'server_rooms'
    def get(self, request, *args, **kwargs):  
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = ServerRoom.objects.all()
        # Vérifier le type du paramètre et trier en conséquence
        if q : 
          queryset = ServerRoom.objects.filter(
                              Q(name__icontains=q) |
                              Q(racks__name__icontains=q) |          
                              Q(datacenter__name__icontains=q)|
                              Q(racks__servers__name__icontains=q)).distinct().order_by('created')
                              
        # Passer le queryset trié au template
        
        context = {
                'server_rooms': queryset,
                   
                   }

        return render(request, self.template_name, context)
    

class ServerRoomDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_serverroom"
    model = ServerRoom
    template_name = 'systeme/server_room_detail.html'
    context_object_name = 'server_room'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ServerRoomSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ServerRoomCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_serverroom"
    model = ServerRoom
    form_class = ServerRoomForm
    template_name = 'systeme/server_room_form.html'
    success_url = reverse_lazy('base:server_room-list')
class ServerRoomUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_serverroom"
    model = ServerRoom
    form_class = ServerRoomUpdateForm
    template_name = 'systeme/server_room_form.html'
    success_url = reverse_lazy('base:server_room-list')

class ServerRoomDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_serverroom"
    model = ServerRoom
    template_name = 'systeme/server_room_confirm_delete.html'
    success_url = reverse_lazy('base:server_room-list')


class RackListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_rack"
    model = Rack
    template_name = 'systeme/rack_list.html'
    context_object_name = 'racks'
    def get(self, request, *args, **kwargs):  
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Rack.objects.all()
        # Vérifier le type du paramètre et trier en conséquence
        if q : 
          queryset = Rack.objects.filter(
                              Q(name__icontains=q) |
                              Q(server_room__name__icontains=q) |          
                              Q(server_room__datacenter__name__icontains=q)|
                              Q(servers__name__icontains=q)).distinct().order_by('created')
                              
        # Passer le queryset trié au template
        context = {'racks': queryset}
        return render(request, self.template_name, context)

class RackDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_rack"
    model = Rack
    template_name = 'systeme/rack_detail.html'
    context_object_name = 'rack'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = RackSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class RackCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_rack"
    model = Rack
    form_class = RackForm
    template_name = 'systeme/rack_form.html'
    success_url = reverse_lazy('base:rack-list')


class RackUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_rack"
    model = Rack
    form_class = RackUpdateForm
    template_name = 'systeme/rack_form.html'
    success_url = reverse_lazy('base:rack-list')

class RackDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_rack"
    model = Rack
    template_name = 'systeme/rack_confirm_delete.html'
    success_url = reverse_lazy('base:rack-list')

class ClusterListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_cluster"
    model = Cluster
    template_name = 'systeme/cluster_list.html'
    context_object_name = 'clusters'
    def get(self, request, *args, **kwargs):  
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = Cluster.objects.all()
        # Vérifier le type du paramètre et trier en conséquence
        if q : 
          queryset = Cluster.objects.filter(
                              Q(name__icontains=q) |
                              Q(ip_address__ipv4__icontains=q) |          
                              Q(servers__name__icontains=q)|
                              Q(servers__type_server__icontains=q)).distinct().order_by('created')
                              
        # Passer le queryset trié au template
        context = {'clusters': queryset}
        return render(request, self.template_name, context)


class ClusterDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_cluster"
    model = Cluster
    template_name = 'systeme/cluster_detail.html'
    context_object_name = 'cluster'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ClusterSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ClusterCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_cluster"
    model = Cluster
    form_class = ClusterForm
    template_name = 'systeme/cluster_form.html'
    success_url = reverse_lazy('base:cluster-list')

class ClusterUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_cluster"
    model = Cluster
    form_class = ClusterUpdateForm
    template_name = 'systeme/cluster_form.html'
    success_url = reverse_lazy('base:cluster-list')

class ClusterDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_cluster"
    model = Cluster
    template_name = 'systeme/cluster_confirm_delete.html'
    success_url = reverse_lazy('base:cluster-list')
class SystemeStockageListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_systemestockage"
    model = SystemeStockage
    template_name = 'systeme/systeme_stockage_list.html'
    context_object_name = 'systeme_stockages'

class SystemeStockageDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_systemestockage"
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
         
class SystemeStockageCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_systemestockage"
    model = SystemeStockage
    form_class = SystemeStockageForm
    template_name = 'systeme/systeme_stockage_form.html'
    success_url = reverse_lazy('base:systeme_stockage-list')
class SystemeStockageUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_systemestockage"
    model = SystemeStockage
    form_class = SystemeStockageUpdateForm
    template_name = 'systeme/systeme_stockage_form.html'
    success_url = reverse_lazy('base:systeme_stockage-list')

class SystemeStockageDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_systemestockage"
    model = SystemeStockage
    template_name = 'systeme/systeme_stockage_confirm_delete.html'
    success_url = reverse_lazy('base:systeme_stockage-list')


class ServerListView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = "base.view_server"
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

class ServerDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_server"
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

class ServerCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_server"
    model = Server
    form_class = ServerForm
    template_name = 'systeme/server_form.html'
    success_url = reverse_lazy('base:server-list')


class ServerUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_server"
    model = Server
    form_class = ServerUpdateForm
    template_name = 'systeme/server_form.html'
    success_url = reverse_lazy('base:server-list')
  
class ServerDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_server"
    model = Server
    template_name = 'systeme/server_confirm_delete.html'
    success_url = reverse_lazy('base:server-list')

class DeploiementClusterListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_deploiementcluster"
    model = DeploiementCluster
    template_name = 'systeme/deploiement_cluster_list.html'
    context_object_name = 'deploiement_clusters'
class DeploiementClusterDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_deploiementcluster"
    model = DeploiementCluster
    template_name = 'systeme/deploiement_cluster_detail.html'
    context_object_name = 'deploiement_cluster'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DeploiementClusterSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class DeploiementClusterCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_deploiementcluster"
    model = DeploiementCluster
    form_class = DeploiementClusterForm
    template_name = 'systeme/deploiement_cluster_form.html'
    success_url = reverse_lazy('base:deploiement_cluster-list')
class DeploiementClusterUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_deploiementcluster"
    model = DeploiementCluster
    form_class = DeploiementClusterUpdateForm
    template_name = 'systeme/deploiement_cluster_form.html'
    success_url = reverse_lazy('base:deploiement_cluster-list')
class DeploiementClusterDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_deploiementcluster"
    model = DeploiementCluster
    template_name = 'systeme/deploiement_cluster_confirm_delete.html'
    success_url = reverse_lazy('base:deploiement_cluster-list')


class PartitionListView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = "base.view_partition"
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
class PartitionDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_partition"
    model = Partition
    template_name = 'systeme/partition_detail.html'
    context_object_name = 'partition'  
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = PartitionSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class PartitionCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_partition"
    model = Partition
    form_class = PartitionForm
    template_name = 'systeme/partition_form.html'
    success_url = reverse_lazy('base:partition-list')
class PartitionUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_partition"
    model = Partition
    form_class = PartitionUpdateForm
    template_name = 'systeme/partition_form.html'
    success_url = reverse_lazy('base:partition-list')
class PartitionDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_partition"
    model = Partition
    template_name = 'systeme/partition_confirm_delete.html'
    success_url = reverse_lazy('base:partition-list')

class DatabaseServerListView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = "base.view_databaseserver"
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
class DatabaseServerDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_databaseserver"
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
class DatabaseServerCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_databaseserver"
    model = DatabaseServer
    form_class = DatabaseServerForm
    template_name = 'systeme/database_server_form.html'
    success_url = reverse_lazy('base:database_server-list')
class DatabaseServerUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_databaseserver"
    model = DatabaseServer
    form_class = DatabaseServerUpdateForm
    template_name = 'systeme/database_server_form.html'
    success_url = reverse_lazy('base:database_server-list')
class DatabaseServerDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_databaseserver"
    model = DatabaseServer
    template_name = 'systeme/database_server_confirm_delete.html'
    success_url = reverse_lazy('base:database_server-list')


class DatabaseListView(LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = "base.view_database"
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

class DatabaseDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_database"
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

class DatabaseCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_database"
    model = Database
    form_class = DatabaseForm
    template_name = 'systeme/database_form.html'
    success_url = reverse_lazy('base:database-list')

class DatabaseUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_database"
    model = Database
    form_class = DatabaseUpdateForm
    template_name = 'systeme/database_form.html'
    success_url = reverse_lazy('base:database-list')
  
class DatabaseDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_database"
    model = Database
    template_name = 'systeme/database_confirm_delete.html'
    success_url = reverse_lazy('base:database-list')

############# END SYSTEME MODULE VIEWS ###############################






def home(request):
    server = Server.objects.get(pk=1)
    serializer = ServerSerializer(server)
    print(serializer.data)
    serializer_data=json.dumps(serializer.data)
    #print(serializer_data)
    context={"serializer_data":serializer_data}
    return render(request, 'application/test2.html',context)  


################################Documentation #######################


class BackupStrategieListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_backupstrategie"
    model = BackupStrategie
    template_name = 'documentation/backupstrategie_list.html'
    context_object_name = 'backup_strategies'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = BackupStrategie.objects.all()
        if q :
          queryset = BackupStrategie.objects.filter(
                            Q(name__icontains=q) |
                            Q(applications__name__icontains=q) |          
                            Q(applications__modules_applicatifs__name__icontains=q))  
        # Passer le queryset trié au template
        print(queryset)
        context = {'backup_strategies': queryset}
        return render(request, self.template_name, context)
class BackupStrategieDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_backupstrategie"
    model = BackupStrategie
    template_name = 'documentation/backupstrategie_detail.html'
    context_object_name = 'backup_strategy'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = BackupStrategieSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class BackupStrategieCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_backupstrategie"
    model = BackupStrategie
    template_name = 'documentation/backupstrategie_form.html'
    form_class = BackupStrategieCreateForm
    success_url = reverse_lazy('base:backupstrategie-list')
    def form_valid(self, form):
        return super().form_valid(form)

class BackupStrategieUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_backupstrategie"
    model = BackupStrategie
    template_name = 'documentation/backupstrategie_form.html'
    form_class = BackupStrategieUpdateForm
    success_url = reverse_lazy('base:backupstrategie-list')
    def form_valid(self, form):
        return super().form_valid(form)

class BackupStrategieDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_backupstrategie"
    model = BackupStrategie
    template_name = 'documentation/backupstrategie_confirm_delete.html'
    success_url = reverse_lazy('backupstrategie-list')



class CallFlowListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_callflow"
    model = CallFlow
    template_name = 'documentation/call_flow_list.html'
    context_object_name = 'call_flows'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = CallFlow.objects.all()
        if q :
          queryset = CallFlow.objects.filter(
                            Q(name__icontains=q) |
                            Q(use_case__name__icontains=q) |          
                            Q(use_case__appels_apis__name__icontains=q))  
        # Passer le queryset trié au template
        print(queryset)
        context = {'call_flows': queryset}
        return render(request, self.template_name, context)
class CallFlowDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_callflow"
    model = CallFlow
    template_name = 'documentation/call_flow_detail.html'
    context_object_name = 'call_flow'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = CallFlowSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class CallFlowCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_callflow"
    model = CallFlow
    template_name = 'documentation/call_flow_form.html'
    form_class = CallFlowCreateForm
    success_url = reverse_lazy('base:call_flow-list')
    def form_valid(self, form):
        return super().form_valid(form)

class CallFlowUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_callflow"
    model = CallFlow
    template_name = 'documentation/call_flow_form.html'
    form_class = CallFlowUpdateForm
    success_url = reverse_lazy('base:call_flow-list')
    def form_valid(self, form):
        return super().form_valid(form)

class CallFlowDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_callflow"
    model = CallFlow
    template_name = 'documentation/call_flow_confirm_delete.html'
    success_url = reverse_lazy('call_flow-list')



class TechnicalRecoveryPlanListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_technicalrecoveryplan"
    model = TechnicalRecoveryPlan
    template_name = 'documentation/technical_recovery_plan_list.html'
    context_object_name = 'technical_recovery_plans'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = TechnicalRecoveryPlan.objects.all()
        if q :
          queryset = TechnicalRecoveryPlan.objects.filter(
                            Q(name__icontains=q) |
                            Q(application__name__icontains=q) |          
                            Q(application__modules_applicatifs__name__icontains=q))  
        # Passer le queryset trié au template
        print(queryset)
        context = {'technical_recovery_plans': queryset}
        return render(request, self.template_name, context)

class TechnicalRecoveryPlanDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_technicalrecoveryplan"
    model = TechnicalRecoveryPlan
    template_name = 'documentation/technical_recovery_plan_detail.html'
    context_object_name = 'technical_recovery_plan'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = TechnicalRecoveryPlanSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class TechnicalRecoveryPlanCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_technicalrecoveryplan"
    model = TechnicalRecoveryPlan
    template_name = 'documentation/technical_recovery_plan_form.html'
    form_class = TechnicalRecoveryPlanCreateForm
    success_url = reverse_lazy('base:technical_recovery_plan-list')
    def form_valid(self, form):
        return super().form_valid(form)

class TechnicalRecoveryPlanUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_technicalrecoveryplan"
    model = TechnicalRecoveryPlan
    template_name = 'documentation/technical_recovery_plan_form.html'
    form_class = TechnicalRecoveryPlanUpdateForm
    success_url = reverse_lazy('base:technical_recovery_plan-list')
    def form_valid(self, form):
        return super().form_valid(form)

class TechnicalRecoveryPlanDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_technicalrecoveryplan"
    model = TechnicalRecoveryPlan
    template_name = 'documentation/technical_recovery_plan_confirm_delete.html'
    success_url = reverse_lazy('technical_recovery_plan-list')



class ArchitectureDiagramListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_architecturediagram"
    model = ArchitectureDiagram
    template_name = 'documentation/architecture_diagram_list.html'
    context_object_name = 'architecture_diagrams'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = ArchitectureDiagram.objects.all()
        if q :
          queryset = ArchitectureDiagram.objects.filter(
                            Q(name__icontains=q) |
                            Q(process__name__icontains=q) |          
                            Q(process__sub_processes__name__icontains=q))  
        # Passer le queryset trié au template
        print(queryset)
        context = {'architecture_diagrams': queryset}
        return render(request, self.template_name, context)

class ArchitectureDiagramDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_architecturediagram"
    model = ArchitectureDiagram
    template_name = 'documentation/architecture_diagram_detail.html'
    context_object_name = 'architecture_diagram'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ArchitectureDiagramSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class ArchitectureDiagramCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_architecturediagram"
    model = ArchitectureDiagram
    template_name = 'documentation/architecture_diagram_form.html'
    form_class = ArchitectureDiagramCreateForm
    success_url = reverse_lazy('base:architecture_diagram-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ArchitectureDiagramUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_architecturediagram"
    model = ArchitectureDiagram
    template_name = 'documentation/architecture_diagram_form.html'
    form_class = ArchitectureDiagramUpdateForm
    success_url = reverse_lazy('base:architecture_diagram-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ArchitectureDiagramDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_architecturediagram"
    model = ArchitectureDiagram
    template_name = 'documentation/architecture_diagram_confirm_delete.html'
    success_url = reverse_lazy('architecture_diagram-list')



class ApiSpecificationListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_apispecification"
    model = ApiSpecification
    template_name = 'documentation/api_specification_list.html'
    context_object_name = 'api_specifications'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = ApiSpecification.objects.all()
        if q :
          queryset = ApiSpecification.objects.filter(
                            Q(name__icontains=q) |
                            Q(api__name__icontains=q) |   
                            Q(api__appels_apis__name__icontains=q) |       
                            Q(apis_documentations__name__icontains=q))  
        # Passer le queryset trié au template
        print(queryset)
        context = {'api_specifications': queryset}
        return render(request, self.template_name, context)
class ApiSpecificationDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_apispecification"
    model = ApiSpecification
    template_name = 'documentation/api_specification_detail.html'
    context_object_name = 'api_specification'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ApiSpecificationSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class ApiSpecificationCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_apispecification"
    model = ApiSpecification
    template_name = 'documentation/api_specification_form.html'
    form_class = ApiSpecificationCreateForm
    success_url = reverse_lazy('base:api_specification-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ApiSpecificationUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_apispecification"
    model = ApiSpecification
    template_name = 'documentation/api_specification_form.html'
    form_class = ApiSpecificationUpdateForm
    success_url = reverse_lazy('base:api_specification-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ApiSpecificationDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_apispecification"
    model = ApiSpecification
    template_name = 'documentation/api_specification_confirm_delete.html'
    success_url = reverse_lazy('api_specification-list')




class ApiDocumentationListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_apidocumentation"
    model = ApiDocumentation
    template_name = 'documentation/api_documentation_list.html'
    context_object_name = 'api_documentations'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = ApiDocumentation.objects.all()
        if q :
          queryset = ApiDocumentation.objects.filter(
                            Q(name__icontains=q) |
                            Q(apis_specifications__api__name__icontains=q) |   
                            Q(apis_specifications__api__appels_apis__name__icontains=q)       
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'api_documentations': queryset}
        return render(request, self.template_name, context)
class ApiDocumentationDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_apidocumentation"
    model = ApiDocumentation
    template_name = 'documentation/api_documentation_detail.html'
    context_object_name = 'api_documentation'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ApiDocumentationSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class ApiDocumentationCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_apidocumentation"
    model = ApiDocumentation
    template_name = 'documentation/api_documentation_form.html'
    form_class = ApiDocumentationCreateForm
    success_url = reverse_lazy('base:api_documentation-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ApiDocumentationUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_apidocumentation"
    model = ApiDocumentation
    template_name = 'documentation/api_documentation_form.html'
    form_class = ApiDocumentationUpdateForm
    success_url = reverse_lazy('base:api_documentation-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ApiDocumentationDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_apidocumentation"
    model = ApiDocumentation
    template_name = 'documentation/api_documentation_confirm_delete.html'
    success_url = reverse_lazy('api_documentation-list')


class DataModelListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_datamodel"
    model = DataModel
    template_name = 'documentation/data_model_list.html'
    context_object_name = 'data_models'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = DataModel.objects.all()
        if q :
          queryset = DataModel.objects.filter(
                            Q(name__icontains=q) |
                            Q(database__name__icontains=q) |   
                            Q(data_dictionnary__name__icontains=q) |  
                            Q(database__module_applicatifs__name__icontains=q)|
                            Q(database__module_applicatifs__application__name__icontains=q)
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'data_models': queryset}
        return render(request, self.template_name, context)
class DataModelDetailView(DetailView):
    permission_required = "base.view_datamodel"
    model = DataModel
    template_name = 'documentation/data_model_detail.html'
    context_object_name = 'data_model'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DataModelSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class DataModelCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_datamodel"
    model = DataModel
    template_name = 'documentation/data_model_form.html'
    form_class = DataModelCreateForm
    success_url = reverse_lazy('base:data_model-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DataModelUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_datamodel"
    model = DataModel
    template_name = 'documentation/data_model_form.html'
    form_class = DataModelUpdateForm
    success_url = reverse_lazy('base:data_model-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DataModelDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_datamodel"
    model = DataModel
    template_name = 'documentation/data_model_confirm_delete.html'
    success_url = reverse_lazy('data_model-list')



class DataDictionnaryModelListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_datadictionnarymodel"
    model = DataDictionnaryModel
    template_name = 'documentation/data_dictionnary_model_list.html'
    context_object_name = 'data_dictionnary_models'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = DataDictionnaryModel.objects.all()
        if q :
          queryset = DataDictionnaryModel.objects.filter(
                            Q(name__icontains=q) |
                            Q(data_model__name__icontains=q) |   
                            Q(data_dictionnary__name__icontains=q)       
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'data_dictionnary_models': queryset}
        return render(request, self.template_name, context)
class DataDictionnaryModelDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_datadictionnarymodel"
    model = DataDictionnaryModel
    template_name = 'documentation/data_dictionnary_model_detail.html'
    context_object_name = 'data_dictionnary_model'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DataDictionnaryModelSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class DataDictionnaryModelCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_datadictionnarymodel"
    model = DataDictionnaryModel
    template_name = 'documentation/data_dictionnary_model_form.html'
    form_class = DataDictionnaryModelCreateForm
    success_url = reverse_lazy('base:data_dictionnary_model-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DataDictionnaryModelUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_datadictionnarymodel"
    model = DataDictionnaryModel
    template_name = 'documentation/data_dictionnary_model_form.html'
    form_class = DataDictionnaryModelUpdateForm
    success_url = reverse_lazy('base:data_dictionnary_model-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DataDictionnaryModelDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_datadictionnarymodel"
    model = DataDictionnaryModel
    template_name = 'documentation/data_dictionnary_model_confirm_delete.html'
    success_url = reverse_lazy('data_dictionnary_model-list')




class DataDictionnaryListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "base.view_datadictionnary"
    model = DataDictionnary
    template_name = 'documentation/data_dictionnary_list.html'
    context_object_name = 'data_dictionnaries'
    def get(self, request, *args, **kwargs):
        # Récupérer le paramètre de la requête GET
        q = self.request.GET.get('q', '')
        # Initialiser le queryset de base (non trié)
        queryset = DataDictionnary.objects.all()
        if q :
          queryset = DataDictionnary.objects.filter(
                            Q(name__icontains=q) |
                            Q(datas_models__name__icontains=q) |          
                            Q(datas_models__database__name__icontains=q) |   
                            Q(datas_models__data_dictionnary__name__icontains=q) |  
                            Q(datas_models__database__module_applicatifs__name__icontains=q)|
                            Q(datas_models__database__module_applicatifs__application__name__icontains=q)    
                            )  
        # Passer le queryset trié au template
        print(queryset)
        context = {'data_dictionnaries': queryset}
        return render(request, self.template_name, context)

class DataDictionnaryDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    permission_required = "base.view_datadictionnary"
    model = DataDictionnary
    template_name = 'documentation/data_dictionnary_detail.html'
    context_object_name = 'data_dictionnary'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DataDictionnarySerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class DataDictionnaryCreateView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "base.add_datadictionnary"
    model = DataDictionnary
    template_name = 'documentation/data_dictionnary_form.html'
    form_class = DataDictionnaryCreateForm
    success_url = reverse_lazy('base:data_dictionnary-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DataDictionnaryUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "base.change_datadictionnary"
    model = DataDictionnary
    template_name = 'documentation/data_dictionnary_form.html'
    form_class = DataDictionnaryUpdateForm
    success_url = reverse_lazy('base:data_dictionnary-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DataDictionnaryDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "base.delete_datadictionnary"
    model = DataDictionnary
    template_name = 'documentation/data_dictionnary_confirm_delete.html'
    success_url = reverse_lazy('data_dictionnary-list')


#########################end documentation###########################