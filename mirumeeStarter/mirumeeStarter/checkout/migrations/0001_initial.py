# Generated by Django 3.2.1 on 2021-05-25 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckoutLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant', to='product.productvariant')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('lines', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='checkout_line', to='checkout.checkoutline')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
