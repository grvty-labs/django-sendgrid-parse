from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.sendgrid, name="django_sendgrid_parse_webhook")
)
