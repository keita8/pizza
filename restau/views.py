from django.shortcuts import render
from django.http import HttpResponse
from daily_pizza.models import Daily_Pizza


def home(request):
	return render(request, 'home.html')


# def dialy(request):
# 	daily = Daily_Pizza.objects.all()
# 	context = {'daily':daily}
# 	return render(request, 'home.html', context)
