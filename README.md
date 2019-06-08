# dominos
A Django powered up application that helps people order pizza.

# Prerequisites

- [Docker](https://docs.docker.com/v17.12/install/)

# Initialize the project

Create a superuser to login to the admin:

```bash
docker-compose run --rm web ./manage.py createsuperuser
```

Start the dev server for local development:
```bash
docker-compose up
```

# Sample Data
In order to check apis with sample data, Run this (You still need to create a superuser to use admin panel):

```bash
docker-compose run --rm web ./manage.py loaddata sampledata.json

```

# Tests

To run tests:

```bash
docker-compose run --rm web ./manage.py test
```