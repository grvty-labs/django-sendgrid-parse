from django.conf.urls import url

from . import views

app_name = 'django_sendgrid_parse'
urlpatterns = [
    url(
        r'^$',
        views.sendgrid_email_receiver, name='webhook'
    ),
]
