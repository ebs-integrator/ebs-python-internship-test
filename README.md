# Simple DRF blog example and test

### Setup

0. In /config/ copy development_sample.py as development.py
1. Database is SQLite, local, and execute ```python manage.py migrate```
2. Start the project
3. Register a user in /users/register/ endpoint
4. Login with registered credentials in /users/token/ endpoint
5. In swagger click "Authorize" button and type ```Bearer <access token from response>```
6. Enjoy other endpoints

### Tasks

#### Milestone 1

1. Add in Blog model boolean field ```enabled```
2. Show in admin blog list the real blog name and status (enabled/disabled): http://prntscr.com/nnsoa8
3. Make an endpoint for create a blog post (similar as register endpoint)
4. Create a model ```Comments``` with ```text``` and ```blog``` foreign key
5. Add Comments in Django Admin
6. Create an endpoint that creates a comment to a blog post (input: blog_id, text)
7. In endpoint ```/blog/blog/{id}/``` return the Blog post object and list of comments

#### Milestone 2

Develop a task management platform

Screens:
1. List: http://prntscr.com/novabn
2. Create: http://prntscr.com/novbj8
3. View: http://prntscr.com/novbth

Functions:
1. Register
2. Login
3. View list of tasks
4. Create a task
5. View my tasks
6. View Completed tasks
7. Assign a task to me
8. Complete a task
9. Remove task
10. Add comment to task
11. View task comments
12. Add notification then task is assigned to me
13. Add notification then my task in commented
14. Add notification then commented task is closed
15. View my notifications
16. View count of new notifications

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
