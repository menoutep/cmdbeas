from django.contrib import admin
from .models import AppType, BackupStrategie, Application,SystemeStockage, Vendor, ModuleApplicatif,Server,Departement,Rack,ServerRoom,Datacenter,Partition,DeploiementCluster,Database,DatabaseServer
from simple_history.admin import SimpleHistoryAdmin

from accounts.models import User
# Register your models here.
#@admin.register(BackupStrategie)
class BackupStrategieAdmin(SimpleHistoryAdmin):
    #list_display = ('name', 'file', 'updated', 'created', 'history_change_reason')
    history_list_display = ["file"]
    search_fields = ['name', 'file']
    #history_list_display = ('history_change_reason')
admin.site.register(BackupStrategie, BackupStrategieAdmin)
class DepartementAdmin(SimpleHistoryAdmin):
    #list_display = ('name', 'file', 'updated', 'created', 'history_change_reason')
    history_list_display = ["name","description"]
    search_fields = ['name']
    #history_list_display = ('history_change_reason')
admin.site.register(Departement, DepartementAdmin)
admin.site.register(User)
admin.site.register(AppType)
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