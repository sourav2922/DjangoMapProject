from django.conf import settings
from django.shortcuts import render

# Create your views here.

def index(request):
  """ Import Google API Key & Creates Initial Homepage View """
  api_key = getattr(settings, 'AIzaSyDKfMN8F-5SX48iuH8EApAsHQgWmIfjuPY')
  context = {
    'api_key': api_key
  }
  return render(request, 'djangomapapp/index.html', context)
