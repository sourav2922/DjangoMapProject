from django.shortcuts import render

# Create your views here.

def index(request):
  """ Creates Initial Homepage View """
  return render(request, 'djangomapapp/index.html')