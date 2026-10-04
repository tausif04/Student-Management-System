from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "phone", "course"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter student name",
                    "autocomplete": "name",
                    "required": True,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "student@example.com",
                    "autocomplete": "email",
                    "required": True,
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "+8801XXXXXXXXX",
                    "autocomplete": "tel",
                    "required": True,
                }
            ),
            "course": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Computer Science and Engineering",
                    "required": True,
                }
            ),
        }
        labels = {
            "name": "Full Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "course": "Course",
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Name must contain at least 2 characters.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        allowed = set("0123456789+-() ")
        if any(character not in allowed for character in phone):
            raise forms.ValidationError(
                "Phone number may contain digits, spaces, +, -, and parentheses only."
            )
        digits = "".join(character for character in phone if character.isdigit())
        if len(digits) < 7 or len(digits) > 15:
            raise forms.ValidationError("Enter a valid phone number.")
        return phone
