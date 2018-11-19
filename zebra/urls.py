from django.conf.urls import url
from zebra import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view())
]
