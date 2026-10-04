# Student Management System

A clean, beginner-friendly **Student Management System** built with Django. This project demonstrates the core concepts of Django forms, ModelForms, class-based views, CRUD operations, template inheritance, validation, and the Django messages framework.

It is designed as a practical learning project while following a clean and maintainable project structure.

---

## Features

### Student Management
- Register a new student
- View all registered students
- View individual student details
- Update student information
- Delete student records
- Prevent duplicate email addresses

### Form & Validation
- Django `ModelForm`
- HTML5 required-field validation
- Email format validation
- Custom name validation
- Custom phone-number validation
- Server-side validation

### Django Features
- Class-Based Views
- Django ORM
- SQLite database
- Django Messages Framework
- Template inheritance
- Reusable templates
- CSRF protection
- Django Admin

### UI
- Clean and responsive interface
- Mobile-friendly student list
- Success/error feedback messages
- Delete confirmation page
- Reusable buttons and form components
- No external frontend framework required

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Programming language |
| Django 5.2 | Web framework |
| SQLite | Database |
| HTML5 | Page structure |
| CSS3 | Styling |
| Pipenv | Dependency & virtual environment management |

---

## Project Structure

```text
student_management_system/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   └── students/
│   │       ├── student_confirm_delete.html
│   │       ├── student_detail.html
│   │       ├── student_form.html
│   │       └── student_list.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   └── css/
│       └── style.css
│
├── .gitignore
├── manage.py
├── Pipfile
└── README.md
```

---

## Data Model

The application contains a `Student` model with the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | BigAutoField | Primary key |
| `name` | CharField | Student's full name |
| `email` | EmailField | Unique email address |
| `phone` | CharField | Student phone number |
| `course` | CharField | Student's course |
| `created_at` | DateTimeField | Record creation time |
| `updated_at` | DateTimeField | Last update time |

The model uses:

```python
class Meta:
    ordering = ["-created_at"]
```

so newly registered students appear first.

---

## CRUD Implementation

The project implements all four CRUD operations using Django Class-Based Views.

### Create

A student can be registered through:

```text
/students/add/
```

Implemented with:

```python
StudentCreateView
```

The form is based on:

```python
StudentForm
```

which is a Django `ModelForm`.

---

### Read

The application provides two read operations.

#### Student List

```text
/
```

Implemented with:

```python
StudentListView
```

#### Student Details

```text
/students/<id>/
```

Implemented with:

```python
StudentDetailView
```

---

### Update

Existing student information can be edited through:

```text
/students/<id>/edit/
```

Implemented with:

```python
StudentUpdateView
```

The same `StudentForm` is reused for updating the record.

---

### Delete

A student can be deleted through:

```text
/students/<id>/delete/
```

Implemented with:

```python
StudentDeleteView
```

A confirmation page is displayed before the record is permanently deleted.

---

## Forms

The project uses Django's `ModelForm`:

```python
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "phone", "course"]
```

Custom validation is also implemented.

For example:

```python
def clean_name(self):
    name = self.cleaned_data["name"].strip()

    if len(name) < 2:
        raise forms.ValidationError(
            "Name must contain at least 2 characters."
        )

    return name
```

This demonstrates the difference between simple HTML validation and Django server-side validation.

---

## Template Inheritance

The project uses a common:

```text
base.html
```

template containing:

- Navbar
- Main content block
- Messages
- Footer
- Static CSS

Individual pages extend it:

```django
{% extends "base.html" %}
```

and customize:

```django
{% block title %}
{% endblock %}

{% block content %}
{% endblock %}
```

This avoids duplicating common HTML across pages.

---

## Messages Framework

The Django Messages Framework is used to provide feedback after successful operations.

Examples:

```text
Student 'John Doe' was added successfully.
```

```text
Student 'John Doe' was updated successfully.
```

```text
Student 'John Doe' was deleted successfully.
```

This provides immediate feedback to the user after CRUD operations.

---

## URL Routes

| Method | URL | Purpose |
|---|---|---|
| `GET` | `/` | Student list |
| `GET` | `/students/add/` | Registration form |
| `POST` | `/students/add/` | Create student |
| `GET` | `/students/<id>/` | Student details |
| `GET` | `/students/<id>/edit/` | Edit form |
| `POST` | `/students/<id>/edit/` | Update student |
| `GET` | `/students/<id>/delete/` | Delete confirmation |
| `POST` | `/students/<id>/delete/` | Delete student |
| `GET` | `/admin/` | Django admin |

> Note: Django's standard `DeleteView` uses a POST request to actually perform deletion after the confirmation page is displayed. This is preferable to exposing destructive operations through a GET request.

---

## Installation

### Prerequisites

Make sure you have installed:

- Python 3.12
- Pip
- Pipenv

Check Python:

```bash
python --version
```

Install Pipenv if necessary:

```bash
pip install pipenv
```

---

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd student_management_system
```

### 2. Install dependencies

```bash
pipenv install
```

This creates the project's virtual environment and installs Django according to the `Pipfile`.

### 3. Activate the environment

```bash
pipenv shell
```

Alternatively, commands can be executed directly through:

```bash
pipenv run python manage.py migrate
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create an admin user

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Django Admin

The `Student` model is registered in Django Admin.

Open:

```text
http://127.0.0.1:8000/admin/
```

The admin interface supports:

- Viewing students
- Searching students
- Filtering students
- Adding students
- Editing students
- Deleting students

Search fields include:

```text
name
email
course
```

---

## Development Commands

Run the development server:

```bash
python manage.py runserver
```

Create migrations after changing models:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create an admin account:

```bash
python manage.py createsuperuser
```

Run Django's system checks:

```bash
python manage.py check
```

Open the Django shell:

```bash
python manage.py shell
```

---

## Learning Outcomes

After completing this project, you should understand:

- How Django projects and apps are structured
- How Django models represent database tables
- How SQLite works with Django
- How to create and use migrations
- How Django ModelForms work
- How to perform form validation
- How GET and POST requests work
- How Class-Based Views simplify CRUD development
- How Django's ORM interacts with the database
- How template inheritance works
- How reusable templates reduce duplication
- How Django messages provide user feedback
- How CSRF protection works in Django forms
- How Django Admin can manage application data

---

## Why Class-Based Views?

This project intentionally uses Class-Based Views because they provide reusable implementations for common operations.

For example:

```python
class StudentCreateView(CreateView):
    ...
```

instead of manually writing all the request handling logic.

The main views are:

```text
ListView
DetailView
CreateView
UpdateView
DeleteView
```

This makes the CRUD implementation concise and follows Django conventions.

---

## Validation Strategy

Validation happens at multiple levels.

### Browser-Level Validation

HTML attributes such as:

```html
required
```

and Django's generated email input provide immediate browser feedback.

### Django Form Validation

The `StudentForm` validates submitted data on the server.

Examples:

- Valid email address
- Name length
- Phone number format
- Required fields

### Database-Level Constraint

Email addresses are unique:

```python
email = models.EmailField(unique=True)
```

This prevents duplicate student records with the same email.

---

## Security Considerations

The project follows several standard Django security practices:

- CSRF protection enabled
- POST used for state-changing operations
- Django's built-in form validation
- ORM used instead of raw SQL
- Secret key stored in settings
- Destructive actions require confirmation

For production deployment, additional configuration should be added, including environment variables for secrets, `DEBUG=False`, production `ALLOWED_HOSTS`, HTTPS, secure cookies, and a production database.

---

## Screenshots

Add screenshots of the application here when publishing the project on GitHub.

Recommended screenshots:

```text
screenshots/
├── student-list.png
├── student-form.png
├── student-detail.png
├── delete-confirmation.png
└── admin.png
```

---

## Future Improvements

Possible extensions include:

- Student search
- Pagination
- Course filtering
- Authentication
- User roles and permissions
- Profile pictures
- REST API using Django REST Framework
- PostgreSQL support
- Automated tests
- Docker support
- Deployment to Render/Railway/AWS
- Dashboard with student statistics

---

## License

This project is intended for educational and learning purposes.

You are free to modify and extend it for your own learning and portfolio projects.
