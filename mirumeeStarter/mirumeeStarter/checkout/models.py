from django.db import models
from ..product.models import ProductVariant
from django.contrib.auth.models import User 

class CheckoutLine(models.Model):
    variant = models.ForeignKey(ProductVariant, related_name="product_variant", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False)

class Checkout(models.Model):
    user = models.ForeignKey(User, related_name="users", on_delete=models.PROTECT)
    lines = models.ForeignKey(CheckoutLine, related_name='checkout_line', on_delete=models.DO_NOTHING)
    user_email = models.EmailField(null=False, blank=False)


    
