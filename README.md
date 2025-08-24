# 🚀 FastAPI ToDo Project

A **simple ToDo application** built with **FastAPI**, featuring user management, task management, and **JWT authentication**.  

---

## ✨ Features

- 👤 **User Management**: Register and login users  
- 📝 **Task Management**: Create, read, edit, and delete tasks  
- 🔐 **JWT Authentication**: Protect user and task actions
- 🐋 **Dockerized**: Run with docker compose

---

## 📦 API Endpoints

### 🏷 Account Endpoints

| Method | Endpoint | Description | Request Body | Response |
|--------|---------|-------------|--------------|----------|
| POST   | `/account/register` | Register a new user | `{ "username": "string", "password": "string", "email": "string" }` | `{ "message": "user: <username> registered" }` |
| POST   | `/account/login/` | Login and get JWT tokens | `{ "username": "string", "password": "string" }` | `{ "access_token": "string", "refresh_token": "string" }` |
| POST   | `/account/token/refresh` | Refresh access token | `{ "refresh_token": "string" }` | `{ "access_token": "string" }` |
| GET    | `/account/users/list` | List all registered users | N/A | `[{ "id": 1, "username": "string", "email": "string" }]` |

---

### 🗂 Task Endpoints

| Method | Endpoint | Description | Request Body | Response |
|--------|---------|-------------|--------------|----------|
| GET    | `/tasks/` | Get all tasks (JWT protected) | N/A | `[{"id": 1, "title": "string", "user_id": 1}]` |
| POST   | `/tasks/create/` | Create a new task | `{ "title": "string" }` | `{ "message": "task: <title> created" }` |
| PUT    | `/tasks/edit/{task_id}/` | Edit a task (JWT protected) | `{ "title": "string" }` | `{ "message": "task updated" }` |
| DELETE | `/tasks/del/{task_id}/` | Delete a task (JWT protected) | N/A | `{ "message": "task deleted" }` |

---

## 🔑 Authentication

- All task endpoints are **JWT protected**  
- Use **access token** in `Authorization: Bearer <token>` header for authentication  
- **Refresh token** can be used to get a new access token  

---

## 🗄 Database

- **SQLAlchemy ORM** for database operations  
- **SQLite** database  
- Models: `User` and `Task`  

---

## ⚡ Installation & Run
```bash
# Clone the repository
git clone https://github.com/Mahdi-jahanfar-dev/FastApi-ToDo.git
cd FastApi-ToDo
```

### docker compose
```bash
sudo docker-compose up -d --build
```

### In Local
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
fastapi dev main.py
```
