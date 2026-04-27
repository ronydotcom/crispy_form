from django.db import models

class ProductModel(models.Model):
    PRODUCT_CATEGORY=[
        ('Electronics','Electronics'),
        ('Clothing','Clothing'),
        ('Books','Books'),
    ]
    name=models.CharField(max_length=100,null=True)
    product_price=models.FloatField(null=True)
    qty=models.PositiveIntegerField(null=True)
    total_price=models.FloatField(null=True)
    description=models.TextField(null=True)
    category=models.CharField(max_length=100,choices=PRODUCT_CATEGORY,null=True)
    image=models.ImageField(upload_to='product_images/',null=True,blank=True)

    def __str__(self):
        return f'{self.name}'
