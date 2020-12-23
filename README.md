## CareerUp JobPortal

<p align="center">
    <img alt="forks" src="https://img.shields.io/github/forks/parad13/CareerUp#jobportal?label=Forks&style=social"/>
    <img alt="stars" src="https://img.shields.io/github/stars/parad13/CareerUp#jobportal?style=social"/>
    <img alt="watchers" src="https://img.shields.io/github/watchers/parad13/CareerUp#jobportal?style=social"/>
    <img alt="github Actions" src="https://github.com/parad13/CareerUp#jobportal/workflows/job-portal/badge.svg"/>
</p>

Live: [Demo](https://careerride.herokuapp.com/)

Used Tech Stack

1. Django
2. MySql

#### Install

1. Create a virtual environment

     `mkvirtualenv env`

2. Activate it

    `workon env`

3. Clone the repository and install the packages in the virtual env:   

    `pip install -r requirements.txt`

#### Run

1.With the venv activate it, execute:

    python manage.py collectstatic

*Note* : Collect static is not necessary when debug is True (in dev mode)

2. Create initial database:

    `python manage.py migrate`

3. Run server:

    `python manage.py runserver`

Show your support by 🌟 the project!!    
