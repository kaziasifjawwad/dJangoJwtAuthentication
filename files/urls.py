from django.urls import path
from .views import TestClass

urlpatterns=[
    path('images/', TestClass.as_view() , name="testName")
]