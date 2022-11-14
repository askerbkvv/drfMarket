from django.contrib.auth.models import AbstractUser
from django.db import models
from products.models import Product


CHOISES = (
    ('ADMIN', 'admin'),
    ('CLIENT', 'client')
)


class User(AbstractUser):
    heart = models.ManyToManyField(Product, blank=True, related_name='favarite')
    type = models.CharField(max_length=20, choices=CHOISES, default='client')
