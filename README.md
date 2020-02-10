<img width="400" src="logo.png" alt="DjangoX logo">

## A Django starter project that "just works."

> **NOTE**: This open source project is supported by [LearnDjango.com](https://learndjango.com) which has free tutorials and premium courses.

## Demo

![Demo Video](https://github.com/wsvincent/djangox/blob/master/demo.gif)

## Features

* [x] Django 3.0 & Python 3.7
* [x] Custom user model
* [x] Email/password for user registration and log in
* [x] Static files properly configured, including Favicon
* [x] [django-allauth](https://github.com/pennersr/django-allauth) for social authentication
* [x] [Bootstrap](https://github.com/twbs/bootstrap) for styling
* [x] [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) for debugging
* [x] [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) for DRY forms


## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).

2.  Clone the repo and configure the virtual environment:

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

6. To customize the name of the project, update 3 files by replacing "djangox_project" with your desired name:

* `manage.py`
* `djangox_project/settings.py`
* `djangox_project/wsgi.py`

It's also possible to change the `djangox_project` directory to your desired project name.


## Next Steps

- Use [PostgreSQL locally via Docker](https://wsvincent.com/django-docker-postgresql/)
- Use [django-environ](https://github.com/joke2k/django-environ) for environment variables
- Update [EMAIL_BACKEND](https://docs.djangoproject.com/en/3.0/topics/email/#module-django.core.mail) to configure an SMTP backend
- Make the [admin more secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure)

## Adding Social Authentication

- [Configuring Google](https://wsvincent.com/django-allauth-tutorial-custom-user-model/#google-credentials)
- [Configuring Facebook](http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/#Create_and_configure_a_Facebook_app)
- [Configuring Github](https://wsvincent.com/django-allauth-tutorial/)
- `django-allauth` supports [many, many other providers in the official docs](https://django-allauth.readthedocs.io/en/latest/providers.html)

## Contributing
See [CONTRIBUTING.md](https://github.com/wsvincent/djangox/blob/master/CONTRIBUTING.md).
