from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name="home"),
    path('delete/<str:id>', delete_task, name="delete"),
    path('complete/<str:id>', complete_task, name="complete"),
]