from django.shortcuts import render, redirect
from . models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin

def course_list(request):
    courses = Courses.objects.filter(status=True)
    return render(request, 'courses/course_list.html', {'courses': courses})


from . forms import CoursesForm
def add_course(request):
    if request.method == 'GET':
        form = CoursesForm()
        return render(request, 'courses/add_course.html', {'form': form})
    else:
        form = CoursesForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.data)
            form.save()
            return redirect('course_list')
    return render(request, "courses/add_course.html", {"form":form})



def update_course(request, id):
    course = Courses.objects.get(id=id)  
    
    if request.method == "POST":
        form = CoursesForm(request.POST, request.FILES, instance=course)  
        if form.is_valid():
            form.save()  
            return redirect('course_list') 
    else:
        form = CoursesForm(instance=course)  

    return render(request, "courses/add_course.html", {'form': form, 'course': course})




# create view for delete
def delete_course(request, id):
    course = Courses.objects.get(id=id)
    course.status = False
    course.save()
    return redirect('course_list')
