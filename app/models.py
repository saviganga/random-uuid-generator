import uuid
from django.db import models

# Create your models here.
class UUIDModel(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    UUID = models.UUIDField(default=uuid.uuid4(), editable=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.timestamp}: {self.UUID}'
