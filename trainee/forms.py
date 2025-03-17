from django import forms
from .models import Trainee
from course.models import Courses

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        # fields = '__all__'
        fields = ['name', 'age', 'email', 'img',  'track','courses']
    def __init__(self, *args, **kwargs):
        super(TraineeForm, self).__init__(*args, **kwargs)
        self.fields['courses'].widget = forms.CheckboxSelectMultiple()
        self.fields['courses'].queryset = Courses.objects.all()