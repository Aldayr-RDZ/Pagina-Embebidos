from django.urls import path
from alarmas.api.api import alarma_api_view, alarma_detail_view


urlpatterns = [
    path('alarma/',alarma_api_view, name='alarma_api') ,
    path('alarma/<int:pk>/', alarma_detail_view, name= 'alarma_detail_api_view')
]