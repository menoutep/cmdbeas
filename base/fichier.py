class MobileAppListView(ListView):
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

class MobileAppDetailView(DetailView):
    model = MobileApp
    template_name = 'channels/mobile_app_detail.html'
    context_object_name = 'mobile_app'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = MobileAppSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class MobileAppCreateView(CreateView):
    model = MobileApp
    template_name = 'channels/mobile_app_form.html'
    form_class = MobileAppCreateForm
    success_url = reverse_lazy('base:mobile_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class MobileAppUpdateView(UpdateView):
    model = MobileApp
    template_name = 'channels/mobile_app_form.html'
    form_class = MobileAppUpdateForm
    success_url = reverse_lazy('base:mobile_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class MobileAppDeleteView(DeleteView):
    model = MobileApp
    template_name = 'channels/mobile_app_confirm_delete.html'
    success_url = reverse_lazy('mobile_app-list')

class DesktopAppListView(ListView):
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

class DesktopAppDetailView(DetailView):
    model = DesktopApp
    template_name = 'channels/desktop_app_detail.html'
    context_object_name = 'desktop_app'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = DesktopAppSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class DesktopAppCreateView(CreateView):
    model = DesktopApp
    template_name = 'channels/desktop_app_form.html'
    form_class = DesktopAppCreateForm
    success_url = reverse_lazy('base:desktop_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DesktopAppUpdateView(UpdateView):
    model = DesktopApp
    template_name = 'channels/desktop_app_form.html'
    form_class = DesktopAppUpdateForm
    success_url = reverse_lazy('base:desktop_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class DesktopAppDeleteView(DeleteView):
    model = DesktopApp
    template_name = 'channels/desktop_app_confirm_delete.html'
    success_url = reverse_lazy('desktop_app-list')

class UrlListView(ListView):
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

class UrlDetailView(DetailView):
    model = Url
    template_name = 'channels/url_detail.html'
    context_object_name = 'url'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = UrlSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class UrlCreateView(CreateView):
    model = Url
    template_name = 'channels/url_form.html'
    form_class = UrlCreateForm
    success_url = reverse_lazy('base:url-list')
    def form_valid(self, form):
        return super().form_valid(form)

class UrlUpdateView(UpdateView):
    model = Url
    template_name = 'channels/url_form.html'
    form_class = UrlUpdateForm
    success_url = reverse_lazy('base:url-list')
    def form_valid(self, form):
        return super().form_valid(form)

class UrlDeleteView(DeleteView):
    model = Url
    template_name = 'channels/url_confirm_delete.html'
    success_url = reverse_lazy('url-list')

class SmppAccountListView(ListView):
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

class SmppAccountDetailView(DetailView):
    model = SmppAccount
    template_name = 'channels/smpp_account_detail.html'
    context_object_name = 'smpp_account'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = SmppAccountSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class SmppAccountCreateView(CreateView):
    model = SmppAccount
    template_name = 'channels/smpp_account_form.html'
    form_class = SmppAccountCreateForm
    success_smpp_account = reverse_lazy('base:smpp_account-list')
    def form_valid(self, form):
        return super().form_valid(form)

class SmppAccountUpdateView(UpdateView):
    model = SmppAccount
    template_name = 'channels/smpp_account_form.html'
    form_class = SmppAccountUpdateForm
    success_smpp_account = reverse_lazy('base:smpp_account-list')
    def form_valid(self, form):
        return super().form_valid(form)

class SmppAccountDeleteView(DeleteView):
    model = SmppAccount
    template_name = 'channels/smpp_account_confirm_delete.html'
    success_smpp_account = reverse_lazy('smpp_account-list')

class SmsShortCodeListView(ListView):
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

class SmsShortCodeDetailView(DetailView):
    model = SmsShortCode
    template_name = 'channels/sms_short_code_detail.html'
    context_object_name = 'sms_short_code'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = SmsShortCodeSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class SmsShortCodeCreateView(CreateView):
    model = SmsShortCode
    template_name = 'channels/sms_short_code_form.html'
    form_class = SmsShortCodeCreateForm
    success_sms_short_code = reverse_lazy('base:sms_short_code-list')
    def form_valid(self, form):
        return super().form_valid(form)

class SmsShortCodeUpdateView(UpdateView):
    model = SmsShortCode
    template_name = 'channels/sms_short_code_form.html'
    form_class = SmsShortCodeUpdateForm
    success_sms_short_code = reverse_lazy('base:sms_short_code-list')
    def form_valid(self, form):
        return super().form_valid(form)

class SmsShortCodeDeleteView(DeleteView):
    model = SmsShortCode
    template_name = 'channels/sms_short_code_confirm_delete.html'
    success_sms_short_code = reverse_lazy('sms_short_code-list')

class UssdShortCodeListView(ListView):
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

class UssdShortCodeDetailView(DetailView):
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_detail.html'
    context_object_name = 'ussd_short_code'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = UssdShortCodeSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class UssdShortCodeCreateView(CreateView):
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_form.html'
    form_class = UssdShortCodeCreateForm
    success_ussd_short_code = reverse_lazy('base:ussd_short_code-list')
    def form_valid(self, form):
        return super().form_valid(form)

class UssdShortCodeUpdateView(UpdateView):
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_form.html'
    form_class = UssdShortCodeUpdateForm
    success_ussd_short_code = reverse_lazy('base:ussd_short_code-list')
    def form_valid(self, form):
        return super().form_valid(form)

class UssdShortCodeDeleteView(DeleteView):
    model = UssdShortCode
    template_name = 'channels/ussd_short_code_confirm_delete.html'
    success_ussd_short_code = reverse_lazy('ussd_short_code-list')

class ConnexionAppListView(ListView):
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

class ConnexionAppDetailView(DetailView):
    model = ConnexionApp
    template_name = 'channels/connexion_app_detail.html'
    context_object_name = 'connexion_app'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ConnexionAppSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context

class ConnexionAppCreateView(CreateView):
    model = ConnexionApp
    template_name = 'channels/connexion_app_form.html'
    form_class = ConnexionAppCreateForm
    success_connexion_app = reverse_lazy('base:connexion_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ConnexionAppUpdateView(UpdateView):
    model = ConnexionApp
    template_name = 'channels/connexion_app_form.html'
    form_class = ConnexionAppUpdateForm
    success_connexion_app = reverse_lazy('base:connexion_app-list')
    def form_valid(self, form):
        return super().form_valid(form)

class ConnexionAppDeleteView(DeleteView):
    model = ConnexionApp
    template_name = 'channels/connexion_app_confirm_delete.html'
    success_connexion_app = reverse_lazy('connexion_app-list')

#################################end Channels views############################################
