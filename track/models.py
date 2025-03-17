from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Tracks(models.Model):
    name = models.CharField(max_length=100)
    hours = models.IntegerField()
    picture = models.ImageField(upload_to='tracks/pictures',null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'Tracks'

    def __str__(self):
        return self.name 