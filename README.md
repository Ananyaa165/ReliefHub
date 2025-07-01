# ReliefHub - Django Hospital Management System 🏥

ReliefHub is a web-based hospital management system built with Django. It helps hospitals manage appointments, patient records, doctor schedules, billing, and feedback efficiently.

## 💡 Features
- Patient registration and appointment booking
- Doctor listing and schedules
- Geolocation integration
- Feedback system using Local Storage
- Admin panel (Django's built-in)
- Fully responsive with Tailwind CSS

## 🚀 Tech Stack
- Python 3
- Django
- HTML, CSS (Tailwind)
- JavaScript
- SQLite (default)

## ⚙️ How to Run Locally
```bash
git clone https://github.com/Ananyaa165/ReliefHub.git
cd ReliefHub
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
