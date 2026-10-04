from django.urls import path

from .views import (
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
)

app_name = "students"

urlpatterns = [
    path("", StudentListView.as_view(), name="list"),
    path("students/add/", StudentCreateView.as_view(), name="create"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="detail"),
    path("students/<int:pk>/edit/", StudentUpdateView.as_view(), name="update"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="delete"),
]
