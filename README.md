Educore – Online Course Platform
A stylish, fully functional Django-powered course platform with user registration, subscriptions, lesson video playback, Tailwind CSS interface, and mobile-adaptive layout. Designed for educational projects, portfolios, or SaaS-like applications.

🛠 Technologies Used
Backend:

Python

Django

Frontend:

Tailwind CSS

HTML5

JavaScript

Database:

SQLite (local) / PostgreSQL (Railway)

Deployment:

Railway

Git + GitHub

🚀 Features
🔐 User authentication (Register, Login, Logout)

🧑‍💻 Personal user dashboard with profile image update

🎥 Course + lesson management with YouTube video support

💳 Subscription model (Free & Paid courses)

🖼 Modern, responsive UI with Tailwind

💾 Admin panel for adding courses and lessons

📂 Organized and scalable project structure

⚙️ Getting Started
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/fxcker01/videostore.git
cd videostore
2. Set up virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run migrations and create superuser
bash
Copy
Edit
python manage.py migrate
python manage.py createsuperuser
5. Start the development server
bash
Copy
Edit
python manage.py runserver
Open your browser at http://127.0.0.1:8000/ 🎉

🌐 Deployment on Railway
Make sure your .env file contains:

ini
Copy
Edit
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=.yourdomain.com,127.0.0.1,localhost
And Procfile should contain:

procfile
Copy
Edit
web: gunicorn videostore.wsgi
📁 Project Structure
bash
Copy
Edit
videostore/
├── courses/           # Course and lesson logic
├── users/             # Registration, login, profile
├── templates/         # All templates grouped by app
├── static/            # Tailwind CSS and JS
├── media/             # Uploaded images (course covers, avatars)
├── .env
├── .gitignore
├── Procfile
├── requirements.txt
├── LICENSE
└── README.md


## 📄 License
This project is licensed under a **Custom Proprietary License**.  
Copying, distribution or usage without permission is strictly prohibited.  
See [LICENSE](LICENSE) for more information.

Created by [fxcker01](https://github.com/fxcker01) 🖤