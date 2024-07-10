from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.order.models import Order
from apps.product.models import Product


class OrderAPITestCase(APITestCase):

    def setUp(self):
        # Creazione product di esempio per i test
        self.product = Product.objects.create(name='Test Product', price=99.99).id

        # Creazione ordine di esempio per i test
        self.order_data = {
            'name': 'Test Order',
            'description': 'Test Description',
            'date': '2024-07-10',
            'products': [self.product],
        }
        self.order = Order.objects.create(name='Existing Order', description='Existing Description', date='2024-07-09')
        self.order.products.add(self.product)

    # verifico la list dell'api
    def test_get_order_list(self):
        url = reverse('order_api_view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # verifica della creazione di un order
    def test_create_order(self):
        url = reverse('order_api_view')
        post_data = {
            'name': 'Swagger Order',
            'description': 'Swagger Description',
            'date': '2024-07-10',
            'products': [self.product]
        }
        response = self.client.post(url, post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # verifica della creazione e del conteggio degli ordini
    def test_create_and_count_orders(self):
        url = reverse('order_api_view')
        response = self.client.post(url, self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)

    # verifica modifica di un ordine
    def test_update_order(self):
        url = reverse('order_detail_api_view', args=[self.order.id])
        update_data = {
            'name': 'Updated Order',
            'description': 'Updated Description',
            'date': '2024-07-10',
            'products': [self.product]
        }
        response = self.client.put(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_order = Order.objects.get(id=self.order.id)
        self.assertEqual(updated_order.name, 'Updated Order')
        self.assertEqual(updated_order.description, 'Updated Description')

    # verifica cancellazione di un ordine
    def test_delete_order(self):
        url = reverse('order_detail_api_view', args=[self.order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)

    # verifica valicazione mancanza campo description
    def test_create_order_invalid_data(self):
        # Manca il campo description
        invalid_data = {
            'name': 'Invalid Order',
        }
        url = reverse('order_api_view')
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # verifica validazione mancanza campo products
    def test_create_order_missing_products(self):
        invalid_data = {
            'name': 'Missing Products Order',
            'description': 'Order without products',
            'date': '2024-07-10'
        }
        url = reverse('order_api_view')
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('products', response.data)  # Assicurati che 'products' sia un campo richiesto
