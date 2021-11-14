from .models import Category

def category_menu(request):
	link = Category.objects.all()
	return dict(link=link)
	