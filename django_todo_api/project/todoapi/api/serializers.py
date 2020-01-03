from rest_framework import serializers
from todoapi import models


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True, read_only=True)
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = models.User 
        fields = ['name', 'tasks', 'id']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task 
        fields = ['description', 'state', 'user']
        lookup_field = 'user'

