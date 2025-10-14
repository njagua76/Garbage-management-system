Garbage Collection Management System
📖 Overview

The Smart Garbage Collection Management System is a Python-based command-line interface (CLI) application designed to streamline and digitize the process of managing garbage collection in residential areas. It uses a PostgreSQL database to store and manage data such as tenants, apartments, payments, and garbage bag issuance.

This system aims to help administrators efficiently monitor garbage collection records and promote accountability in waste management.

⚙️ Features

🧾 Tenant Management: Add, view, update, and delete tenant records.

🏢 Apartment Tracking: Record apartment details and link them to tenants.

💰 Payment Module: Track monthly payments for garbage collection services.

🗃️ Garbage Bag Issuance: Record the number of garbage bags issued per month.

📊 Reports: Generate summaries for tenants, payments, and waste collection activity.

💻 Command Line Interface: Lightweight and simple to operate through the terminal.

🧰 Tech Stack
Component	Technology
Language	Python 3
Database	PostgreSQL
Interface	Command-Line Interface (CLI)
ORM/Driver	psycopg2
Version Control	Git & GitHub
🚀 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/garbage-collection-system.git
cd garbage-collection-system

2️⃣ Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure PostgreSQL

Create a PostgreSQL database and update your credentials in the database_utils.py file:

DB_NAME = "garbage_db"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"

5️⃣ Run the Application
python main.py

 Example Functionalities
1. Add new tenant
2. View tenants
3. Record payment
4. Issue garbage bags
5. Generate monthly report
6. Exit

💡 Future Enhancements

Integration with JSON API for remote data updates.

Optional admin login system for security.

GUI version using Tkinter or React + FastAPI backend.

👨‍💻 Author

Ann Gathoni
💬 Passionate about tech, sustainability, and clean solutions for smart communities.