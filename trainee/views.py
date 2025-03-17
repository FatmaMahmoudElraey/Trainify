from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect , get_object_or_404

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Trainee
from .forms import TraineeForm
from django.views import View

class TraineeListView(LoginRequiredMixin, ListView):
    model = Trainee
    template_name = 'trainee/trainee_list.html'
    context_object_name = 'trainees'
    login_url = '/accounts/login/'

    def get_queryset(self):
        return Trainee.objects.filter(status=True)

# def add_trainee(request):
#     if request.method == 'GET':
#         form = TraineeForm()
#         return render(request, 'trainee/add_trainee.html', {'form': form})
#     else:
#         form = TraineeForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('traineelist')
#     return render(request, "trainee/add_trainee.html", {"form":form})

# class TraineeCreateView(LoginRequiredMixin, CreateView):
#     model = Trainee
#     form_class = TraineeForm
#     template_name = 'trainee/add_trainee.html'
#     success_url = reverse_lazy('traineelist')
#     login_url = '/accounts/login/'

class TraineeCreateView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        form = TraineeForm()
        return render(request, 'trainee/add_trainee.html', {'form': form})

    def post(self, request):
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('traineelist')
        return render(request, 'trainee/add_trainee.html', {'form': form})


# class TraineeUpdateView(LoginRequiredMixin, UpdateView):
#     model = Trainee
#     form_class = TraineeForm
#     template_name = 'trainee/add_trainee.html'
#     success_url = reverse_lazy('traineelist')
#     login_url = '/accounts/login/'

class TraineeUpdateView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request, pk):  
        trainee = get_object_or_404(Trainee, pk=pk)
        form = TraineeForm(instance=trainee)
        return render(request, 'trainee/add_trainee.html', {'form': form, 'trainee': trainee})

    def post(self, request, pk):
        trainee = get_object_or_404(Trainee, pk=pk)
        form = TraineeForm(request.POST, request.FILES, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('traineelist')
        return render(request, 'trainee/add_trainee.html', {'form': form, 'trainee': trainee})


class TraineeDeleteView(LoginRequiredMixin, DeleteView):
    model = Trainee
    template_name = 'trainee/trainee_confirm_delete.html'
    success_url = reverse_lazy('traineelist')
    login_url = '/accounts/login/'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.status = False
        self.object.save()
        return redirect(self.success_url)

class TraineeDetailView(LoginRequiredMixin, DetailView):
    model = Trainee
    template_name = 'trainee/trainee_details.html'
    context_object_name = 'trainee'
    login_url = '/accounts/login/'

def home(request):
    return render(request, 'base/home.html')
