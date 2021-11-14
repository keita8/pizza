from django.db import models
from category.models import Category

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=100, unique=True, verbose_name='Nom du produit')
	slug         = models.SlugField(max_length=100, unique=True)
	description  = models.TextField(max_length=500, blank=True)
	price        = models.FloatField(default=0.0, verbose_name="Prix")
	images       = models.ImageField(upload_to='photos/produits')
	stock        = models.IntegerField()
	is_available = models.BooleanField(default=True, verbose_name='Disponible')
	category       = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categorie")
	created_date   = models.DateTimeField(auto_now_add=True, verbose_name = "Creation")
	modified_date  = models.DateTimeField(auto_now=True, verbose_name = "Modification")

	class Meta:
		verbose_name = 'Produit'
		verbose_name_plural = 'Produits'

	def __str__(self):
		return self.product_name
