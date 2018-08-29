from django.conf import settings
from django.shortcuts import render

# Create your views here.

def index(request):
  """ Import Google API Key & Creates Initial Homepage View """
  api_key = getattr(settings, 'GOOGLE_MAPS_API_KEY')
  context = {
    'api_key': api_key
  }
  return render(request, 'djangomapapp/index.html', context)