from django.shortcuts import render
from .models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
# def categorie(request):
# 	categorie = Category.objects.all()
# 	bypage = Paginator(categorie, 3)
# 	page = request.GET.get('page')
# 	cat_page = bypage.get_page(page)

# 	context = { 'category_paged' : cat_page }
# 	return render(request, 'home.html', context)

