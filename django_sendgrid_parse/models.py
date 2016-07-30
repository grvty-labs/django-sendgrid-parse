from django.db import models
from django.utils.translation import ugettext as _ug

from jsonfield import JSONField
import os


def attachments_file_upload(instance, filename):
    fn, ext = os.path.splitext(filename)
    return 'emails/{to}/{id}/{num}{ext}'.format(
        to=instance.email.to_mailbox,
        id=instance.email.id,
        num=instance.number,
        ext=ext
    )


class Email(models.Model):
    headers = models.TextField()
    text = models.TextField()
    html = models.TextField()
    to_mailbox = models.TextField()
    from_mailbox = models.TextField()
    cc = models.TextField()
    subject = models.TextField()
    dkim = JSONField()
    SPF = JSONField()
    envelope = JSONField()
    charsets = models.CharField(
        max_length=255
    )
    spam_score = models.FloatField()
    spam_report = models.TextField()


class Attachment(models.Model):
    number = models.IntegerField(
        default=1,
        blank=False,
        null=False,
        verbose_name=_ug("Email's Attachment Number")
    )
    file = models.FileField(
        upload_to=attachments_file_upload,
        blank=False,
        null=False,
        verbose_name=_ug('Attached File')
    )
    email = models.ForeignKey(
        Email,
        blank=False,
        null=False,
        related_name='attachments',
        verbose_name=_ug("Email Attached To")
    )
