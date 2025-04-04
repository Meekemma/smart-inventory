

# Inventory Management System

This is an **Inventory Management System** designed to manage product inventory, sales, orders, and purchase orders. It supports features like tracking stock levels, generating sales reports, and managing suppliers. It uses **Django** as the backend framework, **Django Rest Framework (DRF)** for API development, **Celery** for asynchronous task management, and **Redis** for message brokering.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [Configuration](#configuration)
- [Generating Django Secret Key](#generating-django-secret-key)
- [Running the Project](#running-the-project)
- [Celery & Redis Setup](#celery--redis-setup)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The **Inventory Management System** is a full-stack Django application designed to help businesses manage their product inventory, sales, and orders. The system allows users to track products, manage orders and suppliers, and generate reports. The application includes robust features for handling various tasks such as:

- User authentication and authorization (with JWT tokens)
- Inventory management (create, update, delete products and categories)
- Order management (create, update, and track orders)
- Sales reporting (daily, weekly, and monthly sales)
- Purchase order management

---

## Features

- **User Authentication**:
  - JWT-based authentication for secure login and registration.
  - Change password and logout functionality.

- **Inventory Management**:
  - Product and category management (CRUD operations).
  - Transaction tracking and history.

- **Order Management**:
  - Create and track customer orders.
  - Update order status.
  - Order item updates.

- **Purchase Order Management**:
  - Create, track, and update purchase orders.
  - Manage purchase order items.

- **Sales Reporting**:
  - Generate daily, weekly, and monthly sales reports.
  - Low stock alerts and tracking.

---

## Technologies Used

- **Django**: Backend framework
- **Django Rest Framework (DRF)**: For building the RESTful API
- **Celery**: Asynchronous task queue/job queue based on distributed message passing
- **Redis**: Message broker for Celery tasks
- **PostgreSQL**: Database for storing application data
- **JWT**: Authentication token system
- **DRF Spectacular**: API documentation

---

## Installation Instructions

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/Meekemma/smart-inventory.git
```

### 2. Create a Virtual Environment
It’s a good practice to use a virtual environment to isolate your project dependencies:
```bash
cd your-repository
python3 -m venv venv
```

### 3. Activate the Virtual Environment
- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **MacOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Project Dependencies
Install all the required dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Set up the required environment variables:
- Create a `.env` file in the root directory of your project.
- Add the following variables:
  ```bash
  SECRET_KEY=<Your Secret Key>
  DEBUG=True
  ALLOWED_HOSTS=localhost,127.0.0.1
  DATABASE_URL=postgres://username:password@localhost:5432/db_name
  CELERY_BROKER_URL=redis://localhost:6379/0
  CELERY_RESULT_BACKEND=redis://localhost:6379/0
  ```

### 6. Set Up the Database
Make sure you have PostgreSQL installed and running.
- Create a database and user for the project (if not already created).
- Run migrations to set up the database schema:
  ```bash
  python manage.py migrate
  ```

### 7. Create a Django Superuser
If you want to access the Django admin, you can create a superuser:
```bash
python manage.py createsuperuser
```

### 8. Start the Development Server
Run the development server to check if everything is set up properly:
```bash
python manage.py runserver
```
The application should now be available at `http://localhost:8000`.

---

## Configuration

Ensure the following settings are configured properly:

- **DATABASE_URL**: Make sure to update the database URL to match your PostgreSQL configuration.
- **SECRET_KEY**: Generate a secure Django secret key (explained below).
- **Celery & Redis**: Ensure Redis is installed and running for Celery to work properly.

---

## Generating Django Secret Key

You can generate a secure Django secret key using the following methods:

### 1. Using Django’s `get_random_secret_key` Utility:
Run the following command in Python:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### 2. Online Tools:
You can use online tools such as:
- [Django Secret Key Generator](https://djecrety.ir/)

### 3. Manually:
You can manually create a random string and use it as your secret key:
```bash
'django-insecure-xh$&%fs_90=d*j!h49xv-0df3fo34fjq(=)s9kp1c3o8qtzvx-'
```

Make sure to keep this key secure and never expose it in your public repository.

---

## Running the Project

### Celery & Redis Setup

- **Install Redis**: Ensure Redis is installed and running on your local machine. You can download and install Redis from [here](https://redis.io/download).
  
- **Start Redis**:
  ```bash
  redis-server
  ```

- **Start Celery Worker**:
  In a separate terminal window, run the following to start Celery:
  ```bash
  celery -A your_project_name worker --loglevel=info
  ```

---

## API Documentation

Once the server is running, access the API documentation through **DRF Spectacular** at:
```bash
http://localhost:8000/api/docs/
```
This will give you an interactive interface to explore all the available API endpoints, request methods, and parameters.

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new pull request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

