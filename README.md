# Arcitect
Arcitect Task Manager

This is simple task manager using Django and DjangoRest.
1. Backend:
    - Create a model for `Task` with fields: `id`, `title`, `description`, and `status` (Pending, Completed).
    - Create RESTful APIs to perform CRUD operations on `Task`.

2. Frontend:
    - Create a simple HTML page that uses JavaScript to interact with your APIs.
    - The page should have:
        - A form to create a new task.
        - A list to display all tasks.
        - Options to update and delete tasks.

3. Database:
    - Use SQLite for the database.

Project Setup:

python -m venv task #create virtual environment

task/Scripts/activate #activate virtual environment

pip install django #install django

django-admin startproject arcitect #create project
python manage.py startapp task_app #start app
python manage.py runserver #test if project setup is ok

copy respective files and templates to project
python manage.py createsuperuser #create superuser

