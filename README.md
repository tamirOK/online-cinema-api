# online-cinema-api
There are 4 entities in the system: Episode, Season, Show and Person(actor or show director). The service provides REST-API and supports CRUD for each of the entity.

Show directors can update and delete show, its seasons and episodes. Persons can update information about themselves. Admin can CRUD on all entities.  

## Installation and Usage

* Install requirements:
  ```pip install -r requirements.txt``` or ```python setup.py install```

* Create Postgresql database, user and put the credentials into .env file in the following format:
    
    ```DATABASE_URL=postgres://dbuser:password@dbhost:port/dbname```

  .env file should be located in the project root (where manage.py file is located)
* Run the commands to apply migrations and  populate the created database:

    ```python manage.py migrate```
    
    ```python manage.py populate_db```

* Run project

    ```python manage.py runserver_plus```
