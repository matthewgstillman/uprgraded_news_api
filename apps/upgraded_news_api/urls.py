from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^bbc$', views.bbc, name="bbc"),
    url(r'^foxnews$', views.foxnews, name="foxnews"),
    url(r'^nytimes$', views.nytimes, name="nytimes"),
]