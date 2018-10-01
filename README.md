# DjangoX

A framework for launching new Django projects quickly. Comes with a complete user authentication flow, custom user model, and social authentication options via Gmail, Facebook, Twitter, etc.

> **NOTE**: This open source project is supported by my two published books [Django for Beginners and REST APIs with Django](https://wsvincent.com/books/). Learn how to build, test, and deploy websites with Django.

## Features

- For Django 2.1 and Python 3.7
- Modern virtual environments with [pipenv](https://github.com/pypa/pipenv)
- Styling with [Bootstrap](https://github.com/twbs/bootstrap) v4.1.3
- Custom user model
- Email/password for log in/sign up instead of Django's default username/email/password pattern
- Social authentication via [django-allauth](https://github.com/pennersr/django-allauth)
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2.  Clone the repo and configure the virtualenv:

```
$ git clone https://github.com/wsvincent/djangox.git
$ cd djangox
$ pipenv install
$ pipenv shell
```

3.  Set up the initial migration for our custom user models in `users` and build the database.

```
(djangox) $ python manage.py makemigrations users
(djangox) $ python manage.py migrate
```

4.  Create a superuser:

```
(djangox) $ python manage.py createsuperuser
```

5.  Confirm everything is working:

```
(djangox) $ python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000).

![Home](static/images/home.png)

![Sign up](static/images/signup.png)

<!-- ![Log in](static/images/login.png)

![About](static/images/about.png)

![Forget password](static/images/forgetpassword.png) -->

## Next Steps

- Use [PostgreSQL locally via Docker](https://wsvincent.com/django-docker-postgresql/)
- Use [django-environ](https://github.com/joke2k/django-environ) for environment variables
- Update [EMAIL_BACKEND](https://docs.djangoproject.com/en/2.0/topics/email/#module-django.core.mail) to configure an SMTP backend
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure)

## Adding Social Authentication

- [Configuring Google](https://wsvincent.com/django-allauth-tutorial-custom-user-model/#google-credentials)
- [Configuring Facebook](http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Create_and_configure_a_Facebook_app)
- [Configuring Github](https://wsvincent.com/django-allauth-tutorial/)
- `django-allauth` supports [many, many other providers in the official docs](https://django-allauth.readthedocs.io/en/latest/providers.html)

## Learn More

Want to build _DjangoX_ from scratch and understand how it all really works? Check out my book-length look at Django which overs how to build five progresively more complex web applications in Django, starting with a "Hello, World" app and concluding with a robust Newspaper app with complete user authentication flow, custom user model, foreign keys, and more.

The first 4 chapters are available for free online at [https://djangoforbeginners.com/](https://djangoforbeginners.com/).

[![Django for Beginners](https://wsvincent.com/assets/images/dfb_cover300.jpg)](https://djangoforbeginners.com)

## Acknowledgments

This project is heavily inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django). If you're looking for an even more advanced framework that comes with deployment configurations, give it a look!
