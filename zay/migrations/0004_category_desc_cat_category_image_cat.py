# Generated by Django 5.0.2 on 2024-03-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zay', '0003_order_status_payment_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc_cat',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='category',
            name='image_cat',
            field=models.ImageField(blank=True, default='', upload_to='category_images/'),
        ),
    ]
