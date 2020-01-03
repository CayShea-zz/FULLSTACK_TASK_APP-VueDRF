from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from todoapi import models
from .serializers import TaskSerializer, UserSerializer


# -------
#   User
# -------
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer

# -------
#   TASK
# -------
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = models.Task.objects.all()

    # to do next: filter Task by user id


