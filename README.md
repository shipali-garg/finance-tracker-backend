Finance Tracker Backend
Overview
This is a backend system built using Django and Django REST Framework to manage financial transactions. 
It allows users to store income/expense records and view summaries of their financial data.

Features
•	Add, update, delete transactions
•	View all transactions
•	Filter by category and type
•	Get summary (income, expense, balance)
•	Monthly summary (extra)
•	Recent transactions (extra)
•	Role-based access (viewer, analyst, admin)

Tech Used
•	Python
•	Django
•	Django REST Framework
•	SQLite

How to Run
1.	Clone the repo
git clone https://github.com/shipali-garg/finance-tracker-backend.git
cd finance-tracker-backend
2.	Create virtual environment
python -m venv .venv
.venv\Scripts\activate
3.	Install dependencies
pip install django djangorestframework djangorestframework-simplejwt
4.	Run migrations
python manage.py makemigrations
python manage.py migrate
5.	Create admin user
python manage.py createsuperuser
6.	Run server
python manage.py runserver

API Endpoints
Method	   Endpoint	                Description
POST	     /api/login/	            Get JWT token
GET	       /api/transactions/	      List transactions
POST	     /api/transactions/	      Create transaction
GET	       /api/summary/	          Financial summary
GET	       /api/monthly-summary/	  Monthly analytics
GET	       /api/recent/	            Recent transactions

Notes
•	Roles can be assigned from admin panel
•	Viewer → only view
•	Admin → full access

Author
Shipali Garg


