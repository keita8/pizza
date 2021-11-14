from .models import Daily_Pizza

def daily(request):
	daily_pizza = Daily_Pizza.objects.all()

	return dict(daily_pizza=daily_pizza)