# Simple DRF blog example and test

### Setup

0. In /config/ copy development_sample.py as development.py
1. Database is SQLite, local, and execute ```python manage.py migrate```
2. Start the project
3. Register a user in /users/register/ endpoint
4. Login with registered credentials in /users/token/ endpoint
5. In swagger click "Authorize" button and type Bearer<space>access token from response
6. Enjoy other endpoints

### Tasks

1. Add in Blog model boolean field ```enabled```
2. Show in admin blog list the real blog name and status (enabled/disabled): http://prntscr.com/nnsoa8
3. Make an endpoint for create a blog post (similar as register endpoint)


### Config

For run project in another ENV:

```bash
DJANGO_ENV = production
```

default value is ```development```


### Create a new app

```bash
mkdir -p apps/name_of_app
python manage.py startapp name_of_app apps/name_of_app
```
