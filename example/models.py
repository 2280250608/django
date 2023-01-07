from django.db import models


# Create your models here.
class Example(models.Model):
    title = models.CharField(max_length=50, default=None)
    year = models.PositiveIntegerField()
    flag = models.BooleanField(default=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.year}'
