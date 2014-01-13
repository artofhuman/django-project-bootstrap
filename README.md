# project_name|title
## Prerequisites

    - python >= 2.6
    - pip
    - virtualenv/wrapper (optional)

# Create Django Project From template

    django-admin.py startproject --template https://github.com/artofhuman/django-project-bootstrap/zipball/master project_name

# Start project

    cd project_name
    virtualenv --no-site-packages ENV
    source ENV/bin/activate
    pip install -r reqs.txt
    pip freeze > reqs.txt
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver

# Run tests

    python manage.py test --settings=project_name.test_settings
