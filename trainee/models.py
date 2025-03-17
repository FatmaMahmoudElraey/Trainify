from django.db import models
from django.utils import timezone

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    img = models.ImageField(upload_to='trainee/pictures', null=True)
    status = models.BooleanField(default=True)

    courses = models.ManyToManyField('course.Courses', related_name='trainees')
    track = models.ForeignKey('track.Tracks', on_delete=models.CASCADE, related_name='trainees', null=True)
    class Meta:
        db_table = 'Trainee'

    def __str__(self):
        return self.name
