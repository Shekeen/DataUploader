from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class StoredData(models.Model):
    class Meta:
        unique_together = ('key',)

    key = models.CharField(max_length=1000)
    sha1_hexdigest = models.CharField(max_length=100)
    byte_size = models.BigIntegerField()
    upload_time = models.DateTimeField(default=timezone.now)
    comment = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return '<StoredData: {}>'.format(self.key)