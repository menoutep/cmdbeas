
class ProcessListView(ListView):
    model = Process
    template_name = 'integration/process_list.html'
    context_object_name = 'processes'
class ProcessDetailView(DetailView):
    model = Process
    template_name = 'integration/process_detail.html'
    context_object_name = 'process'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ProcessSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ProcessCreateView(CreateView):
    model = Process
    form_class = ProcessForm
    template_name = 'integration/process_form.html'
    success_url = reverse_lazy('base:process-list')
class ProcessUpdateView(UpdateView):
    model = Process
    form_class = ProcessUpdateForm
    template_name = 'integration/process_form.html'
    success_url = reverse_lazy('base:process-list')
class ProcessDeleteView(DeleteView):
    model = Process
    template_name = 'integration/process_confirm_delete.html'
    success_url = reverse_lazy('base:process-list')
class SubProcessListView(ListView):
    model = SubProcess
    template_name = 'integration/sub_process_list.html'
    context_object_name = 'sub_processes'
class SubProcessDetailView(DetailView):
    model = SubProcess
    template_name = 'integration/sub_process_detail.html'
    context_object_name = 'sub_process'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = SubProcessSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class SubProcessCreateView(CreateView):
    model = SubProcess
    form_class = SubProcessForm
    template_name = 'integration/sub_process_form.html'
    success_url = reverse_lazy('base:sub_process-list')
class SubProcessUpdateView(UpdateView):
    model = SubProcess
    form_class = SubProcessUpdateForm
    template_name = 'integration/sub_process_form.html'
    success_url = reverse_lazy('base:sub_process-list')
class SubProcessDeleteView(DeleteView):
    model = SubProcess
    template_name = 'integration/sub_process_confirm_delete.html'
    success_url = reverse_lazy('base:sub_process-list')
class UseCaseListView(ListView):
    model = UseCase
    template_name = 'integration/use_case_list.html'
    context_object_name = 'use_cases'
class UseCaseDetailView(DetailView):
    model = UseCase
    template_name = 'integration/use_case_detail.html'
    context_object_name = 'use_case'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = UseCaseSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class UseCaseCreateView(CreateView):
    model = UseCase
    form_class = UseCaseForm
    template_name = 'integration/use_case_form.html'
    success_url = reverse_lazy('base:use_case-list')
class UseCaseUpdateView(UpdateView):
    model = UseCase
    form_class = UseCaseUpdateForm
    template_name = 'integration/use_case_form.html'
    success_url = reverse_lazy('base:use_case-list')
class UseCaseDeleteView(DeleteView):
    model = UseCase
    template_name = 'integration/use_case_confirm_delete.html'
    success_url = reverse_lazy('base:use_case-list')
class ApiListView(ListView):
    model = Api
    template_name = 'integration/api_list.html'
    context_object_name = 'apis'
class ApiDetailView(DetailView):
    model = Api
    template_name = 'integration/api_detail.html'
    context_object_name = 'api'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = ApiSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class ApiCreateView(CreateView):
    model = Api
    form_class = ApiForm
    template_name = 'integration/api_form.html'
    success_url = reverse_lazy('base:api-list')
class ApiUpdateView(UpdateView):
    model = Api
    form_class = ApiUpdateForm
    template_name = 'integration/api_form.html'
    success_url = reverse_lazy('base:api-list')
class ApiDeleteView(DeleteView):
    model = Api
    template_name = 'integration/api_confirm_delete.html'
    success_url = reverse_lazy('base:api-list')
class AppelApiListView(ListView):
    model = AppelApi
    template_name = 'integration/appel_api_list.html'
    context_object_name = 'appel_apis'
class AppelApiDetailView(DetailView):
    model = AppelApi
    template_name = 'integration/appel_api_detail.html'
    context_object_name = 'appel_api'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            serializer = AppelApiSerializer(self.object)
            serializer_data=json.dumps(serializer.data)
            context['serializer_data'] = serializer_data
            return context
class AppelApiCreateView(CreateView):
    model = AppelApi
    form_class = AppelApiForm
    template_name = 'integration/appel_api_form.html'
    success_url = reverse_lazy('base:appel_api-list')
class AppelApiUpdateView(UpdateView):
    model = AppelApi
    form_class = AppelApiUpdateForm
    template_name = 'integration/appel_api_form.html'
    success_url = reverse_lazy('base:appel_api-list')
class AppelApiDeleteView(DeleteView):
    model = AppelApi
    template_name = 'integration/appel_api_confirm_delete.html'
    success_url = reverse_lazy('base:appel_api-list')
