from django.urls import path
from .views import ServiceListView, ServiceCreateView, ServiceUpdateView, ServiceDeleteView, ServiceDetaileView, ServiceView

urlpatterns = [
    path('service/list', ServiceListView.as_view(), name='service_list'),
    path('service/create', ServiceCreateView.as_view(), name='add_service'),
    path('service/<int:pk>/update', ServiceUpdateView.as_view(), name='update_service'),
    path('service/<int:pk>/detail', ServiceDetaileView.as_view(), name='service_detail'),
    path('service/<int:pk>/delete', ServiceDeleteView.as_view(), name='delete_service'),
    path('api/service/list', ServiceView.as_view())
]
