from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import AppType, BackupStrategie, Application,SystemeStockage, Vendor, ModuleApplicatif,Server,Departement,Rack,ServerRoom,Datacenter,Partition,DeploiementCluster,Database,DatabaseServer
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import CustomUserUpdateForm
from base.forms import BackupStrategieUpdateForm
from base import forms
from accounts.models import User
# Register your models here.
#@admin.register(BackupStrategie)



class UserAdmin(BaseUserAdmin):
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

admin.site.register(Vendor)
admin.site.register(ModuleApplicatif)
admin.site.register(Server)
admin.site.register(Rack)
admin.site.register(ServerRoom)

admin.site.register(Datacenter)
admin.site.register(Partition)

admin.site.register(DeploiementCluster)
#admin.site.register(Departement)
#register(BackupStrategie)