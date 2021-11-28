from django.urls import path
from .views import *

urlpatterns = [
    path('list_create/position', PositionListCreateView.as_view()),
    path('update_destroy/position/<int:pk>', PositionRetrieveUpdateDestroyAPIView.as_view()),
    path('list_create/personin', PersonInListCreateView.as_view()),
    path('update_destroy/personin/<int:pk>', PersonInRetrieveUpdateDestroyAPIView.as_view()),
    path('list_create/personout', PersonOutListCreateView.as_view()),
    path('update_destroy/personout/<int:pk>', PersonOutRetrieveUpdateDestroyAPIView.as_view()),
    path('list_create/project', ProjectListCreateView.as_view()),
    path('update_destroy/project/<int:pk>', ProjectRetrieveUpdateDestroyAPIView.as_view()),
]