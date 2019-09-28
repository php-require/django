from django.http import HttpResponse

def index(request):
	return HttpResponse("Hi every body!")

def test(request):
	return HttpResponse("Yahooo!")