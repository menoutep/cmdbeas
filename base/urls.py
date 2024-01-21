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

path('departement-api/<int:departement_id>/', views.departementApi, name='departement-api'),
path('server-room-api/<int:id>/', views.serverRoomApiView.as_view(), name='server-room-api'),
path('datacenter-api/<int:id>/', views.DatacenterApiView.as_view(), name='datacenter-api'),

path('home', views.home, name='home'),
]