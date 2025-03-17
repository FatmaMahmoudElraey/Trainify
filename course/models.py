from django.db import models

# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=100)
    hours = models.IntegerField()
    picture = models.ImageField(upload_to='courses/pictures',null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'Courses'

    def __str__(self):
        return self.name 