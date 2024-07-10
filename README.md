# Backend project
This is python/django writte backend for my Join project (Kanban-Board) for Basic CRUD actions and user authentication
Create, Read, Update and Delete database models for User, Todos, Subtasks 
Login and Register yourself
local port on 127.0.0.1:8000 for backend connection

# Start backend server:
1. Clone repository and cd into it
2. Create and virtual environment
```bash 
    python -m venv env
```
```bash
    source env/bin/activate || # windows: env/Scripts/activate
```
3. Install requirements and migrations
```bash
    pip install -r requirements.txt
```
```bash
    python manage.py makemigrations
```
```bash
    python manage.py migrate

```
4. Start the Development Server
```bash
    python manage.py runserver
```