from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import Propietario, Mascota, ConsultaVeterinaria


class MascotaSerializerTests(APITestCase):
    def setUp(self):
        self.propietario = Propietario.objects.create(
            identificacion='1-1111-1111',
            nombre='Propietario de Prueba',
            telefono='8888-8888',
            email='prueba@test.com'
        )

    def test_crear_mascota_peso_invalido(self):
        url = reverse('mascota-list-create')
        data = {
            'nombre': 'Firulais',
            'especie': 'Perro',
            'peso': -5,
            'propietario': self.propietario.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_crear_mascota_valida(self):
        url = reverse('mascota-list-create')
        data = {
            'nombre': 'Firulais',
            'especie': 'Perro',
            'peso': 12.5,
            'propietario': self.propietario.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PerfilEndpointTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='usuario1', password='Vetclinica2026')
        self.token = Token.objects.create(user=self.user)

    def test_perfil_sin_token(self):
        url = reverse('perfil')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_perfil_con_token(self):
        url = reverse('perfil')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EstadisticasEndpointTests(APITestCase):
    def setUp(self):
        self.user_regular = User.objects.create_user(username='usuario1', password='Vetclinica2026')
        self.token_regular = Token.objects.create(user=self.user_regular)

        self.admin = User.objects.create_user(username='admin1', password='AdminVet2026', is_staff=True)
        self.token_admin = Token.objects.create(user=self.admin)

    def test_estadisticas_usuario_regular_prohibido(self):
        url = reverse('estadisticas')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_regular.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_estadisticas_admin_permitido(self):
        url = reverse('estadisticas')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_admin.key)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SesionEndpointTests(APITestCase):
    def test_contador_incrementa(self):
        url = reverse('sesion')
        response1 = self.client.get(url)
        response2 = self.client.get(url)
        self.assertEqual(response1.data['contador'], 1)
        self.assertEqual(response2.data['contador'], 2)