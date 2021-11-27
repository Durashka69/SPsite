from rest_framework import serializers
from .models import Project


class ProjectSerializers:
    class Meta:
        model = Project
        fields = '__all__'
