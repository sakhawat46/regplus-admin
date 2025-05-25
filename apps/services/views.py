from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework.generics import ListAPIView
from web_project import TemplateLayout
from django.urls import reverse_lazy
from .serializers import ServiceSerializer
from .models import Service
from .forms import ServiceForm


class ServiceListView(ListView):
    model = Service
    template_name = 'service-list.html'
    context_object_name = 'services'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Initialize your TemplateLayout if needed
        context = TemplateLayout.init(self, context)

        # Add additional pagination context
        if context.get('page_obj'):
            context['services'] = context['page_obj'] 
        return context

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'edit.html'
    success_url = reverse_lazy('service_list')
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

class ServiceUpdateView(UpdateView):
    model = Service
    fmodel = Service
    form_class = ServiceForm
    template_name = 'edit.html'
    success_url = reverse_lazy('service_list')
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

class ServiceDeleteView(DeleteView):
    model = Service
    success_url = reverse_lazy('service_list')

class ServiceDetaileView(DetailView):
    model = Service
    template_name = 'service-detail.html'
    context_object_name = 'service'
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context

class ServiceView(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
