from django.db import models
from jsonfield import JSONField


class Attachment(models.Model):
    file = models.FileField()


class Email(models.Model):
    headers = models.TextField()
    text = models.TextField()
    html = models.TextField()
    to = models.TextField()
    cc = models.TextField()
    subject = models.TextField()
    dkim = JSONField()
    SPF = JSONField()
    envelope = JSONField()
    charsets = models.CharField(max_length=255)
    spam_score = models.FloatField()
    spam_report = models.TextField()
    attachments = models.ManyToManyField(
        Attachment,
        related_name='email'
    )
