# project_name|title
## Prerequisites

    - python >= 2.7 or >=3.0

# Usage
## Create Django Project From template

    django-admin.py startproject --template https://github.com/artofhuman/django-project-bootstrap/zipball/master project_name

## Install requirements

  for development run `pip install -r requirements/development.txt`
  for production run `pip install -r requirements.txt`

# Run tests

    python manage.py test --settings=project_name.test_settings
