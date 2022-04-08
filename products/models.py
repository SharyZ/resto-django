from datetime import datetime

from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product/images/%Y/%m/%d/')
    small_description = models.TextField(
        max_length=130, help_text='Description length must not exceed 130')
    price = models.IntegerField(help_text='Price in UZS :)')
    created_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(
        'categories.Category', related_name='products', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
