from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PositionListCreateView(ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


class PositionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializers


class ProjectListCreateView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializers


class PersonInListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonInSerializers


class PersonInRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonInSerializers


class PersonOutListCreateView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonOutSerializers


class PersonOutRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonOutSerializers
