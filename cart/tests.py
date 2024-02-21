from django.test import TestCase
from . models import Product
from . models import CartItem
from . models import Billing

# Create your tests here.

class ProductTestCase(TestCase): #testing the product model

    def setUp(self):
        product = Product.objects.create(name='pen', description='this is a blue pen', price='120', image='pen.jpeg')
        
    def test_product(self):
        product = Product.objects.all().count()
        self.assertEqual(product, 1)


class CartItemTestCase(TestCase): #testing the CartItem model

    def setUp(self):
        cart = CartItem.objects.create(quantity='3')

    def test_cart(self):
        cart  = CartItem.objects.filter(quantity='3')
        self.assertTrue(cart)


class BillingTestCase(TestCase): #testing the billig address
    
    def setUp(self):
        billing = Billing.objects.create(firstname='tinny', lastname='keino',phone_number='0793930123', email='keino@gmail.com', address1='keino street', address2='nyerere street',city='nairobi', constituency='dagoretti south', postal_code='00100')


    def test_billing(self):
        billing = Billing.objects.filter(city='kisumu').exists()
        self.assertFalse(billing)