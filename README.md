**django-sendgrid-parse**
=========================

Django app to receive and save email from sendgrid
--------------------------------------------------

[Sendgrid Parse](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html)
is an incoming event API which will analyse and parse incoming emails and POST
them on a specific url as a JSON with a multipart encoding

**Django Sendgrid Parse** allows you to save all the information redirected
from Sendgrid Parse to our Django project.

Installation
------------

    pip install django-sendgrid-parse

Usage
-----

*   Add **django_sendgrid_parse** to your `INSTALLED_APPS`

*   In order to use the TransactionalEmail, you need to add the API key in
your settings configuration the variable
`DJANGO_SENDGRID_PARSE_API='Your-API-key'` and by using
`from django_sendgrid_parse.emails import TransactionalEmail` you can use this
functionality.

*   Add to urls.py `url("sendgrid", include("django_sendgrid_parse.urls"))`

*   Associate the Domain/Hostname and the URL in the Parse API settings page.
      The Parse API settings page is [here](https://sendgrid.com/developer/reply)

*   This application executes a signal when an email is received, in case you
      wish to do something with the message after the save but before informing
      Sendgrid about the reception. The signal is in:
      `from django_sendgrid_parse.signals import message_received` and use the
      `email` parameter. (In case of error in your code, this library will
      return a 208 status to Sendgrid to stop the multiple retries).

Extra functionality
-------------------

### class TransactionalEmail [¶][trans_email]

The `EmailMessage` class is initialized with the following parameters
(in the given order, if positional arguments are used). All required
parameters must be set prior to calling the `send()` method.

`subject`: Required. The subject line of the email.

`template_id`: Required. The transactional template ID used in Sendgrid.

`body`: Required. The body text with which the template will be filled. This should be a
dictionary.

`from_email`: Optional. The sender’s address. Both `fred@example.com`
and `Fred <fred@example.com>` forms are accepted. If omitted, the
`DEFAULT_FROM_EMAIL` setting is used.

`to`: Optional. A list or tuple of recipient addresses.


Other docs
----------

*   [Changelog][changelog]
*   [Milestones][milestones]
*   [LICENSE][license]


Owned and developed by
--------

[![GRVTYlabs][logo]](www.grvtylabs.com)

[![GRVTY][logo]](http://grvty.digital)

[logo]: http://grvty.digital/images/logos/repos-logo-1.png?raw=true "GRVTY"
[stack-shield]: http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat
[stack-tech]: http://stackshare.io/grvty/grvty

[trans_email]: https://github.com/grvty-labs/django-sendgrid-parse/blob/master/django_sendgrid_parse/emails.py

[changelog]: https://github.com/grvty-labs/django-sendgrid-parse/blob/master/docs/Changelog.md
[milestones]: https://github.com/grvty-labs/django-sendgrid-parse/blob/master/docs/Milestones.md
[license]: https://github.com/grvty-labs/django-sendgrid-parse/blob/master/LICENSE
