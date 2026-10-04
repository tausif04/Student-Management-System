from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import StudentForm
from .models import Student


class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_detail.html"
    context_object_name = "student"


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("students:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Student '{self.object.name}' was added successfully.",
        )
        return response


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "students/student_form.html"
    success_url = reverse_lazy("students:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Student '{self.object.name}' was updated successfully.",
        )
        return response


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "students/student_confirm_delete.html"
    success_url = reverse_lazy("students:list")

    def form_valid(self, form):
        student_name = self.object.name
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Student '{student_name}' was deleted successfully.",
        )
        return response
