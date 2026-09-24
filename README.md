# Decode the Dark Side of the Language Applications of LLMs in the Dark Web

## 📖 Project Overview
This project is an advanced web-based platform built with Django designed to detect, analyze, and mitigate threats originating from language applications (such as LLMs) within the Dark Web. It utilizes comprehensive text analysis, slang dictionaries, pattern matching, and threat scoring algorithms to identify suspicious communication patterns, illegal terminology, and evasive operations.

## ✨ Features
- **User Management**: Role-based access control with specific roles such as `Admin`, `User`, and `Hacker` to manage operational boundaries.
- **Dataset Analysis**: Upload entire datasets (CSV, JSON, TXT, PDF) to be queued and analyzed automatically by the system.
- **Manual Text Analysis**: A quick-input interface for real-time analysis of raw text snippets to detect immediate threats.
- **Advanced Threat Detection**:
  - **Category Classification**: Classifies text into specific threat domains (e.g., narcotics, cybercrime).
  - **Keyword & Slang Identification**: Detects encoded Dark Web terminology and translates known slangs.
  - **Multilingual Support**: Flags text containing mixed language elements typically used for evasion.
  - **Risk Scoring**: Calculates a confidence score and assigns a Threat Level (Low, Medium, High).
- **Intelligent Summarization**: Generates human-readable summaries detailing the detected threat intent and key indicators.
- **Reporting**: Automatically generates downloadable PDF reports detailing the findings.
- **Audit & Logging**: Detailed tracking of user activity, dataset uploads, and analysis tasks for compliance and monitoring.

## 🛠️ Tech Stack
- **Backend**: Python 3.11, Django 4.2+
- **Database**: MySQL (via `mysqlclient`)
- **PDF Processing**: `PyPDF2` (for reading PDF datasets), `reportlab` (for generating PDF reports)
- **Frontend**: HTML, CSS, JavaScript (Django Templates)

## ⚙️ Prerequisites
Before running the project locally, ensure you have the following installed:
1. Python 3.11+
2. MySQL Server (Ensure it's running locally on port 3306)
3. `pip` (Python package installer)

## 🚀 Step-by-Step Installation

### Step 1: Clone the Repository
Open your terminal and navigate to your preferred directory, then clone the project (if applicable) or navigate into the project root folder.

```bash
cd "Decode the Dark Side of the Language Applications of LLMs in the Dark Web\Source Code\DECODE THE DARK SIDE OF THE LANGUAGE APPLICATIONS OF LLMS IN THE DARK WEB"
```

### Step 2: Set Up Database (MySQL)
The project is configured to use MySQL. Create the corresponding database using your MySQL client:
```sql
CREATE DATABASE dark_decode_db;
```
*(Note: Default credentials configured in `core/settings.py` are User: `root`, Password: `root`. Update them if your local MySQL setup differs).*

### Step 3: Install Dependencies
Install all required Python packages from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Apply Database Migrations
Set up your database schema by applying Django migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Admin Account)
To access the admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set your username, email, and password.

### Step 6: Run the Development Server
Start the Django application locally:
```bash
python manage.py runserver
```

## 💻 Usage Instructions

1. **Access the App**: Open your web browser and go to `http://localhost:8000`.
2. **Login/Register**: Create a new account or log in with your credentials.
3. **Dashboard**: Navigate to your dashboard where you can see recent activities and notifications.
4. **Upload Dataset**: Go to the Dataset Upload section. You can upload files (PDF, CSV, JSON, TXT) which will be processed by the internal analyzers.
5. **Manual Analysis**: Use the Manual Analysis view to paste a block of text directly and instantly receive a threat report, complete with intent categories, slang translations, and AI summaries.
6. **Generate Reports**: After analysis, utilize the report generation feature to export your findings as a PDF.
7. **Admin Tools**: Log in as a superuser to access `http://localhost:8000/admin` to manually configure Threat Keywords, Slang Dictionaries, Threat Patterns, and Risk Rules dynamically.

## 🔮 Future Enhancements
- Integration of actual LLM APIs (OpenAI/Gemini) inside the `ai_summary` pipeline for deeper semantic analysis of encrypted intent.
- Scaling database deployment and background task queues (e.g., Celery) for massive dataset operations.
