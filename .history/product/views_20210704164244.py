from django.shortcuts import render, get_object_or_404
from category.models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Product

# Create your views here.
def store(request, category_slug=None):
	category = None
	product = None

	if category_slug != None:
		category 	  = get_object_or_404(Category, slug=category_slug)
		products 	  = Product.objects.all().filter(category=category, is_available=True)
		bypage   	  = Paginator(products, 3)
		page     	  = request.GET.get('page')
		paged_product = bypage.get_page(page)
		page_count    = paged_product.count()
	else:
		products      = Product.objects.all().filter(is_available=True).order_by('id')
		bypage   	  = Paginator(products, 3)
		page     	  = request.GET.get('page')
		paged_product = bypage.get_page(page)
		page_count    = paged_product.count()

	context = {

		'products'   : paged_product,
		'page_count' : page_count
	}

	return render(request, 'home.html', context)

