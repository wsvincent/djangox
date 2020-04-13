<h1 align="center"><img align="center" width="300" src="logo.png" alt="DjangoX logo"></h1>

> **NOTE**: This open source project is supported by [LearnDjango.com](https://learndjango.com).

## Features

* [x] Django 3.0.x
* [x] [Bootstrap v4](https://github.com/twbs/bootstrap)
* [x] Registration via [django-allauth](https://github.com/pennersr/django-allauth)
* [x] Static files properly configured


* [x] [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) for debugging
* [x] [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) for DRY forms

## Demo

![Demo Video](https://github.com/wsvincent/djangox/blob/master/demo.gif)

## Install

```
$ git clone https://github.com/wsvincent/djangox.git
$ cd djangox
$ pipenv install
$ pipenv shell
```

## Usage

```
# Run Migrations
(djangox) $ python manage.py makemigrations users

# Migrate the Database
(djangox) $ python manage.py migrate

# Create a Superuser:
(djangox) $ python manage.py createsuperuser

# Confirm everything is working:
(djangox) $ python manage.py runserver

# Load the site at http://127.0.0.1:8000
```

<!-- ## Docker Usage
```
# Build the Docker Image
$ docker-compose build

# Run Migrations
$ docker-compose run --rm web python manage.py migrate

# Migrate the Database
$ python manage.py migrate

# Create a Superuser
$ docker-compose run --rm web python manage.py createsuperuser

# Run Django on http://localhost:8000/
$ docker-compose up

# Run Django in background mode
$ docker-compose up -d

# Stop all running containers
$ docker-compose down

# Run Tests
$ docker-compose run --rm web pytest

# Re-build PIP requirements
$ docker-compose run --rm web pip-compile requirements/requirements.in
```-->


<!-- ## Next Steps

- Use [PostgreSQL locally via Docker](https://wsvincent.com/django-docker-postgresql/)
- Use [django-environ](https://github.com/joke2k/django-environ) for environment variables
- Update [EMAIL_BACKEND](https://docs.djangoproject.com/en/3.0/topics/email/#module-django.core.mail) to configure an SMTP backend
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure)

## Adding Social Authentication

- [Configuring Google](https://wsvincent.com/django-allauth-tutorial-custom-user-model/#google-credentials)
- [Configuring Facebook](http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Create_and_configure_a_Facebook_app)
- [Configuring Github](https://wsvincent.com/django-allauth-tutorial/)
- `django-allauth` supports [many, many other providers in the official docs](https://django-allauth.readthedocs.io/en/latest/providers.html) -->

## 🤝 Contributing

Contributions, issues and feature requests are welcome! See [CONTRIBUTING.md](https://github.com/wsvincent/djangox/blob/master/CONTRIBUTING.md).

## Show your support

Give a ⭐️ if this project helped you!
