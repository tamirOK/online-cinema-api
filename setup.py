from setuptools import setup, find_packages

setup(
    name="Online cinema",
    version="0.1.0",
    author="Tamirlan Omarov",
    author_email="tamirok@protonmail.com",
    packages=find_packages(),
    license="LICENSE.txt",
    description="REST API for online cinema of tv series/soap operas",
    long_description=open("README.txt").read(),
    install_requires=[
        "atomicwrites==1.1.5",
        "attrs==18.1.0",
        "Django==2.0.5",
        "django-debug-toolbar==1.9.1",
        "django-environ==0.4.4",
        "django-extensions==2.0.7",
        "djangorestframework==3.8.2",
        "mimesis==2.0.1",
        "more-itertools==4.1.0",
        "pkg-resources==0.0.0",
        "pluggy==0.6.0",
        "psycopg2==2.7.4",
        "py==1.5.3",
        "pytest==3.6.0",
        "pytest-django==3.2.1",
        "pytz==2018.4",
        "six==1.11.0",
        "sqlparse==0.2.4",
        "Werkzeug==0.14.1",
    ],
    package_data={
        "cinema": ["*.ini"]
    }
)