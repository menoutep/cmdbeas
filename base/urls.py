from django.urls import path
from base import views
app_name='base'

urlpatterns = [

path('', views.index, name='index'),
path('departement', views.DepartementListView.as_view(), name='departement-list'),
path('departement/<int:pk>/', views.DepartementDetailView.as_view(), name='detail-departement'),
path('departement/<int:pk>/update/', views.DepartementUpdateView.as_view(), name='update-departement'),
path('departement/create', views.DepartementCreateView.as_view(), name='create-departement'),

path('apptype', views.AppTypeListView.as_view(), name='apptype-list'),
path('apptype/<int:pk>/', views.AppTypeDetailView.as_view(), name='detail-apptype'),
path('apptype/<int:pk>/update/', views.AppTypeUpdateView.as_view(), name='update-apptype'),
path('apptype/create', views.AppTypeCreateView.as_view(), name='create-apptype'),

path('datacenter', views.DatacenterListView.as_view(), name='datacenter-list'),
path('datacenter/<int:pk>/', views.DatacenterDetailView.as_view(), name='detail-datacenter'),
path('datacenter/<int:pk>/update/', views.DatacenterUpdateView.as_view(), name='update-datacenter'),
path('datacenter/create', views.DatacenterCreateView.as_view(), name='create-datacenter'),

path('server_room', views.ServerRoomListView.as_view(), name='server_room-list'),
path('server_room/<int:pk>/', views.ServerRoomDetailView.as_view(), name='detail-server_room'),
path('server_room/<int:pk>/update/', views.ServerRoomUpdateView.as_view(), name='update-server_room'),
path('server_room/create', views.ServerRoomCreateView.as_view(), name='create-server_room'),

path('rack', views.RackListView.as_view(), name='rack-list'),
path('rack/<int:pk>/', views.RackDetailView.as_view(), name='detail-rack'),
path('rack/<int:pk>/update/', views.RackUpdateView.as_view(), name='update-rack'),
path('rack/create', views.RackCreateView.as_view(), name='create-rack'),

path('cluster', views.ClusterListView.as_view(), name='cluster-list'),
path('cluster/<int:pk>/', views.ClusterDetailView.as_view(), name='detail-cluster'),
path('cluster/<int:pk>/update/', views.ClusterUpdateView.as_view(), name='update-cluster'),
path('cluster/create', views.ClusterCreateView.as_view(), name='create-cluster'),
path('systeme_stockage', views.SystemeStockageListView.as_view(), name='systeme_stockage-list'),
path('systeme_stockage/<int:pk>/', views.SystemeStockageDetailView.as_view(), name='detail-systeme_stockage'),
path('systeme_stockage/<int:pk>/update/', views.SystemeStockageUpdateView.as_view(), name='update-systeme_stockage'),
path('systeme_stockage/create', views.SystemeStockageCreateView.as_view(), name='create-systeme_stockage'),

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

path('home', views.home, name='home'),
]