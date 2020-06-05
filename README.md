# Django Rest Framework example and test

This repository contains a base project for intership program at EBS Integrator. Fork it and bring it to the next level.

### References

1. https://www.djangoproject.com/
2. https://www.django-rest-framework.org/
3. https://restfulapi.net/
4. https://swagger.io/docs/specification/2-0/what-is-swagger/

### Setup

Some steps before start work on tasks.

1. Database is SQLite, local, and execute ```python manage.py migrate```
2. Start the project ```python manage.py runserver```
3. Open website and register a user in /users/register/ endpoint
4. Login with registered credentials in /users/token/ endpoint
5. In swagger click "Authorize" button and type ```Bearer <access token from response>```
6. Let's do first milestone!

### Tasks

#### Milestone 1

1. Add in Blog model a boolean field ```enabled``` to make some posts published or unpublished
2. Show in Django Admin blog list the real blog name and status (enabled/disabled): http://prntscr.com/nnsoa8 docs: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
3. Make an endpoint for create a blog post (similar as register endpoint) that will add a new record in blog table
4. Create a new model ```Comments``` with ```text``` and ```blog``` foreign key, here we will save comments for each blog post
5. Add Comments for management in Django Admin
6. Create an endpoint that creates a comment to a blog post (input: blog_id, text)
7. In endpoint ```/blog/blog/{id}/``` return the Blog post object and list of comments.

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

#### Milestone 3

New functions for task application

1. Start a timer for my task (send task id and time starts)
2. Stop timer for the started task (on stop the API will log the time from start in a table)
3. Add time log for a task on a specific date (send in endpoint task id, date, duration in minutes)
3. Get a list of time logs records by task ID
4. On getting tasks endpoint get the sum of the time on each task
5. Get the logged time in last month by date
6. Get top 20 tasks in last month that has more time


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
