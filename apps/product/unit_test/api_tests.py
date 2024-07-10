from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.product.models import Product
from apps.product.api.serializers import ProductSerializer


# UNIT TEST PER LE API
class ProductAPITestCase(APITestCase):

    def setUp(self):
        # Creazione istanza per test
        self.product_data = {
            'name': 'Test Product',
            'price': '99.99'
        }
        self.product = Product.objects.create(name='Existing Product', price='49.99')

    def test_get_product_list(self):
        url = reverse('product-api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_product(self):
        url = reverse('product-api')
        response = self.client.post(url, self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_create_product_invalid_data(self):
        invalid_data = {
            'name': 'Invalid Product',
        }
        url = reverse('product-api')
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

