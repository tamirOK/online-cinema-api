=============
Online cinema
=============

Online cinema is a test task for a company.

There are 4 entities in the system: Episode, Season, Show and Person(actor or show director). The service provides REST-API and supports CRUD for each of the entity.

Installation and Usage
======================

Follow these instructions:

* pip install cinema

* Create Postgresql database, user and put the credentials into .env file in the following format::

    DATABASE_URL=postgres://dbuser:password@dbhost:port/dbname

  .env file should be located in the project root
* Run the command to populate the created database::

    python manage.py populate_db

* Run project::

    python manage.py runserver_plus

