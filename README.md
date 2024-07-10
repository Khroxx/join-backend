# Backend project
This is a python/django written backend for my Join project (Kanban-Board) for Basic CRUD actions and user authentication
Create, Read, Update and Delete database models for User, Todos, Subtasks 
Login and Register yourself
local port on 127.0.0.1:8000 for backend connection

# Start backend server:
1. Clone repository and cd into it
```bash
    git clone https://github.com/Khroxx/join-backend.git
```
```bash
    cd join-backend/
```
2. Create and virtual environment
```bash 
    python -m venv env
```
## Select the correct Interpreter
Linux:
```bash
    source env/bin/activate  
```
Windows :
```bash
    source env/Scripts/activate
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