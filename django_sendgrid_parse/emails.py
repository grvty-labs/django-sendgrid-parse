from django.conf import settings
from django.utils import six

import sendgrid
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib


class TransactionalEmail(object):
    # A container for email information using Sendgrid Transactional Email

    def __init__(self, subject, template_id, body, from_email=None, to=None):
        #  reply_to=None

        if to:
            if isinstance(to, six.string_types):
                raise TypeError('"to" argument must be a list or tuple')
            self.to = list(to)
        if body:
            if not isinstance(body, dict):
                raise TypeError('"body" argument must be a dictionary')
            self.body = body

        # if reply_to:
        #     if isinstance(reply_to, six.string_types):
        #         raise TypeError('"reply_to" argument must be a list or tuple')
        #     self.reply_to = list(reply_to)

        self.from_email = from_email or settings.DEFAULT_FROM_EMAIL
        self.subject = subject
        self.template_id = template_id

    def recipients(self):
        # Returns a list of all recipients of the email (includes direct
        # addressees as well as Cc and Bcc entries).
        return self.to

    def send(self):
        sg = sendgrid.SendGridAPIClient(
            apikey=settings.DJANGO_SENDGRID_PARSE_API)

        data = {
          'personalizations': [
            {
              'to': [
                {
                  'email': mail
                } for mail in self.to
              ],
              'substitutions': self.body,
              'subject': self.subject,
            }
          ],
          'from': {
            'email': self.from_email
          },
          'template_id': self.template_id,
        }

        try:
            response = sg.client.mail.send.post(request_body=data)
        except urllib.HTTPError as e:
            print(e.read())
