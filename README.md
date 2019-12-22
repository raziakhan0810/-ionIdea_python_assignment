# SETUP TO RUN PROJECTS
### make sure you have already below list in your system:
- python 3.7
- postgresSQL (database)

1) Clone project from github/bitbucket repository,
2) Create virtualenv and activate virtualenv
3) Install all packages from requirements.txt file
```
pip install -r requirements.txt
```
4) setup database:
​        a)
​        - create user with password
​        - create database with above user
​        - grant all permission to it.
​	```
​	create user <user_name> with password '<password>';
​	create database <db_name> with owner <user_name>;
​	grant all privileges on database <db_name> to <user_name>;
​	```
​        
​        b)
​         - create local.py file from settings
​	```
​	inside ionIdea_python_test folder settings i.e ionIdea_python_test/settings
​	```
​         - add database in local.py
​	```
​	import os
​    DEBUG = True
​    DATABASES = {
​        'default': {
​            'ENGINE': 'django.db.backends.postgresql_psycopg2',
​            'NAME': os.environ.get('DB_NAME', ''),
​            'HOST': os.environ.get('DB_HOST', ''),
​            'USER': os.environ.get('DB_USER', ''),
​            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
​            'PORT': os.environ.get('DB_PORT', '5432')
​        }
​    }
​	```

5) run migrate 
```
./manage.py migrate
```
6) create token for API:
​        - create super user from terminal
​        - login from admin
​        - create token
7) run project
```
./manage.py runserver
```
```
API for POST employee_hire :
​    - endpoint: '/employee_hire/' 
​    - body: {
​                "birth_date": "08/10/1990",
​                "employee_id": 1,
​                "first_name": "Test1",
​                "last_name": "test1",
​                "gender": "F",
​                "hire_date": "22/12/2018",
​                "salary": 50000,
​                "department": "Finance",
​                "title": "Assistant Engineer"
​            }
​     - header: {
​                "Authorization": "Token <created_token>"
​              }

API for GET eligible_for_hike :
​    - endpoint: '/eligible_for_hike/' 
​    - params: {
​                "employee_id": 1
​            }
​    - header: {
​                "Authorization": "Token <created_token>"
​              }
​          
```