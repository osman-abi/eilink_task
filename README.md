# eilink_task
# postman collection link >>> https://www.postman.com/collections/e08210b72dcb4bdb1149

In this projects I use Django, Django REST Framework, JWT Authentication , logging, celery tasks, pylint for upgrade code quality, Django MPTT models for creating hierarchical structure and Black methodoly for formatting .py files.

Follow sequences as below for running in local (./core folder):
1) python3 -m venv venv
2) source venv/bin/activate
3) pip install -r requirements.txt
4) Change DEBUG to True in settings.py file
5) python manage.py runserver

# if you wanna check celery tasks you must have redis server in your local machine. 
Follow sequences as below:
1) celery -A core beat -l INFO
2) celery -A core worker -l INFO

I use AWS EC2 server for deployment via Dockerfile, docker-compose.yml, nginx
# link >>> http://3.70.24.182/
