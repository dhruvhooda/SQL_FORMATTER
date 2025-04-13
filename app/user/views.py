from rest_framework import generics
from user.serializers import (
      UserSerializer
)
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
class CreateUserView(generics.CreateAPIView):

    serializer_class = UserSerializer

def register(request):
      if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  user = form.save()
                  login(request, user)
                  return redirect("formatter:formatter")
      else:
            form = UserCreationForm()
      return render(request, 'register.html', {'form': form})
