# Django Rest Framework - Internship tasks

This repository contains a base project for internship program at EBS Integrator. Fork it and bring it to the next level.

### References

1. https://www.djangoproject.com/
2. https://www.django-rest-framework.org/
3. https://restfulapi.net/
4. https://swagger.io/docs/specification/2-0/what-is-swagger/

## Requirements
* [Python 3.8](https://docs.python.org/3.8)
* [Django 3.1](https://docs.djangoproject.com/en/3.1)

### Setup

Some steps before start work on tasks.

1. Install python requirements ```pip install -r requirements.txt```
2. Database is SQLite, local, and execute ```python manage.py migrate```
3. Start the project ```python manage.py runserver```
4. Open website and register a user in /users/register/ endpoint
5. Login with registered credentials in /users/token/ endpoint
6. In swagger click "Authorize" button and type ```Bearer <access token from response>```
7. Let's do first milestone!

### Milestone 1

We start with some changes to understand the project code

1. Add in Blog model a boolean field ```enabled``` to make some posts published or unpublished
2. Show in Django Admin blog list the real blog name and status (enabled/disabled): http://prntscr.com/nnsoa8 docs: https://docs.djangoproject.com/en/3.0/ref/contrib/admin/
3. Make an endpoint for create a blog post (similar as register endpoint) that will add a new record in blog table
4. Create a new model ```Comments``` with ```text``` and ```blog``` foreign key, here we will save comments for each blog post
5. Add Comments for management in Django Admin
6. Create an endpoint that creates a comment to a blog post (input: blog_id, text)
7. In endpoint ```/blog/blog/{id}/``` return the Blog post object and list of comments.

### Milestone 2

Based on previous experience, create a new project with a simple Task Management system. 
You need to set up DB, DRF and Swagger to build a beautiful API.

These screens will help you to imagine the app:
1. List: https://prnt.sc/1q9sn7i
2. Create: http://prntscr.com/novbj8
3. View: http://prntscr.com/novbth

**Tasks:**
1. Register - user send first name, last name, email, password and receive JWT token for authentication
2. Login - user send email, password and receive JWT token for authentication
3. Get list of users - user receive a list with id and full name of all users from application
4. Create a task - user send title, description and receive new task id, the new task is assigned to current user
5. View list of tasks - user receive a list with id and title of all created tasks from application
6. View task details by id - user send task_id and receive task details: id, title, description, status, owner
7. View my tasks - user receive a list with id and title of tasks assigned to him
8. View Completed tasks - user receive a list with id and title of tasks with status completed
9. Assign a task to user - user send task_id and user_id and receive successful response after update task owner
10. Complete a task - user send task_id and receive successful response after update of task status in completed
11. Remove task - user send task_id and receive successful response after task deletion
12. Add comment to task - user send task_id, comment text and receive id of the new comment
13. View task comments - user send task id and receive list of all comments added to this task
14. Add email notification when task is assigned to me
15. Add email notification when my task is commented
16. Add email notification when commented task is completed
17. Search task by title - user send search term and receive list of tasks that match 

### Milestone 3

Add these new functions to your task application to help users to track time spent on completion of each task.
User will start time when start working on task and stop it when complete the task or take a pause.

1. Start a timer for my task - user send task id and receive successful response after logging the start of task in DB
2. Stop timer for the started task - user send task id and receive successful response after adding a time log for this task with duration of work for current date
3. Add time log for a task on a specific date - user manually send in task id, date, duration in minutes and receive successful response of save
3. Get a list of time logs records by task - user send task id and receive list of all time logs created for this task 
4. Change get list of tasks endpoint get receive the sum of the time in minutes for each task
5. Get the logged time in last month - user send a request and receive total amount of time logged by him in last month
6. Get top 20 tasks in last month by time - user send request and receive list of id, title, time amount of tasks with bigger logged amount of time

### Milestone 4

In this milestone we start to improve our application.

1. Add unit tests for each endpoint https://www.django-rest-framework.org/api-guide/testing/
2. Add coverage package and generate report to be sure in 100% test coverage https://docs.djangoproject.com/en/3.2/topics/testing/advanced/#integration-with-coverage-py
3. Install PostgreSQL docker container and move your app on PostgreSQL (edit settings.py)
4. Create a script that will add random 25.000 tasks and 50.000 time logs (use https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/)
4. Install PGHero docker container and connect it to your db https://github.com/ankane/pghero/blob/master/guides/Docker.md
5. Manual test all endpoints and check with PGHero that all sql queries use db indexes
6. Install Redis docker container and configure Django to cache with 1 minute TTL the endpoint with Top 20 tasks by time for each user https://github.com/jazzband/django-redis
7. Create Dockerfile for your application to run it with docker-compose command
