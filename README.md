# Django Rest Framework - Internship tasks

This repository contains a base project for internship program at EBS Integrator, each candidate for position of Junior
Backend Developer must be able to develop all the tasks in the following lists. Fork it and bring it to the next level.

### Workflow

1. Before starting this program you should know Python or another programming language at a level beginner, and
   understand syntax, variables, functions, algorithms, etc. If you have lacked in language understanding then start
   with https://www.learnpython.org/
2. First milestone is to prove that you are ready for internship program
3. Before each milestone estimate each task in hours of work to understand how much time you need to achieve the finish,
   don't worry if your estimations are wrong because you don't have experience.
4. After each milestone or sequence of tasks create a merge request to your mentor to receive feedback, after code
   review you will have something to fix this will improve your coding skills
5. Stay focused on tasks and ask questions if you don't understand something and can't find it on Google (googling is a
   basic skill for developers).

#### References

1. https://www.djangoproject.com/ - official documentation of Django framework
2. https://www.django-rest-framework.org/ - documentation of DRF, an package for Django to transform it in a full REST
   API framework
3. https://restfulapi.net/ - documentation about REST APIs communication standard
4. https://github.com/ebs-integrator/rest-api-guide - A short REST API guide used in the company
5. https://swagger.io/docs/specification/2-0/what-is-swagger/
6. https://github.com/HackSoftware/Django-Styleguide - A styleguide for Django developers
7. https://www.django-antipatterns.com/ - A resource with most frequent mistakes in Django development

#### Project requirements

* [Python 3.12](https://docs.python.org/3.12)
* [Django 4.2](https://docs.djangoproject.com/en/4.2)

### First steps to run the project

Some steps before start work on tasks.

https://docs.djangoproject.com/en/4.2/intro/install/

1. Install poetry ```pip install poetry```
2. Install python requirements ```poetry install```
3. Install pre-commit hooks ```pre-commit install```
4. Database is SQLite, local, and execute ```python manage.py migrate```
5. Start the project ```python manage.py runserver```
6. Open website and register a user in /users/register endpoint
7. Login with registered credentials in /users/token endpoint
8. In swagger click "Authorize" button and type ```Bearer <access token from response>```
9. Let's do first milestone!

### Milestone 1

We start with some changes to understand the project code

#### What will you learn

1. How to add new fields in Django Models
2. How to add new Django Models entities
3. How to create a new API endpoint that add data in database
4. How to manage information in Django Admin

#### Tasks

1. Add in Blog model a boolean field ```enabled``` to make some posts published or unpublished (
   ref: https://docs.djangoproject.com/en/4.2/ref/models/fields/#booleanfield)
2. Open in Django Admin (access /admin website section) and add in Blog list the real blog name and status (
   enabled/disabled): [Preview](https://github.com/ebs-integrator/ebs-python-internship-test/blob/master/static/blog_list.png) (
   ref: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)
3. Make an endpoint for create a blog post (similar as register endpoint) that will add a new record in blog table (
   ref: https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)
4. Create a new model ```Comments``` with ```text``` and ```blog``` foreign key, here we will save comments for each
   blog post.
5. Add Comments for management in Django Admin (
   ref: https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#modeladmin-objects)
6. Create an endpoint that creates a comment to a blog post (input: blog_id, text)
7. In endpoint ```/blog/{id}``` return the Blog post object and list of comments.

### Milestone 2

Based on previous experience, create a new project with a simple Task Management system.
You need to set up DB, DRF and Swagger to build a beautiful API.

#### What will you learn

1. How to create new projects
2. How to design a database
3. How to create a full API
4. How to send email notifications

#### Task description:

These screens will help you to imagine the app:

1. [List](https://github.com/ebs-integrator/ebs-python-internship-test/blob/master/static/list.png)
2. [Create](https://github.com/ebs-integrator/ebs-python-internship-test/blob/master/static/create.png)
3. [View](https://github.com/ebs-integrator/ebs-python-internship-test/blob/master/static/view.png)

#### Tasks:

1. Create a new django project with the same file structure like previous project (
   ref: https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
2. Install poetry and pre-commit hook as in previous project
3. Copy "common" and "users" apps from previous project and start the project
4. Create Register endpoint - user send first name, last name, email, password and receive JWT access token and refresh
   token for authentication.

   Example:
   ```json
   {
       "access": "eyJ...",
       "refresh": "eyJ..."
   }
   ```
5. Create Login endpoint - user send email, password and receive JWT access token and refresh
   token for authentication.

   Example:
    ```json
    {
         "access": "eyJ...",
         "refresh": "eyJ..."
    }
    ```
6. Get list of users endpoint - user receive a list with id and full name of all users from application
7. Create a new "tasks" app that will have Task model with title, description and status fields(Choices: Open, In
   Progress, Completed, Canceled, Archived)
8. Create a task endpoint - user send title, description and receive new task data, the new task is assigned to current
   user
9. View list of tasks - user receive a list with id and title of all created tasks from application
10. View task details by id - user send task_id and receive task details: id, title, description, status, owner
11. Add filter by user_id in get list of tasks endpoint to receive tasks assigned to specific user
12. Add status filter in get list of tasks endpoint to receive tasks with specific status
13. Assign a task to user - user send task_id and user_id and receive successful response after update task owner
14. Complete a task - user send task_id and receive successful response after update of task status in completed
15. Remove task - user send task_id and receive successful response after task deletion
16. Create a new "Comment" model in "tasks" app
17. Add comment to task - user send task_id, comment text and receive id of the new comment
18. View task comments - user send task id and receive list of all comments added to this task
19. Add email notification when task is assigned to me
20. Add email notification when my task is commented
21. Add email notification when commented task is completed
22. Search task by title - user send search term and receive list of tasks that match

### Milestone 3

Add these new functions to your task application to help users to track time spent on completion of each task.
User will start time when start working on task and stop it when complete the task or take a pause.

#### What will you learn

1. How to work with relational entities
2. How to create complex database queries (https://docs.djangoproject.com/en/4.2/topics/db/queries/)

#### Tasks

1. Start a timer for my task - user send task id and receive successful response after logging the start of task in DB
2. Stop timer for the started task - user send task id and receive successful response after adding a time log for this
   task with duration of work for current date
3. Add time log for a task on a specific date - user manually send in task id, date, duration in minutes and receive
   successful response of save
4. Get a list of time logs records by task - user send task id and receive list of all time logs created for this task
5. Change get list of tasks endpoint get receive the sum of the time in minutes for each task
6. Get the logged time in last month - user send a request and receive total amount of time logged by him in last month
7. Get top 20 tasks in last month by time - user send request and receive list of id, title, time amount of tasks with
   bigger logged amount of time

### Milestone 4

In this milestone we start to improve our application.

#### What will you learn

1. How to work increase quality of you app and identify bugs
2. How to install and switch project to PostgreSQL database and use pgHero
3. How to find out performance issues and improve response time of your endpoints with cache
4. How to work with Docker

#### Tasks

1. Add unit tests for each endpoint https://www.django-rest-framework.org/api-guide/testing/
2. Add coverage package and generate report to be sure in 100% test
   coverage https://docs.djangoproject.com/en/4.2/topics/testing/advanced/#integration-with-coverage-py
3. Install PostgreSQL docker container and move your app on PostgreSQL (edit settings.py)
4. Create a script that will add random 25.000 tasks and 50.000 time logs (
   use https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/)
5. Install PGHero docker container and connect it to your
   db https://github.com/ankane/pghero/blob/master/guides/Docker.md
6. Manual test all endpoints and check with PGHero that all sql queries use db indexes, after insert of thousands of
   tasks some endpoints can perform slow
7. Install Redis docker container and configure Django to cache with 1 minute TTL the endpoint with Top 20 tasks by time
   for each user https://github.com/jazzband/django-redis
8. Create Dockerfile for your application to run it with docker-compose command

### Milestone 5

In this milestone we will improve the application with new features and third-party services.

#### What will you learn

1. How to work with MinIO (S3 compatible storage)
2. How to work with celery and redis
3. How to work with django signals
4. How to use django templates
5. How to work with elastic search
6. How to integrate third-party authentication
7. How to setup github actions for CI/CD

#### Tasks

1. Use MinIO as static and media storage for your application https://pypi.org/project/django-minio-backend/
2. Create a new model "Attachment" with file field and task foreign key (use MinIO for storage)
3. Add attachment to task - user send task_id and file and receive successful response after adding attachment to task
4. Get list of attachments by task - user send task_id and receive list of all attachments added to this task
5. Send all email notifications with celery https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
6. Create celery beat task that will create a report with top 20 tasks by time for each user using Django templates and
   send it by email to each user one time per week
7. Create a signal handler that will create a new task in elastic search when task or comment is created or
   updated https://elasticsearch-dsl.readthedocs.io/en/latest/
8. Create endpoint that will search by choosing task field or comment in elastic
   search
9. Add third-party authentication with GitHub https://django-allauth.readthedocs.io/en/latest/
10. Add all this to your docker-compose file and test it
11. Create a github action that will run ruff lint and tests on each pull request https://github.com/features/actions

## Congratulations!

Congratulations on your job well done. We appreciate your dedication, and we look forward to seeing your career
flourish.

### Next steps

1. Think and design your own project, what startup would you like to build? Do it now!
2. With your mentor plan some tasks from real running projects
