from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import AppType, BackupStrategie, Application,SystemeStockage, Vendor, ModuleApplicatif,Server,Departement,Rack,ServerRoom,Datacenter,Partition,DeploiementCluster,Database,DatabaseServer,NetworkInterface,IpAdress
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import CustomUserUpdateForm
from base.forms import BackupStrategieUpdateForm
from base import forms
from accounts.models import User
# Register your models here.
#@admin.register(BackupStrategie)



class UserAdmin(SimpleHistoryAdmin):
    list_display = ('username', 'email', 'contact', 'departement', 'last_password_change', 'updated', 'reset_by_admin')
    list_filter = ('departement', 'reset_by_admin', 'last_password_change', 'updated')
    search_fields = ('username', 'email', 'contact','departement')

    form = CustomUserUpdateForm
admin.site.register(User, UserAdmin)


class BackupStrategieAdmin(SimpleHistoryAdmin):
    list_filter = ('file', 'updated')
    history_list_display = ["file"]
    search_fields = ['name', 'file','applications__name']
    empty_value_display = "unknown"
    form = BackupStrategieUpdateForm
admin.site.register(BackupStrategie, BackupStrategieAdmin)

class DepartementAdmin(SimpleHistoryAdmin):
    list_filter = ('name','updated','created')
    history_list_display = ["name","description","users__name"]
    search_fields = ["name","description","users__name"]
    empty_value_display = "unknown"
    form = forms.DepartementUpdateForm
admin.site.register(Departement, DepartementAdmin)

class AppTypeAdmin(SimpleHistoryAdmin):
    list_filter = ('name','updated','created')
    history_list_display = ["name","description","applications__name"]
    search_fields = ["name","description","applications__name"]
    empty_value_display = "unknown"
    form = forms.AppTypeUpdateForm
admin.site.register(AppType, AppTypeAdmin)

#####Application start######################
class ApplicationAdmin(SimpleHistoryAdmin):
    list_filter = ('deployement_year','app_type','updated','created')
    history_list_display = ["name","description","replication","priority","control_name","deployement_year","app_type","backup_strategie"]
    search_fields = ["name","description","modules_applicatifs__name","technicals_recoveries_plans__name","backup_strategie"]
    empty_value_display = "unknown"
    form = forms.ApplicationUpdateForm
admin.site.register(Application, ApplicationAdmin)

class DatabaseServerAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created')
    history_list_display = ["name","ram","rom","cluster","server"]
    search_fields = ["name",'databases_name',"description","cluster__name","cluster__ip_address__ipv4","server__name"]
    empty_value_display = "unknown"
    form = forms.DatabaseServerUpdateForm
admin.site.register(DatabaseServer, DatabaseServerAdmin)


#####Application end#############################


class SystemeStockageAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created')
    history_list_display = ["name","ram","rom"]
    search_fields = ["name",'ram','rom']
    empty_value_display = "unknown"
    form = forms.SystemeStockageUpdateForm
admin.site.register(SystemeStockage, SystemeStockageAdmin)

class VendorAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created')
    history_list_display = ["name","ram","rom"]
    search_fields = ["name","modules_applicatifs__name","modules_applicatifs__application__name"]
    empty_value_display = "unknown"
    form = forms.VendorUpdateForm
admin.site.register(Vendor, VendorAdmin)


class ModuleApplicatifAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created')
    history_list_display = ["name","ram","rom"]
    search_fields = ["name","application__name","vendor__name","departement__name","databases__name"]
    empty_value_display = "unknown"
    form = forms.ModuleApplicatifUpdateForm
admin.site.register(ModuleApplicatif, ModuleApplicatifAdmin)

class ServerAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created',"type_server","rack__server_room__name","rack__server_room__datacenter__name")
    history_list_display = ["name","ram","rom","type_server","rack","nb_processor","v_processor","sys_stockage"]
    search_fields = ["name","type_server","sys_stockage__name","rack__name","rack__server_room__name","rack__server_room__datacenter__name","networks_interfaces__name","clusters__name","networks_interfaces__ip_addresses__ipv4","apps_servers__name","databases_servers__name","databases_servers__databases__name","apps_servers__modules_applicatifs__name"]
    empty_value_display = "unknown"
    
admin.site.register(Server, ServerAdmin)


class RackAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created',"server_room__name","server_room__datacenter__name")
    history_list_display = ["name","server_room","description"]
    search_fields = ["name","servers__name","server_room__name","server_room__datacenter__name"]
    empty_value_display = "unknown"
    form = forms.RackUpdateForm
admin.site.register(Rack, RackAdmin)

class ServerRoomAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created',"datacenter__name")
    history_list_display = ["name","datacenter","description","racks__name"]
    search_fields = ["name","datacenter__name","racks__servers__name","racks__name"]
    empty_value_display = "unknown"
    form = forms.ServerRoomUpdateForm
admin.site.register(ServerRoom, ServerRoomAdmin)

class DatacenterAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created',"localisation")
    history_list_display = ["name","localisation"]
    search_fields = ["name","servers_rooms__racks__servers__name","servers__rooms__name"]
    empty_value_display = "unknown"
    form = forms.DatacenterUpdateForm
admin.site.register(Datacenter, DatacenterAdmin)

class PartitionAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created')
    history_list_display = ["name","serveur","stockage"]
    search_fields = ["name","serveur__name","stockage__name"]
    empty_value_display = "unknown"
    form = forms.PartitionUpdateForm
admin.site.register(Partition, PartitionAdmin)

class DeploiementClusterAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created')
    history_list_display = ["serveur","cluster"]
    search_fields = ["serveur__name","cluster__name","serveur__networks_interfaces__name","serveur__networks_interfaces__ip_addresses__ipv4","cluster__ip_address__ipv4"]
    empty_value_display = "unknown"
    form = forms.DeploiementClusterUpdateForm
admin.site.register(DeploiementCluster, DeploiementClusterAdmin)


