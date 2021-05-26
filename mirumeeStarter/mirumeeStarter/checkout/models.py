from django.db import models
from ..product.models import ProductVariant
from django.contrib.auth.models import User 

class Checkout(models.Model):
    user = models.ForeignKey(User, related_name="users", on_delete=models.PROTECT)
    user_email = models.EmailField(null=False, blank=False)

class CheckoutLine(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)
    checkout = models.ForeignKey(Checkout, related_name="lines", on_delete=models.CASCADE)

    
