from django.db import models

from jsonfield import JSONField
import os

from . import _ugl


def attachments_file_upload(instance, filename):
    fn, ext = os.path.splitext(filename)
    return 'emails/{to}/{id}/{num}{ext}'.format(
        to=instance.email.to_mailbox,
        id=instance.email.id,
        num=instance.number,
        ext=ext
    )


class Email(models.Model):
    headers = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Headers')
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Text')
    )
    html = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('HTML')
    )
    to_mailbox = models.TextField(
        blank=False,
        null=False,
        verbose_name=_ugl('To')
    )
    from_mailbox = models.TextField(
        blank=False,
        null=False,
        verbose_name=_ugl('From')
    )
    cc = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Carbon Copy')
    )
    subject = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Subject')
    )
    dkim = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('DomainKeys Identified Mail')
    )
    SPF = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Sender Policy Framework')
    )
    envelope = JSONField(
        blank=True,
        null=True,
        verbose_name=_ugl('Envelope')
    )
    charsets = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_ugl('Charsets')
    )
    spam_score = models.FloatField(
        blank=True,
        null=True,
        verbose_name=_ugl('Spam score')
    )
    spam_report = models.TextField(
        blank=True,
        null=True,
        verbose_name=_ugl('Spam report')
    )
    # sender_ip
    # attachment-info
    # content-ids


class Attachment(models.Model):
    number = models.IntegerField(
        default=1,
        blank=False,
        null=False,
        verbose_name=_ugl("Email's Attachment Number")
    )
    file = models.FileField(
        upload_to=attachments_file_upload,
        blank=False,
        null=False,
        verbose_name=_ugl('Attached File')
    )
    email = models.ForeignKey(
        Email,
        blank=False,
        null=False,
        related_name='attachments',
        verbose_name=_ugl("Email Attached To")
    )
