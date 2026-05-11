# 🔐 AccessControl API

> A production-style authentication and role-based access control system built using FastAPI, JWT, SQLAlchemy, and Alembic.

---

## 🚀 Overview

AccessControl API is a secure backend authentication system that implements:

* User registration
* Password hashing
* JWT authentication
* Protected routes
* Role-based access control (RBAC)
* Database migrations using Alembic

This project follows modular backend architecture and production-style authentication patterns.

---

## ⚡ Features

### 👤 User System

* Register users
* Secure password hashing
* Fetch all users

### 🔐 Authentication

* JWT token generation
* Secure login system
* Token verification
* Protected endpoints

### 👑 Authorization (RBAC)

* Admin-only routes
* Role validation
* Permission-based access control

### 🗄️ Database

* SQLite integration
* SQLAlchemy ORM
* Alembic migrations

---

## 🧱 Tech Stack

* ⚡ FastAPI
* 🐍 Python
* 🗄️ SQLite
* 🧠 SQLAlchemy
* 🔄 Alembic
* 🔐 JWT Authentication
* 🔒 pwdlib Password Hashing

---

## 📂 Project Structure

```text
src/
├── auth/
│   ├── controllers.py
│   ├── routers.py
│   ├── schemas.py
│   └── utils.py
│
├── user/
│   ├── controllers.py
│   ├── models.py
│   ├── routers.py
│   └── schemas.py
│
├── utils/
│   ├── db.py
│   └── settings.py
│
└── main.py
```

---

## 🔥 API Endpoints

### 👤 Users

| Method | Endpoint  | Description   |
| ------ | --------- | ------------- |
| POST   | `/users/` | Register user |
| GET    | `/users/` | Get all users |

---

### 🔐 Authentication

| Method | Endpoint      | Description                    |
| ------ | ------------- | ------------------------------ |
| POST   | `/auth/login` | Login & receive JWT token      |
| GET    | `/auth/me`    | Get current authenticated user |
| GET    | `/auth/admin` | Admin-only protected route     |

---

## 🧪 Example Login Response

```json
{
  "access_token": "your.jwt.token",
  "token_type": "bearer"
}
```

---

## 🔐 Authentication Flow

```text
User Login
    ↓
Credentials Verification
    ↓
JWT Token Generated
    ↓
Client Stores Token
    ↓
Protected Request with Bearer Token
    ↓
Token Verification
    ↓
Access Granted / Denied
```

---

## 👑 Role-Based Access Control

This API supports role-based authorization.

### Example Roles

* `user`
* `admin`

Admin-only endpoints are protected using dependency-based authorization.

---

## ⚙️ Setup & Run

### Clone Repository

```bash
git clone https://github.com/whoismehfooz/AccessControl-API.git
cd AccessControl-API
```

---

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Migrations

```bash
alembic upgrade head
```

---

### Start Server

```bash
uvicorn src.main:app --reload
```

---

## 📚 Swagger Documentation

Open in browser:

```text
http://127.0.0.1:8000/docs
```

---

## 🧠 What I Learned

* JWT Authentication
* Protected Routes
* Role-Based Access Control
* Dependency Injection
* Database Migrations
* Production-style FastAPI Structure
* Git Branching Workflow

---

## 🚀 Future Improvements

* Refresh Tokens
* Email Verification
* Password Reset
* PostgreSQL Integration
* Docker Deployment

---

## 👨‍💻 Author

Building backend systems step-by-step with FastAPI 🚀
