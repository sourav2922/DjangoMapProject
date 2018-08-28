from django.conf.urls import url
from DjangoMapApp import views

urlpatterns = [
  url(r'^$', views.index, name='home'),
]
