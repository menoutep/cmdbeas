from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import AppType, BackupStrategie, Application,SystemeStockage, Vendor, ModuleApplicatif,Server,Departement,Rack,ServerRoom,Datacenter,Partition,DeploiementCluster,Database,DatabaseServer
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.forms import CustomUserUpdateForm
from base.forms import BackupStrategieUpdateForm
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
    list_filter = ('name', 'file', 'updated')
    history_list_display = ["file"]
    search_fields = ['name', 'file','applications__name']
    empty_value_display = "unknown"
    form = BackupStrategieUpdateForm
admin.site.register(BackupStrategie, BackupStrategieAdmin)
class DepartementAdmin(SimpleHistoryAdmin):
    list_filter = ('name','updated','created')
    history_list_display = ["name","description","users_name"]
    search_fields = ["name","description","users_name"]
admin.site.register(Departement, DepartementAdmin)

class AppTypeAdmin(SimpleHistoryAdmin):
    list_filter = ('name','updated','created')
    history_list_display = ["name","description","applications_name"]
    search_fields = ["name","description","applications_name"]
admin.site.register(AppType, AppTypeAdmin)

#####Application start######################

#####Application end#############################

#admin.site.register(BackupStrategie)
admin.site.register(Application)
admin.site.register(Database)
admin.site.register(DatabaseServer)
admin.site.register(SystemeStockage)
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