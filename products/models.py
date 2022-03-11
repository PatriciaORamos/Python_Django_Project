from django.db import models
from categories import models as categories

# Create your models here.
class Product(models.Model):
  category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  quantity = models.IntegerField(default=0)
  sku = models.CharField(max_length=50)
  picture = models.ImageField(default='default.png', blank=True)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  def snippet(self):
    return self.description[:50] + '...'