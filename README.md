## CareerUp JobPortal

<p align="center">
    <img alt="forks" src="https://img.shields.io/github/forks/parad13/CareerUp#jobportal?label=Forks&style=social"/>
    <img alt="stars" src="https://img.shields.io/github/stars/parad13/CareerUp#jobportal?style=social"/>
    <img alt="watchers" src="https://img.shields.io/github/watchers/parad13/CareerUp#jobportal?style=social"/>
    <img alt="github Actions" src="https://github.com/parad13/CareerUp#jobportal/workflows/job-portal/badge.svg"/>
</p>

Live: [Demo](https://careerride.herokuapp.com/)

Used Tech Stack

1. Python
2. Django
3. Django Rest Framework(DRF)
4. MySql

#### Install

1. Create a virtual environment

     `mkvirtualenv env`

2. Activate it

    `workon env`

3. Clone the repository and install the packages in the virtual env:   

    `pip install -r requirements.txt`

4. Check the database settings in the settings.py file and create a .env file with referece to env_text file

#### Run

1.With the venv activate it, execute: (Optional, only used in case of final/production deployment)

    python manage.py collectstatic

*Note* : Collect static is not necessary when debug is True (in dev mode)

2. Create initial database migrations:

    `python manage.py makemigrations`

3. Create initial database:

    `python manage.py migrate`

4. Some useful commands in case got errors in step3: (there might be pending or incomplete migrations that are causing the issue, below command will show migrations happened)

    `python manage.py showmigrations`

5. Based on above step output create/run migrations for each django app mentioned in settings.py
    `python manage.py makemigrations app_name`
    `python manage.py migrate app_name`

6. Some other useful commands:
    `python manage.py dbshell`
    `python manage.py shell`
    `python manage.py migrate --fake`
    `python manage.py migrate --fake-intial`

7. Run server:

    `python manage.py runserver`

Show your support by 🌟 the project!!    
