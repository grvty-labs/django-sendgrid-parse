from django.apps import AppConfig as BaseConfig
from django.utils.translation import ugettext_lazy as _


class DjangoSendgridParseAppConfig(BaseConfig):
    name = 'django_sendgrid_parse'
    verbose_name = _('Django Sendgrid Parse')
