from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^abc$', views.abc, name="abc"),
    url(r'^ap$', views.ap, name="ap"),
    url(r'^bbc$', views.bbc, name="bbc"),
    url(r'^bleacherreport$', views.bleacherreport, name="bleacherreport"),
    url(r'^bloomberg$', views.bloomberg, name="bloomberg"),
    url(r'^cnn$', views.cnn, name="cnn"),
    url(r'^foxnews$', views.foxnews, name="foxnews"),
    url(r'^nytimes$', views.nytimes, name="nytimes"),
    url(r'^politico$', views.politico, name="politico"),
    url(r'^usatoday$', views.usatoday, name="usatoday"),
    url(r'^wsj$', views.wsj, name="wsj"),
    url(r'^wapost$', views.wapost, name="wapost"),
]