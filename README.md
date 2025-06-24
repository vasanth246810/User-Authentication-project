# User Authentication Project

A Django-based user authentication system with custom user profile management, session-based login/logout, and MySQL database support.

## Features

- User registration (sign up) with username, first name, last name, email, and password
- Secure password hashing (custom or configurable)
- User login and logout with session management
- Dashboard page for logged-in users
- User profile information display
- Error and success message handling
- Bootstrap 5 styled frontend
- MySQL database integration

## Requirements

- Python 3.8+
- Django 5.x
- MySQL server
- Bootstrap 5 (via CDN)
- (Optional) VS Code for development

## Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/vasanth246810/User-Authentication-project.git
   cd User-Authentication-project
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv myenv
   myenv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install django mysqlclient
   ```

4. **Configure your MySQL database in `UserProject/settings.py`:**
   ```python
 DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': DATABASE_NAME,
                'USER': DATABASE_USER,
                'PASSWORD': DATABASE_PASSWORD,
                'HOST': DATABASE_HOST,
                'PORT': DATABASE_POST,
                'OPTIONS':{
                        'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
                }
        }
}
   ```

5. **Apply migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

## Project Structure

```
UserProject/
├── Userapp/
│   ├── migrations/
│   ├── templates/
│   │   └── Userapp/
│   │       ├── base.html
│   │       ├── signup.html
│   │       ├── signin.html
│   │       └── dashboard.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── UserProject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── myenv/
```


