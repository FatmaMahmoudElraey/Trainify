from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView, DeleteView
from .models import Trainee
from .forms import TraineeForm
from .serializers import TraineeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class TraineeListView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        trainees = Trainee.objects.filter(status=True)

        if request.headers.get('Accept') == 'application/json':
              
            serializer = TraineeSerializer(trainees, many=True)
            return JsonResponse(serializer.data, safe=False)

        return render(request, 'trainee/trainee_list.html', {'trainees': trainees})


class TraineeCreateView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        form = TraineeForm()
        return render(request, 'trainee/add_trainee.html', {'form': form})

    def post(self, request):
        if request.headers.get('Accept') == 'application/json':  
            serializer = TraineeSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)

        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('traineelist')
        return render(request, 'trainee/add_trainee.html', {'form': form})



class TraineeListCreateView(APIView):

    def get(self, request):
        trainees = Trainee.objects.filter(status=True)  
        serializer = TraineeSerializer(trainees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class TraineeUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TraineeSerializer

    def perform_destroy(self, instance):
        instance.status = False
        instance.save()

class TraineeDetailView(LoginRequiredMixin, DetailView):
    model = Trainee
    template_name = 'trainee/trainee_details.html'
    context_object_name = 'trainee'
    login_url = '/accounts/login/'


def home(request):
    return render(request, 'base/home.html')
