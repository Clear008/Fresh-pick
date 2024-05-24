`cd webapp`

`python -m venv venv`

`./venv/scripts/activate`

`pip install django`

`py manage.py makemigrations`

`py manage.py migrate`

`py manage.py runserver`

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- MySQL
- Node.js (for frontend, if applicable)

### Backend Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/khalilelamraoui/Fresh-pick.git
    cd Fresh-Pick
    ```

2. Create and activate a virtual environment:

    ```bash
    cd webapp
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    pip install django
    ```

4. Configure your MySQL database in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

5. Run migrations and start the server:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```


## Usage

- Access the application at `http://localhost:8000`
