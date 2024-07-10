# Orders

This is system to monitor and manage daily user orders.

It is assumed that on the machine where you want to run this application, 
there is installed docker.

We assume that for launching all scripts(docker and test), we are in the main root of the project

## Authors

- [@jsotamba](https://github.com/jsotamba)

## Running Tests

To run unit tests, run the following command

```bash
  python manage.py test # all tests
  python manage.py test apps.order # only order app tests
  python manage.py test apps.product # only product app tests
```

## Run project

To run this project 

```bash
  docker-compose up --build
```

## API Reference

#### Swagger

```http
  GET /swagger/
```

#### Docs

```http
  GET /redoc/
```

