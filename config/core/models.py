from django.db import models

# Create your models here.
  class Livre(models.Model):

    def save(self, *args, **kwargs):
        self.isbn = self.isbn.replace("-", "").strip()
        super().save(*args, **kwargs)

