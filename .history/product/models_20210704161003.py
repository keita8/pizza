from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
	product_name = models.CharField('Produit', max_length=200, blank=True, unique=True)
	slug 		 = models.SlugField(max_length=200, blank=True)
	ingredients  = models.TextField(max_length=200, blank=True)
	price 		 = models.FloatField('Prix', default=0.0)
	images       = models.ImageField(upload_to='photos/produits')
	stock        = models.IntegerField(default=0)
	is_available = models.BooleanField(default=True)
	category     = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='categorie')


	class Meta:
		verbose_name = 'Produit'
		verbose_name_plural = 'Produits'

	def __str__(self):
		return self.product_name