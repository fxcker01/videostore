# 🎓 Educore – Online Course Platform

A modern, dark-themed online learning platform built with Django, Tailwind CSS, and PostgreSQL. Educore allows users to register, browse categorized programming courses, view lessons, and manage personal profiles with subscription support.

---

## 🛠 Technologies Used

- **Backend**: Python, Django
- **Frontend**: Tailwind CSS, HTML, JavaScript
- **Database**: SQLite (default), PostgreSQL (for production)
- **Deployment**: Railway, GitHub, Gunicorn

---

## 🚀 Features

- User registration, login, logout
- Profile with avatar and email editing
- Course & lesson pages with video embedding
- Access control (free/paid content)
- Category-based course filtering
- Pagination support
- Tailwind-powered adaptive UI
- Admin course creation panel

---

## ⚙️ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/fxcker01/videostore.git
cd videostore
```

### 2. Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations and create superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Start the development server
```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/` 🎉

---

## 🌐 Deployment on Railway

### .env file example:
```ini
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=.yourdomain.com,127.0.0.1,localhost
```

### Procfile:
```procfile
web: gunicorn videostore.wsgi
```

---

## 📁 Project Structure
```
videostore/
├── courses/          # Course and lesson logic
├── users/            # Registration, login, profile
├── templates/        # All templates grouped by app
├── static/           # Tailwind CSS and JS
├── media/            # Uploaded images (course covers, avatars)
├── .env
├── .gitignore
├── Procfile
├── requirements.txt
├── LICENSE
└── README.md
```

---


## 📄 License
This project is licensed under a **Custom Proprietary License**.  
Copying, distribution or usage without permission is strictly prohibited.  
See [LICENSE](LICENSE) for more information.

Created by [fxcker01](https://github.com/fxcker01) 🖤