from django.urls import path
from . import views

app_name='fruit'
urlpatterns = [
    path('fruits/',views.fruits,name="good-fruit"),
    path('testmonial/',views.testmonial,name="testmonial"),
]
