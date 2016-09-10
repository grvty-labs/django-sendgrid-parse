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

The EmailMessage class is initialized with the following parameters
(in the given order, if positional arguments are used). Almost all parameters
are optional and can be set at any time prior to calling the send() method.

`subject`: The subject line of the email.

`template_id`: The transactional template ID used in Sendgrid.

`body`: The body text with which the template will be filled. This should be a
dictionary.

`from_email`: The sender’s address. Both fred@example.com and Fred
<fred@example.com> forms are legal. If omitted, the DEFAULT_FROM_EMAIL
setting is used.

`to`: A list or tuple of recipient addresses.

Release Notes
-------------

*   0.4.2

  * Fixed error

*   0.4.1

  * Added filename property to Attachment

  * Added creation_date field to Email

*   0.4.0

  * Added TransactionalEmail functionality

  * It is required to use the API key to use the template engine.

  * Some testing is still required, but we could say this is almost a stable
  version until proven otherwise.

*   0.3.4

  *  Testing has been successful enough to say we are at BETA.

  * Now you can create emails manually without actually receiving them.
  (Oh yes, this was a small issue thanks to JSONField)

*   0.3.1

  *  Added comments and TODO's inside the code.

  *  Modified some models and included their migrations, but nothing to
  important

*   0.3.0

  * Changing to [Semantic Versioning](http://semver.org/) for better
  interpretation of the following releases.

  * Note: Remember, this project is still in alpha, and the first stable
  release will be **Version 1.0.0**.

  * Simple testing has been successful up to this point.

*   0.2.2

  * Bug detected in reception. Fixing.

  * Models improved for translation. (Still trying to get the hold of this,
    bear with me)

*   0.2.1

  * Improved the Attachments model, in order to save all the information
  inside the **media** directory

  * Migrate is required

*   0.2

  * The Email model lacked a **from** field. The word from is reserved by
  Python, so it had to be named as **from_mailbox** and the **to** field
  was renamed to **to_mailbox** just to maintain the standard.

  * Migrate is required

*   0.1.9

  * First alpha version.

  * This was the first time I published in PyPi (and the reason this is the
    first stable version)

Owned and developed by
--------

[![GRVTYlabs][logo]](www.grvtylabs.com)

[logo]: https://github.com/letops/django-sendgrid-parse/blob/master/logo.png?raw=true "GRVTYlabs"

[trans_email]: https://github.com/letops/django-sendgrid-parse/blob/master/django_sendgrid_parse/emails.py
