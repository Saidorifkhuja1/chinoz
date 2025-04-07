import uuid

from django.db import models

class Worker(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='worker/')
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

