# Django-Hackathon

A Django project to kick off new projects.

### Requirements
  - Django 1.7
  - django-bootstrap3
  
### Installation
First `git clone` this repo, then install the requirements using pip(I am using virtualenv with python 2.7.6):

```
pip install -r requirements.txt
```

Now, inside the django_hackathon settings folder (the one with the settings.py), you must crete a `settings_local.py` file with a `SECRET_KEY`:

```
SECRET_KEY = 'LARGE RANDOM VALUE YOU MUST CREATE'
```

That's the way to keep your keys, passwords and tokens only local.

### Clean Bootstrap
I've created a branch called `clean-bootstrap`, that holds just a Django Project with Twitter-Bootstrap pre-configured, so you just have to create your views and extend the `base.html` template.

### Todo's
  - Create all user generic views
  - Create Facebook / Twitter / Google Plus Login
  - Use Pipeline / Yui Compressor (not sure yet)

### Author

** Fernando Freitas Alves (ffreitasalves@gmail.com) **

### Contributors

> Please feel free to contribute
