from django.db import models

# Create your models here.
class Daily_Pizza(models.Model):
	title            = models.CharField(max_length=200, blank=True)
	daily_pizza_name = models.CharField(max_length=200, blank=True, verbose_name='Pizza du jour')
	slug             = models.SlugField(max_length=200, blank=True)
	price            = models.FloatField(default=0.0, verbose_name='Prix')
	image            = models.ImageField(upload_to='photos/daily_pizza')
	ingredients      = models.TextField(max_length=500)
	is_available     = models.BooleanField(default=True)


	class Meta:
		verbose_name = 'Pizza du jour'
		verbose_name_plural = 'Pizza du jour'

	def __str__(self):
		return self.daily_pizza_name
