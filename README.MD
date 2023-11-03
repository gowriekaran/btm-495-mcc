# MCC Student Recruitment Process Prototype

Prototype of MCC Student Recruitment Process for BTM 495 course

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.11.3)
- Django (version 4.2.7)

## Installation

To use this project on your local machine, follow these steps:

1. **Clone the Repository**

   ```
   git clone https://github.com/gowriekaran/btm-495-mcc.git
   cd btm-495-mcc/
   ```

2. **Set Up a Virtual Environment (Optional)**

   ```
   python -m venv venv  # Replace 'venv' with your preferred environment name
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. **Install Dependencies**

   ```
   pip install -r requirements_windows.txt # On Mac, use requirements_mac.txt
   ```

4. **Create a .env File at the Project's Root Directory**

   In the root directory of your project, create a file named .env and define your database URL like this:

   ```
   DATABASE_URL=your_database_url
   ```

5. **Launch the Development Server**

   ```
   python manage.py runserver
   ```
