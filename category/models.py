from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	category_name = models.CharField('Nom Categorie', max_length=100, blank=True)
	slug          = models.SlugField(max_length=200 ,unique=True)
	description   = models.TextField(max_length=200, blank=True)
	images        = models.ImageField(upload_to='photos/categorie', blank=True)


	class Meta:
		verbose_name = 'Categorie'
		verbose_name_plural = 'Categories'

	def get_url(self):
		return reverse('product_by_category', args=[self.slug])


	def __str__(self):
		return self.category_name
