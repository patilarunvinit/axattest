from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", views.loginmain, name="login"),
    path("ad/", views.admin, name="admin"),
    path("teacher/", views.teacher, name="teacher"),
    path("student/", views.student, name="student"),
    path("registration/", views.registration, name="registration"),
]
