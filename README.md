# 📝 Django Blog App

A fully functional, dynamic blog application built using **Django** and **Bootstrap 5**. This project features a responsive design, a custom dark mode toggle, and a complete admin interface for managing posts.

## 🚀 Features

* **Dynamic Content:** All blog posts are fetched from the database.
* **Modern UI:** Built with Bootstrap 5 for a responsive and clean look.
* **Dark/Light Mode:** Includes a theme toggle button that persists user preference (using LocalStorage).
* **Home & Detail Views:** Dedicated homepage with "Latest Posts" grid and individual detail pages for articles.
* **Admin Panel:** Easy-to-use Django admin dashboard to create, edit, and delete posts.
* **Template Inheritance:** Uses a scalable `base.html` structure.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, Bootstrap 5.3, JavaScript
* **Database:** SQLite (Default)
* **Development Environment:** Developed on Android using Acode & Termux.

## 📸 Screenshots

*(You can add screenshots here later)*

## 📦 How to Run Locally

If you want to run this project on your machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Alexashok99/django-blog-app.git](https://github.com/Alexashok99/django-blog-app.git)
    cd django-blog-app
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # Linux/Mac/Termux
    source .venv/bin/activate
    ```

3.  **Install Requirements:**
    ```bash
    pip install django
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Start the Server:**
    ```bash
    python manage.py runserver
    ```

6.  Open `http://127.0.0.1:8000/` in your browser.

---
*Created with ❤️ by Alexashok99*