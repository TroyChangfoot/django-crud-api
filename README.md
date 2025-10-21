# 🧩 Django CRUD API Demo

A fully containerized **Django REST API** showcasing production-grade CRUD patterns with JWT authentication, nested serializers, and Postman integration.

---

## 🚀 Features

- **Django REST Framework (DRF)** with full CRUD for:
  - `Products` — basic inventory items
  - `Customers` — client records
  - `Orders` — parent/child with nested `OrderItems`
- **JWT Authentication** via `djangorestframework-simplejwt`
- **Nested serializer creation** for Orders + automatic total calculation
- **PostgreSQL** via Docker Compose
- **Gunicorn** + Python 3.12 slim container
- **Seeding command** to populate demo data
- **Swagger UI / OpenAPI Docs**
- **Postman collection + environment** for instant testing

---

## 🏗️ Tech Stack

| Layer | Tech |
|-------|------|
| Backend | Django 5 + Django REST Framework |
| Auth | SimpleJWT |
| Database | PostgreSQL 15 |
| Container | Docker / Docker Compose |
| Docs | drf-spectacular + Swagger UI |
| Data Seeding | Faker |
| Testing | Postman collection |

---

## 🐳 Quick Start (Docker)

### 1️⃣ Clone & build
```bash
git clone https://github.com/<your-username>/django-crud-api.git
cd django-crud-api
docker compose up --build
```
> Default API will be available at **http://localhost:8000**

---

### 2️⃣ Run initial migrations
```bash
docker compose exec web python manage.py migrate
```

---

### 3️⃣ Seed demo data
Populate example products, customers, and orders:
```bash
docker compose exec web python manage.py seed_demo_data
```

---

### 4️⃣ Create superuser (optional)
```bash
docker compose exec web python manage.py createsuperuser
```
Access the Django Admin at **http://localhost:8000/admin/**

---

## 🔐 Authentication (JWT)

| Endpoint | Method | Purpose |
|-----------|---------|----------|
| `/api/auth/register/` | POST | Register a new user + auto-issue JWT |
| `/api/token/` | POST | Obtain JWT access & refresh token |
| `/api/token/refresh/` | POST | Refresh your access token |
| `/api/auth/me/` | GET | Retrieve current user info |

**Example request**
```json
POST /api/token/
{
  "username": "demo_user",
  "password": "StrongPass123"
}
```

**Use token on secured endpoints**
```
Authorization: Bearer <access_token>
```

---

## 🧾 CRUD Endpoints

| Resource | Endpoint | Example Methods |
|-----------|-----------|-----------------|
| Products | `/api/products/` | GET, POST, PUT, DELETE |
| Customers | `/api/customers/` | GET, POST, PUT, DELETE |
| Orders | `/api/orders/` | GET, POST, PUT, DELETE |
| Order Items | `/api/orders/items/` | GET, POST |

**Nested creation example**
```json
{
  "customer": 1,
  "status": "pending",
  "items": [
    {"product": 1, "quantity": 2},
    {"product": 3, "quantity": 1}
  ]
}
```

Response automatically includes calculated totals and product names.

---

## 📘 API Docs

Swagger UI
```
http://localhost:8000/api/docs/
```

OpenAPI schema
```
http://localhost:8000/api/schema/
```

---

## 🧠 Data Seeding

```bash
docker compose exec web python manage.py seed_demo_data   --products 15 --customers 10 --orders 20
```
Creates:
- Products with random SKUs, prices, stock
- Customers with fake names/emails
- Orders linked with nested items

---

## 🧰 Postman Setup

Import the following files from `/postman/`:
- `django-crud-api.postman_collection.json`
- `django-crud-api.postman_environment.json`

Environment variables
```
base_url = http://localhost:8000
access_token = {{populated automatically}}
refresh_token = {{populated automatically}}
```

The collection includes scripts that automatically:
- Save tokens from `/api/token/`
- Inject `Authorization: Bearer {{access_token}}` headers
- Refresh tokens if expired

---

## 🧱 Project Structure

```
backend/
├── core/                    # Django settings, URLs, WSGI
├── accounts/                # Auth & registration
├── products/                # Product CRUD
├── customers/               # Customer CRUD
├── orders/                  # Orders & nested order items
└── products/management/commands/seed_demo_data.py
```

---

## 🧩 Makefile Commands (optional)

```makefile
# Build & start containers
up:
	docker compose up --build

# Stop containers
down:
	docker compose down

# Apply migrations
migrate:
	docker compose exec web python manage.py migrate

# Seed demo data
seed:
	docker compose exec web python manage.py seed_demo_data
```

---

## 🧠 Example Workflow

1. Register user → `/api/auth/register/`
2. Obtain JWT → `/api/token/`
3. List products → `/api/products/`
4. Create order with nested items → `/api/orders/`
5. View orders with items → `/api/orders/{id}/`

---

## 🧾 License
MIT License © 2025 Troy Changfoot
This repository is for educational and demo purposes.