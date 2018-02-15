# DjangoX

**DjangoX** - A framework for launching new Django projects quickly.

Comes with a custom user model, social authentication, and email/password for sign up and log in.

![Falconx](static/images/falconx.png)

## Features

* Django 2.0 and Python 3.6
* [Pipenv](https://github.com/pypa/pipenv) for virtualenvs
* User registration via [django-allauth](https://github.com/pennersr/django-allauth)
* Add social auth via Google, Facebook, etc
* [Bootstrap v4](https://getbootstrap.com/)
* Custom user model with email and no username

## First-time setup

1. Make sure Python 3.6x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2. Install packages with `pipenv install`
3. Activate a virtual environment with `pipenv shell`
4. Set up the initial migration for our custom user models in `users`

   $ python manage.py makemigrations users

5. Build the database schema:

   $ python manage.py migrate

6. Create a superuser:

   $ python manage.py createsuperuser

7. Confirm everything is working:

   $ python manage.py runserver

   Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000).

   Click on links for "Sign up" or "Log in."

8. This is optional but I also recommend logging into admin and changing the default site:

   Go to [http://127.0.0.1:8000/admin]([http://127.0.0.1:8000/admin]). You may need to logout and then login with your superuser account.

   Navigate to [http://127.0.0.1:8000/admin/sites/site/](http://127.0.0.1:8000/admin/sites/site/) and change the default "example.com" to "127.0.0.1" and the name to "<YOUR_PROJECT_NAME>" for local development.

## Recommendations

* Use [PostgreSQL locally via Docker](https://wsvincent.com/django-docker-postgresql/)
* Use [django-environ](https://github.com/joke2k/django-environ) for environment variables
* Update [EMAIL_BACKEND](https://docs.djangoproject.com/en/2.0/topics/email/#module-django.core.mail) to [configure an SMTP backend](https://djangoforbeginners.com/password-change-reset/)
* Add [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) and [django-extensions](https://github.com/django-extensions/django-extensions)

* Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure)

## Adding Social Authentication

* [Configuring Google](https://wsvincent.com/django-allauth-tutorial-custom-user-model/#google-credentials)
* [Configuring Facebook](http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Create_and_configure_a_Facebook_app)
* [Configuring Github](https://wsvincent.com/django-allauth-tutorial/)
* `django-allauth` supports [many, many other providers in the official docs](https://django-allauth.readthedocs.io/en/latest/providers.html)

## Acknowledgments

This project is heavily inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django). It's my own preferred template for starting new projects built out of a personal desire to actually understand all the config magic in `cookiecutter-django`.
