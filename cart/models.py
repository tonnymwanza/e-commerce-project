from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    City = (
        ('nrb', 'Nairobi'),
        ('mbs', 'Mombasa'),
        ('ksm', 'Kisumu'),
        ('eldy', 'Eldoret')
    )
    Constituency = (
        ('dgts', 'Dagoretti south'),
        ('dgtn', 'Dagoretti north'),
        ('thk', 'Thika'),
        ('kmb', 'Kiambu'),
        ('ktl', 'Kitengela'),
        ('kky', 'kikuyu'),
        ('klm', 'Kilimani')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=50, null=True, verbose_name='your first name')
    lastname = models.CharField(max_length=50, null=True, verbose_name='your last name')
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    address1 = models.CharField(max_length=255, null=True)
    address2 = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=7,choices=City ,null=True,)
    constituency = models.CharField(max_length=15, choices=Constituency, null=True, blank=True)
    country = CountryField(null=True, blank=False)
    postal_code = models.IntegerField(null=True)

    def __str__(self):
        return self.firstname

    
    def item_total(self):
        return self.quantity * self.product.price
    
    def item_subtotal(self):
        total = self.quantity * self.product.price
        total += 1
        return total


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)
    bio = models.TextField()

# user = User

# @receiver(post_save, sender='cart.User')
# def post_save_receiver(sender,user, instance, *args, **kwargs):
#     profile = Profile.objects.create(user=instance)