Django Job Scraper:

📌 Project Overview:
This project is a Django-based Job Scraper that extracts Python Developer job listings from Indeed.com using Selenium and stores the data in MongoDB. It also includes a Django Admin Panel to manage job listings and provides insights into the average salary of Python developers in different cities using NumPy.

🚀 Features:
-Web Scraping: Extracts job listings from Indeed using Selenium.
-Database Storage: Stores job listings in MongoDB.
-Django Admin Panel: Allows admins to search, edit, and delete jobs.
-Salary Calculation: Uses NumPy to calculate the average salary per city.
-Deployment: The Django panel is hosted online.

🛠️ Installation and Setup:
1️⃣ Clone the Repository
git clone https://github.com/sweekarmishra/django-job-scraper.git
cd django-job-scraper

2️⃣ Create a Virtual Environment & Install Dependencies
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Set Up MongoDB
Install and run MongoDB.
Create a database named job_scraper_db.
Update your Django settings.py to configure MongoDB connection.

4️⃣ Set Up Environment Variables
Create a .env file in the root directory and add:
MONGO_URI=mongodb://localhost:27017/job_scraper_db
SECRET_KEY=your_django_secret_key

5️⃣ Run Migrations & Start the Server
python manage.py migrate
python manage.py runserver

Your Django app should now be running at http://127.0.0.1:8000/

🕵️‍♂️ How to Scrape Jobs
-Run the scraper using:
-python scrape_jobs.py

🎯 Project Structure
├── job_scraper_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── ...
│
├── scraper/
│   ├── scrape_jobs.py
│   ├── selenium_utils.py
│
├── templates/
├── static/
├── db.sqlite3  # (Ignored in Git)
├── manage.py
└── README.md

📤 Deployment
To deploy this Django project online, follow these steps:
-Use Heroku, AWS, or any hosting platform.
-Set up MongoDB Atlas for a cloud database.
-Update allowed hosts and environment variables.

📌 Conclusion

This project is a powerful tool for scraping and analyzing job data. Feel free to contribute or suggest improvements!
📧 Contact: aimlsweekarmishra@gmail.com

