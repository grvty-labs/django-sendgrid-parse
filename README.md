django-sendgrid-parse
=====================

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

*   Add **django_sendgrid_parse** to your `installed_apps`

*   Add to urls.py `url("sendgrid", include("django_sendgrid_parse.urls"))`

*   Associate the Domain/Hostname and the URL in the Parse API settings page.
      Parse API settings page is [here](https://sendgrid.com/developer/reply)

Release Notes
-------------

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

  * This was the first time I published in PyPi (that is the reason this
  is the first stable version)

GRVTYlabs 2016
