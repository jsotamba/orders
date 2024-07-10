from django.test import TestCase

from apps.product.models import Product


# CREAZIONI TEST UNITARI PER I MODELS
class ProductModelTestCase(TestCase):

    def setUp(self):
        # Creazione di un'istanza per i unit_test
        self.product = Product.objects.create(name='Test Product', price=99.99)

    def test_product_creation(self):
        # Verifico che il prodotto sia stato creato correttamente
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.price, 99.99)

    def test_product_str_method(self):
        # Verifico che il metodo __str__ restituisca il nome del prodotto
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_verbose_name_plural(self):
        # Verifico il verbose name plurale del modello
        self.assertEqual(str(Product._meta.verbose_name_plural), 'Products')

    def test_product_ordering(self):
        # Verifica l'ordinamento dei prodotti per nome
        products = Product.objects.all()
        self.assertEqual(list(products), list(Product.objects.order_by('name')))