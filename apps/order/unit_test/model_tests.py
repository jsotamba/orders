from django.test import TestCase

from datetime import date
from django.utils import timezone

from apps.order.models import Order
from apps.product.models import Product


# CREAZIONI TEST UNITARI PER I MODELS
class OrdersTestCase(TestCase):
    def setUp(self):
        # Creazione di istanze di oggetti necessari per i unit_test
        self.product1 = Product.objects.create(name='Product 1', price=100)
        self.product2 = Product.objects.create(name='Product 2', price=50)
        self.order = Order.objects.create(
            name='Test Order',
            description='Test description',
            date=date(2023, 1, 1)
        )
        self.order.products.add(self.product1, self.product2)

    def test_order_creation(self):
        # Verifica che l'ordine sia stato creato correttamente
        self.assertEqual(self.order.name, 'Test Order')
        self.assertEqual(self.order.description, 'Test description')
        self.assertEqual(self.order.date, date(2023, 1, 1))

    def test_order_str_method(self):
        # Verifica che il metodo __str__ restituisca il nome dell'ordine
        self.assertEqual(str(self.order), 'Test Order')

    def test_order_has_products(self):
        # Verifica che l'ordine abbia correttamente i prodotti associati
        self.assertEqual(self.order.products.count(), 2)
        self.assertIn(self.product1, self.order.products.all())
        self.assertIn(self.product2, self.order.products.all())

    def test_order_date_default(self):
        # Verifico che la data dell'ordine sia impostata correttamente al valore di default
        new_order = Order.objects.create(name='New Order', description='New description')
        self.assertEqual(new_order.date, timezone.now())

    def test_order_verbose_name_plural(self):
        # Verifico il verbose name plurale del modello
        self.assertEqual(str(Order._meta.verbose_name_plural), 'Orders')

    def test_order_ordering(self):
        # Verifico l'ordinamento degli ordini per data
        orders = Order.objects.all()
        self.assertEqual(list(orders), list(Order.objects.order_by('date')))

    def test_order_add_product(self):
        # Verifico l'aggiunta di un prodotto a un ordine
        new_product = Product.objects.create(name='New Product', price=75)
        self.order.products.add(new_product)
        self.assertIn(new_product, self.order.products.all())

    def test_order_remove_product(self):
        # Verifico la rimozione di un prodotto da un ordine
        self.order.products.remove(self.product1)
        self.assertNotIn(self.product1, self.order.products.all())
