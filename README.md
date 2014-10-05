# project_name|title
## Prerequisites

    - python >= 2.6
    - pip
    - virtualenv/wrapper (optional)

# Usage
## Create Django Project From template

    django-admin.py startproject --template https://github.com/artofhuman/django-project-bootstrap/zipball/master project_name

## Install requirements

for development run `pip install -r requirements/development.txt`


# Run tests

    python manage.py test --settings=project_name.test_settings
