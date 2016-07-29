django-sendgrid-parse
=====================

Django app to receive and save email from sendgrid
--------------------------------------------------

[Sendgrid Parse](https://sendgrid.com/docs/API_Reference/Webhooks/parse.html)
is an incoming event API which will analyse and parse incoming emails and POST
them on a specific url as a JSON with a multipart encoding

This app provides a simple solution to create save those parsed emails
directly in our Django database by receiving them through a public URL.

Installation
------------

    pip install django-sendgrid-parse

Usage
-----

*   Add **django_sendgrid_parse** to your `installed_apps`

*   Add to urls.py `url("sendgrid", include("django_sendgrid_parse.urls"))`

*   Associate the Domain/Hostname and the URL in the Parse API settings page.
      Parse API settings page is [here](https://sendgrid.com/developer/reply)

GRVTYlabs 2016
