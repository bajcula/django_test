from django.db import models

from companies.models import Company

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 32)
    age = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING),

    def __str__(self):
        return self.name