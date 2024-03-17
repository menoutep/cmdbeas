from django.urls import path
from base import views
# urls.py



app_name='base'

urlpatterns = [

path('', views.index, name='index'),
path('departement', views.DepartementListView.as_view(), name='departement-list'),
path('departement/<int:pk>/', views.DepartementDetailView.as_view(), name='detail-departement'),
path('departement/<int:pk>/update/', views.DepartementUpdateView.as_view(), name='update-departement'),
path('departement/create', views.DepartementCreateView.as_view(), name='create-departement'),
path('departement/<int:pk>/delete', views.DepartementDeleteView.as_view(), name='delete-departement'),

path('apptype', views.AppTypeListView.as_view(), name='apptype-list'),
path('apptype/<int:pk>/', views.AppTypeDetailView.as_view(), name='detail-apptype'),
path('apptype/<int:pk>/update/', views.AppTypeUpdateView.as_view(), name='update-apptype'),
path('apptype/create', views.AppTypeCreateView.as_view(), name='create-apptype'),

path('datacenter', views.DatacenterListView.as_view(), name='datacenter-list'),
path('datacenter/<int:pk>/', views.DatacenterDetailView.as_view(), name='detail-datacenter'),
path('datacenter/<int:pk>/update/', views.DatacenterUpdateView.as_view(), name='update-datacenter'),
path('datacenter/create', views.DatacenterCreateView.as_view(), name='create-datacenter'),
path('datacenter/<int:pk>/delete', views.DatacenterDeleteView.as_view(), name='delete-datacenter'),

path('server_room', views.ServerRoomListView.as_view(), name='server_room-list'),
path('server_room/<int:pk>/', views.ServerRoomDetailView.as_view(), name='detail-server_room'),
path('server_room/<int:pk>/update/', views.ServerRoomUpdateView.as_view(), name='update-server_room'),
path('server_room/create', views.ServerRoomCreateView.as_view(), name='create-server_room'),
path('server_room/<int:pk>/delete', views.ServerRoomDeleteView.as_view(), name='delete-server_room'),

path('rack', views.RackListView.as_view(), name='rack-list'),
path('rack/<int:pk>/', views.RackDetailView.as_view(), name='detail-rack'),
path('rack/<int:pk>/update/', views.RackUpdateView.as_view(), name='update-rack'),
path('rack/create', views.RackCreateView.as_view(), name='create-rack'),
path('rack/<int:pk>/delete', views.RackDeleteView.as_view(), name='delete-rack'),

path('cluster', views.ClusterListView.as_view(), name='cluster-list'),
path('cluster/<int:pk>/delete', views.ClusterDeleteView.as_view(), name='delete-cluster'),
path('cluster/<int:pk>/', views.ClusterDetailView.as_view(), name='detail-cluster'),
path('cluster/<int:pk>/update/', views.ClusterUpdateView.as_view(), name='update-cluster'),
path('cluster/create', views.ClusterCreateView.as_view(), name='create-cluster'),
path('systeme_stockage', views.SystemeStockageListView.as_view(), name='systeme_stockage-list'),
path('systeme_stockage/<int:pk>/', views.SystemeStockageDetailView.as_view(), name='detail-systeme_stockage'),
path('systeme_stockage/<int:pk>/update/', views.SystemeStockageUpdateView.as_view(), name='update-systeme_stockage'),
path('systeme_stockage/create', views.SystemeStockageCreateView.as_view(), name='create-systeme_stockage'),
path('systeme_stockage/<int:pk>/delete', views.SystemeStockageDeleteView.as_view(), name='delete-systeme_stockage'),

path('server', views.ServerListView.as_view(), name='server-list'),
path('server/<int:pk>/', views.ServerDetailView.as_view(), name='detail-server'),
path('server/<int:pk>/update/', views.ServerUpdateView.as_view(), name='update-server'),
path('server/create', views.ServerCreateView.as_view(), name='create-server'),
path('server/<int:pk>/delete/', views.ServerDeleteView.as_view(), name='delete-server'),

path('deploiement_cluster', views.DeploiementClusterListView.as_view(), name='deploiement_cluster-list'),
path('deploiement_cluster/<int:pk>/', views.DeploiementClusterDetailView.as_view(), name='detail-deploiement_cluster'),
path('deploiement_cluster/<int:pk>/update/', views.DeploiementClusterUpdateView.as_view(), name='update-deploiement_cluster'),
path('deploiement_cluster/create', views.DeploiementClusterCreateView.as_view(), name='create-deploiement_cluster'),
path('deploiement_cluster/<int:pk>/delete/', views.DeploiementClusterDeleteView.as_view(), name='delete-deploiement_cluster'),

path('partition', views.PartitionListView.as_view(), name='partition-list'),
path('partition/<int:pk>/', views.PartitionDetailView.as_view(), name='detail-partition'),
path('partition/<int:pk>/update/', views.PartitionUpdateView.as_view(), name='update-partition'),
path('partition/create', views.PartitionCreateView.as_view(), name='create-partition'),
path('partition/<int:pk>/delete/', views.PartitionDeleteView.as_view(), name='delete-partition'),

path('database_server', views.DatabaseServerListView.as_view(), name='database_server-list'),
path('database_server/<int:pk>/', views.DatabaseServerDetailView.as_view(), name='detail-database_server'),
path('database_server/<int:pk>/update/', views.DatabaseServerUpdateView.as_view(), name='update-database_server'),
path('database_server/create', views.DatabaseServerCreateView.as_view(), name='create-database_server'),
path('database_server/<int:pk>/delete/', views.DatabaseServerDeleteView.as_view(), name='delete-database_server'),

path('database', views.DatabaseListView.as_view(), name='database-list'),
path('database/<int:pk>/', views.DatabaseDetailView.as_view(), name='detail-database'),
path('database/<int:pk>/update/', views.DatabaseUpdateView.as_view(), name='update-database'),
path('database/create', views.DatabaseCreateView.as_view(), name='create-database'),
path('database/<int:pk>/delete/', views.DatabaseDeleteView.as_view(), name='delete-database'),

path('vendor', views.VendorListView.as_view(), name='vendor-list'),
path('vendor/<int:pk>/', views.VendorDetailView.as_view(), name='detail-vendor'),
path('vendor/<int:pk>/update/', views.VendorUpdateView.as_view(), name='update-vendor'),
path('vendor/create', views.VendorCreateView.as_view(), name='create-vendor'),
path('vendor/<int:pk>/delete/', views.VendorDeleteView.as_view(), name='delete-vendor'),

path('application', views.ApplicationListView.as_view(), name='application-list'),
path('application/<int:pk>/', views.ApplicationDetailView.as_view(), name='detail-application'),
path('application/<int:pk>/update/', views.ApplicationUpdateView.as_view(), name='update-application'),
path('application/create', views.ApplicationCreateView.as_view(), name='create-application'),
path('application/<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='delete-application'),

path('module_applicatif', views.ModuleApplicatifListView.as_view(), name='module_applicatif-list'),
path('module_applicatif/<int:pk>/', views.ModuleApplicatifDetailView.as_view(), name='detail-module_applicatif'),
path('module_applicatif/<int:pk>/update/', views.ModuleApplicatifUpdateView.as_view(), name='update-module_applicatif'),
path('module_applicatif/create', views.ModuleApplicatifCreateView.as_view(), name='create-module_applicatif'),
path('module_applicatif/<int:pk>/delete/', views.ModuleApplicatifDeleteView.as_view(), name='delete-module_applicatif'),

path('app_server', views.AppServerListView.as_view(), name='app_server-list'),
path('app_server/<int:pk>/', views.AppServerDetailView.as_view(), name='detail-app_server'),
path('app_server/<int:pk>/update/', views.AppServerUpdateView.as_view(), name='update-app_server'),
path('app_server/create', views.AppServerCreateView.as_view(), name='create-app_server'),
path('app_server/<int:pk>/delete/', views.AppServerDeleteView.as_view(), name='delete-app_server'),


path('app_deployment', views.AppDeploymentListView.as_view(), name='app_deployment-list'),
path('app_deployment/<int:pk>/', views.AppDeploymentDetailView.as_view(), name='detail-app_deployment'),
path('app_deployment/<int:pk>/update/', views.AppDeploymentUpdateView.as_view(), name='update-app_deployment'),
path('app_deployment/create', views.AppDeploymentCreateView.as_view(), name='create-app_deployment'),
path('app_deployment/<int:pk>/delete/', views.AppDeploymentDeleteView.as_view(), name='delete-app_deployment'),


path('connexion_bd', views.ConnexionBDListView.as_view(), name='connexion_bd-list'),
path('connexion_bd/<int:pk>/', views.ConnexionBDDetailView.as_view(), name='detail-connexion_bd'),
path('connexion_bd/<int:pk>/update/', views.ConnexionBDUpdateView.as_view(), name='update-connexion_bd'),
path('connexion_bd/create', views.ConnexionBDCreateView.as_view(), name='create-connexion_bd'),
path('connexion_bd/<int:pk>/delete/', views.ConnexionBDDeleteView.as_view(), name='delete-connexion_bd'),



path('ip_adress', views.IpAdressListView.as_view(), name='ip_adress-list'),
path('ip_adress/<int:pk>/', views.IpAdressDetailView.as_view(), name='detail-ip_adress'),
path('ip_adress/<int:pk>/update/', views.IpAdressUpdateView.as_view(), name='update-ip_adress'),
path('ip_adress/create', views.IpAdressCreateView.as_view(), name='create-ip_adress'),
path('ip_adress/<int:pk>/delete/', views.IpAdressDeleteView.as_view(), name='delete-ip_adress'),

path('network_interface', views.NetworkInterfaceListView.as_view(), name='network_interface-list'),
path('network_interface/<int:pk>/', views.NetworkInterfaceDetailView.as_view(), name='detail-network_interface'),
path('network_interface/<int:pk>/update/', views.NetworkInterfaceUpdateView.as_view(), name='update-network_interface'),
path('network_interface/create', views.NetworkInterfaceCreateView.as_view(), name='create-network_interface'),
path('network_interface/<int:pk>/delete/', views.NetworkInterfaceDeleteView.as_view(), name='delete-network_interface'),


path('appel_api', views.AppelApiListView.as_view(), name='appel_api-list'),
path('appel_api/<int:pk>/', views.AppelApiDetailView.as_view(), name='detail-appel_api'),
path('appel_api/<int:pk>/update/', views.AppelApiUpdateView.as_view(), name='update-appel_api'),
path('appel_api/create', views.AppelApiCreateView.as_view(), name='create-appel_api'),
path('appel_api/<int:pk>/delete/', views.AppelApiDeleteView.as_view(), name='delete-appel_api'),

path('api', views.ApiListView.as_view(), name='api-list'),
path('api/<int:pk>/', views.ApiDetailView.as_view(), name='detail-api'),
path('api/<int:pk>/update/', views.ApiUpdateView.as_view(), name='update-api'),
path('api/create', views.ApiCreateView.as_view(), name='create-api'),
path('api/<int:pk>/delete/', views.ApiDeleteView.as_view(), name='delete-api'),

path('use_case', views.UseCaseListView.as_view(), name='use_case-list'),
path('use_case/<int:pk>/', views.UseCaseDetailView.as_view(), name='detail-use_case'),
path('use_case/<int:pk>/update/', views.UseCaseUpdateView.as_view(), name='update-use_case'),
path('use_case/create', views.UseCaseCreateView.as_view(), name='create-use_case'),
path('use_case/<int:pk>/delete/', views.UseCaseDeleteView.as_view(), name='delete-use_case'),

path('process', views.ProcessListView.as_view(), name='process-list'),
path('process/<int:pk>/', views.ProcessDetailView.as_view(), name='detail-process'),
path('process/<int:pk>/update/', views.ProcessUpdateView.as_view(), name='update-process'),
path('process/create', views.ProcessCreateView.as_view(), name='create-process'),
path('process/<int:pk>/delete/', views.ProcessDeleteView.as_view(), name='delete-process'),

path('sub_process', views.SubProcessListView.as_view(), name='sub_process-list'),
path('sub_process/<int:pk>/', views.SubProcessDetailView.as_view(), name='detail-sub_process'),
path('sub_process/<int:pk>/update/', views.SubProcessUpdateView.as_view(), name='update-sub_process'),
path('sub_process/create', views.SubProcessCreateView.as_view(), name='create-sub_process'),
path('sub_process/<int:pk>/delete/', views.SubProcessDeleteView.as_view(), name='delete-sub_process'),

path('backupstrategie/', views.BackupStrategieListView.as_view(), name='backupstrategie-list'),
path('backupstrategie/<int:pk>/', views.BackupStrategieDetailView.as_view(), name='backupstrategie-detail'),
path('backupstrategie/create/', views.BackupStrategieCreateView.as_view(), name='backupstrategie-create'),
path('backupstrategie/<int:pk>/update/', views.BackupStrategieUpdateView.as_view(), name='backupstrategie-update'),
path('backupstrategie/<int:pk>/delete/', views.BackupStrategieDeleteView.as_view(), name='backupstrategie-delete'),

path('data_model', views.DataModelListView.as_view(), name='data_model-list'),
path('data_model/<int:pk>/', views.DataModelDetailView.as_view(), name='detail-data_model'),
path('data_model/<int:pk>/update/', views.DataModelUpdateView.as_view(), name='update-data_model'),
path('data_model/create', views.DataModelCreateView.as_view(), name='create-data_model'),
path('data_model/<int:pk>/delete/', views.DataModelDeleteView.as_view(), name='delete-data_model'),

path('architecture_diagram', views.ArchitectureDiagramListView.as_view(), name='architecture_diagram-list'),
path('architecture_diagram/<int:pk>/', views.ArchitectureDiagramDetailView.as_view(), name='detail-architecture_diagram'),
path('architecture_diagram/<int:pk>/update/', views.ArchitectureDiagramUpdateView.as_view(), name='update-architecture_diagram'),
path('architecture_diagram/create', views.ArchitectureDiagramCreateView.as_view(), name='create-architecture_diagram'),
path('architecture_diagram/<int:pk>/delete/', views.ArchitectureDiagramDeleteView.as_view(), name='delete-architecture_diagram'),

path('technical_recovery_plan', views.TechnicalRecoveryPlanListView.as_view(), name='technical_recovery_plan-list'),
path('technical_recovery_plan/<int:pk>/', views.TechnicalRecoveryPlanDetailView.as_view(), name='detail-technical_recovery_plan'),
path('technical_recovery_plan/<int:pk>/update/', views.TechnicalRecoveryPlanUpdateView.as_view(), name='update-technical_recovery_plan'),
path('technical_recovery_plan/create', views.TechnicalRecoveryPlanCreateView.as_view(), name='create-technical_recovery_plan'),
path('technical_recovery_plan/<int:pk>/delete/', views.TechnicalRecoveryPlanDeleteView.as_view(), name='delete-technical_recovery_plan'),

path('data_dictionnary', views.DataDictionnaryListView.as_view(), name='data_dictionnary-list'),
path('data_dictionnary/<int:pk>/', views.DataDictionnaryDetailView.as_view(), name='detail-data_dictionnary'),
path('data_dictionnary/<int:pk>/update/', views.DataDictionnaryUpdateView.as_view(), name='update-data_dictionnary'),
path('data_dictionnary/create', views.DataDictionnaryCreateView.as_view(), name='create-data_dictionnary'),
path('data_dictionnary/<int:pk>/delete/', views.DataDictionnaryDeleteView.as_view(), name='delete-data_dictionnary'),

path('api_specification', views.ApiSpecificationListView.as_view(), name='api_specification-list'),
path('api_specification/<int:pk>/', views.ApiSpecificationDetailView.as_view(), name='detail-api_specification'),
path('api_specification/<int:pk>/update/', views.ApiSpecificationUpdateView.as_view(), name='update-api_specification'),
path('api_specification/create', views.ApiSpecificationCreateView.as_view(), name='create-api_specification'),
path('api_specification/<int:pk>/delete/', views.ApiSpecificationDeleteView.as_view(), name='delete-api_specification'),

path('api_documentation', views.ApiDocumentationListView.as_view(), name='api_documentation-list'),
path('api_documentation/<int:pk>/', views.ApiDocumentationDetailView.as_view(), name='detail-api_documentation'),
path('api_documentation/<int:pk>/update/', views.ApiDocumentationUpdateView.as_view(), name='update-api_documentation'),
path('api_documentation/create', views.ApiDocumentationCreateView.as_view(), name='create-api_documentation'),
path('api_documentation/<int:pk>/delete/', views.ApiDocumentationDeleteView.as_view(), name='delete-api_documentation'),

path('call_flow', views.CallFlowListView.as_view(), name='call_flow-list'),
path('call_flow/<int:pk>/', views.CallFlowDetailView.as_view(), name='detail-call_flow'),
path('call_flow/<int:pk>/update/', views.CallFlowUpdateView.as_view(), name='update-call_flow'),
path('call_flow/create', views.CallFlowCreateView.as_view(), name='create-call_flow'),
path('call_flow/<int:pk>/delete/', views.CallFlowDeleteView.as_view(), name='delete-call_flow'),

path('data_dictionnary_model', views.DataDictionnaryModelListView.as_view(), name='data_dictionnary_model-list'),
path('data_dictionnary_model/<int:pk>/', views.DataDictionnaryModelDetailView.as_view(), name='detail-data_dictionnary_model'),
path('data_dictionnary_model/<int:pk>/update/', views.DataDictionnaryModelUpdateView.as_view(), name='update-data_dictionnary_model'),
path('data_dictionnary_model/create', views.DataDictionnaryModelCreateView.as_view(), name='create-data_dictionnary_model'),
path('data_dictionnary_model/<int:pk>/delete/', views.DataDictionnaryModelDeleteView.as_view(), name='delete-data_dictionnary_model'),

path('mobile_app', views.MobileAppListView.as_view(), name='mobile_app-list'),
path('mobile_app/<int:pk>/', views.MobileAppDetailView.as_view(), name='detail-mobile_app'),
path('mobile_app/<int:pk>/update/', views.MobileAppUpdateView.as_view(), name='update-mobile_app'),
path('mobile_app/create', views.MobileAppCreateView.as_view(), name='create-mobile_app'),
path('mobile_app/<int:pk>/delete/', views.MobileAppDeleteView.as_view(), name='delete-mobile_app'),

path('connexion_app', views.ConnexionAppListView.as_view(), name='connexion_app-list'),
path('connexion_app/<int:pk>/', views.ConnexionAppDetailView.as_view(), name='detail-connexion_app'),
path('connexion_app/<int:pk>/update/', views.ConnexionAppUpdateView.as_view(), name='update-connexion_app'),
path('connexion_app/create', views.ConnexionAppCreateView.as_view(), name='create-connexion_app'),
path('connexion_app/<int:pk>/delete/', views.ConnexionAppDeleteView.as_view(), name='delete-connexion_app'),

path('domain_name', views.DomainNameListView.as_view(), name='domain_name-list'),
path('domain_name/<int:pk>/', views.DomainNameDetailView.as_view(), name='detail-domain_name'),
path('domain_name/<int:pk>/update/', views.DomainNameUpdateView.as_view(), name='update-domain_name'),
path('domain_name/create', views.DomainNameCreateView.as_view(), name='create-domain_name'),
path('domain_name/<int:pk>/delete/', views.DomainNameDeleteView.as_view(), name='delete-domain_name'),


path('desktop_app', views.DesktopAppListView.as_view(), name='desktop_app-list'),
path('desktop_app/<int:pk>/', views.DesktopAppDetailView.as_view(), name='detail-desktop_app'),
path('desktop_app/<int:pk>/update/', views.DesktopAppUpdateView.as_view(), name='update-desktop_app'),
path('desktop_app/create', views.DesktopAppCreateView.as_view(), name='create-desktop_app'),
path('desktop_app/<int:pk>/delete/', views.DesktopAppDeleteView.as_view(), name='delete-desktop_app'),

path('url', views.UrlListView.as_view(), name='url-list'),
path('url/<int:pk>/', views.UrlDetailView.as_view(), name='detail-url'),
path('url/<int:pk>/update/', views.UrlUpdateView.as_view(), name='update-url'),
path('url/create', views.UrlCreateView.as_view(), name='create-url'),
path('url/<int:pk>/delete/', views.UrlDeleteView.as_view(), name='delete-url'),

path('ussd_short_code', views.UssdShortCodeListView.as_view(), name='ussd_short_code-list'),
path('ussd_short_code/<int:pk>/', views.UssdShortCodeDetailView.as_view(), name='detail-ussd_short_code'),
path('ussd_short_code/<int:pk>/update/', views.UssdShortCodeUpdateView.as_view(), name='update-ussd_short_code'),
path('ussd_short_code/create', views.UssdShortCodeCreateView.as_view(), name='create-ussd_short_code'),
path('ussd_short_code/<int:pk>/delete/', views.UssdShortCodeDeleteView.as_view(), name='delete-ussd_short_code'),

path('sms_short_code', views.SmsShortCodeListView.as_view(), name='sms_short_code-list'),
path('sms_short_code/<int:pk>/', views.SmsShortCodeDetailView.as_view(), name='detail-sms_short_code'),
path('sms_short_code/<int:pk>/update/', views.SmsShortCodeUpdateView.as_view(), name='update-sms_short_code'),
path('sms_short_code/create', views.SmsShortCodeCreateView.as_view(), name='create-sms_short_code'),
path('sms_short_code/<int:pk>/delete/', views.SmsShortCodeDeleteView.as_view(), name='delete-sms_short_code'),

path('smpp_account', views.SmppAccountListView.as_view(), name='smpp_account-list'),
path('smpp_account/<int:pk>/', views.SmppAccountDetailView.as_view(), name='detail-smpp_account'),
path('smpp_account/<int:pk>/update/', views.SmppAccountUpdateView.as_view(), name='update-smpp_account'),
path('smpp_account/create', views.SmppAccountCreateView.as_view(), name='create-smpp_account'),
path('smpp_account/<int:pk>/delete/', views.SmppAccountDeleteView.as_view(), name='delete-smpp_account'),






#path('test-pdf', views.HelloPDFView.as_view()),

path('pdf/<int:id>/<str:type_file>/', views.pdf_view, name='pdf-view'),
path('home', views.home, name='home'),
]