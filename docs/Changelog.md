Changelog
==========

This is **django-sendgrid-parse**'s changelog: The place where you can
read about the new releases and how they could impact your current
installation of this package.


*   0.4.3
    *   Modified attachment's filename


*   0.4.2
    *   Fixed error


*   0.4.1
    *   Added filename property to Attachment
    *   Added creation_date field to Email


*   0.4.0
    *   Added TransactionalEmail functionality
    *   It is required to use the API key to use the template engine.
    *   Some testing is still required, but we could say this is almost
    a stable version until proven otherwise.


*   0.3.4
    *   Testing has been successful enough to say we are at BETA.
    *   Now you can create emails manually without actually receiving
    them. (Oh yes, this was a small issue thanks to JSONField)


*   0.3.1
    *   Added comments and TODO's inside the code.
    *   Modified some models and included their migrations, but
    nothing to important


*   0.3.0
    *   Changing to [Semantic Versioning](http://semver.org/) for better
    interpretation of the following releases.
    *   Note: Remember, this project is still in alpha, and the first
    stable release will be **Version 1.0.0**.
    *   Simple testing has been successful up to this point.


*   0.2.2
    *   Bug detected in reception. Fixing.
    *   Models improved for translation. (Still trying to get the hold
    of this, bear with me)


*   0.2.1
    *   Improved the Attachments model, in order to save all the
    information inside the **media** directory
    *   Migration is required


*   0.2
    *   The Email model lacked a **from** field. The word from is
    reserved by Python, so it had to be named as **from_mailbox** and
    the **to** field was renamed to **to_mailbox** just to maintain the
    standard.
    *   Migrate is required


*   0.1.9
    *   First alpha version.
    *   This was the first time I published in PyPi (and the reason
    this is the first alpha version)



Owned and developed by
--------

[![StackShare][stack-shield]][stack-tech]


[![GRVTY][logo]](http://grvty.digital)

[logo]: http://grvty.digital/images/logos/repos-logo-2.png?raw=true "GRVTY"
[stack-shield]: http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat
[stack-tech]: http://stackshare.io/grvty/grvty
