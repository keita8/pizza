from django.shortcuts import render
from .models import Daily_Pizza
from django.http import HttpResponse

#Create your views here.
def daily(request):
	daily = Daily_Pizza.objects.all()

	context = {'daily': daily}
	return render(request, 'home.html', context)

