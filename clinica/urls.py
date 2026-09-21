from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('api/mascotas/', views.MascotaListCreateView.as_view(), name='mascota-list-create'),
    path('api/mascotas/<int:pk>/', views.MascotaDetailView.as_view(), name='mascota-detail'),

    path('api/propietarios/', views.PropietarioListCreateView.as_view(), name='propietario-list-create'),

    path('api/consultas/', views.ConsultaListCreateView.as_view(), name='consulta-list-create'),

    path('api/token/', obtain_auth_token, name='api-token'),

    path('api/perfil/', views.perfil, name='perfil'),
    path('api/estadisticas/', views.estadisticas, name='estadisticas'),
    path('api/sesion/', views.sesion, name='sesion'),
]