from django.contrib import admin
from .models import Daily_Pizza
# Register your models here.

class Daily_Pizza_Admin(admin.ModelAdmin):
	list_display = ('daily_pizza_name', 'ingredients', 'price', 'is_available')
	prepopulated_fields = {'slug': ('daily_pizza_name',)}

admin.site.register(Daily_Pizza, Daily_Pizza_Admin)
