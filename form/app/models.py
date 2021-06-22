from django.db import models


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    city = models.CharField(max_length=50, null=True, blank=True)
    marks = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name
