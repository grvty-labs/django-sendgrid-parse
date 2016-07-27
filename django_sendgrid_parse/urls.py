from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^$',
        views.sendgrid_email_receiver, name="django_sendgrid_parse_webhook"
    ),
]
