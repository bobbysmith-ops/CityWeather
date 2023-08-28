from django.urls import path
from . import views # . means import from the current directory

urlpatterns = [
    path('', views.index)
]