from rest_framework import serializers

from .models import *


class PositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class PersonInSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'date_joined', 'position', 'image', 'age', 'slug')


class PersonOutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

