from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Provider
from django.contrib.auth.models import User


class ProviderViewSetTests(APITestCase):
    def setUp(self):
        self.provider_url = reverse('provider-list')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        self.providers = [
            Provider.objects.create(name='ShuttleExpress', email='contact@shuttleexpress.com', 
                                    phone_number='+12025550123', language='English', currency='USD'),
            Provider.objects.create(name='CityTransfers', email='info@citytransfers.com', 
                                    phone_number='+442071838888', language='English', currency='GBP'),
            Provider.objects.create(name='FastTravel', email='support@fasttravel.com', 
                                    phone_number='+33123456789', language='French', currency='EUR'),
            Provider.objects.create(name='GoRide', email='service@goride.com', 
                                    phone_number='+819012345678', language='Japanese', currency='JPY')
        ]

    def test_create_provider(self):
        data = {
            'name': 'Test Provider',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'language': 'English',
            'currency': 'USD',
        }
        response = self.client.post(self.provider_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), len(self.providers) + 1)
        self.assertEqual(Provider.objects.get(name='Test Provider').email, 'test@example.com')

    def test_get_providers(self):
        response = self.client.get(self.provider_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.providers))

    def test_update_provider(self):
        provider = self.providers[0]
        update_url = reverse('provider-detail', args=[provider.id])
        data = {
            'name': 'Updated Provider',
            'email': 'updated@example.com',
            'phone_number': '0987654321',
            'language': 'Spanish',
            'currency': 'EUR',
        }
        response = self.client.put(update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        provider.refresh_from_db()
        self.assertEqual(provider.name, 'Updated Provider')
        self.assertEqual(provider.email, 'updated@example.com')

    def test_delete_provider(self):
        provider = self.providers[0]
        delete_url = reverse('provider-detail', args=[provider.id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Provider.objects.count(), len(self.providers) - 1)
        self.assertRaises(Provider.DoesNotExist, Provider.objects.get, id=provider.id)
