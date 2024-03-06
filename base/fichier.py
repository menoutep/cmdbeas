class DeploiementClusterAdmin(SimpleHistoryAdmin):
    list_filter = ('updated','created')
    history_list_display = ["serveur","cluster"]
    search_fields = ["serveur__name","cluster__name","serveur__networks_interfaces__name","serveur__networks_interfaces__ip_addresses__ipv4","cluster__ip_address__ipv4"]
    empty_value_display = "unknown"
    form = forms.DeploiementClusterUpdateForm
admin.site.register(DeploiementCluster, DeploiementClusterAdmin)