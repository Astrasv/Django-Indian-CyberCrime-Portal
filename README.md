# Cybercrime Portal for India

This project is a Cybercrime Portal specifically designed for India. It serves as a centralized platform to manage, report, and visualize cybercrime incidents across the country.

## Features

- **CRUD Operations:** Allows Create, Read, Update, and Delete functionalities for cybercrime incidents and data.
- **Map Visualization:** Utilizes Django with mapping libraries (specify libraries if applicable) to display the geographical distribution of cybercrime incidents in India.
- **User Authentication:** Implements secure user authentication and access control mechanisms.
- **Incident Reporting:** Enables users to report cybercrime incidents with relevant details.
- **Data Analysis Tools:** Provides tools for analyzing trends, patterns, and statistics related to cybercrime.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Astrasv/cybercrime-portal.git
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the portal:**
   Open a web browser and go to `http://127.0.0.1:8000/` to access the Cybercrime Portal.

## Usage

- **Admin Dashboard:** Access the admin panel at `http://127.0.0.1:8000/admin/` to manage cybercrime incidents and user data.
- **Reporting Incidents:** Explain how users can report cybercrime incidents through the portal.
- **Data Analysis:** Provide instructions on how to utilize data analysis tools if available.



## Acknowledgments

- I have used Corey Schauffer tutorail to create the blog application and built the rest of the applications by myself, using the concept learnt in the blog application tutorial
