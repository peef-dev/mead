# Mead

# !!! WORK IN PROGRESS !!!

Mead is a Flask boilerplate for common web development projects with:

- Simple and extensible structure
- PostgreSQL support
- Docker support
- pre-commit support for code quality
- Basic users authentication

# How to run the application ?

First of all, note that the variables **<APP_CONTAINER_NAME>** and **<DB_CONTAINER_NAME>** should be set in your **.env** file.
An example is given in **dot.env.example** file.

### To build the image

```
docker-compose up --build
```

### To run the image

```
docker-compose up
```

### To go inside the containers

```
docker exec -it <APP_CONTAINER_NAME> bash

docker exec -it <DB_CONTAINER_NAME> psql -U admin
```

### To initialize or migrate database, go inside your <APP_CONTAINER_NAME> container and execute

```
./dev/db_init.sh

./dev/db_migrate.sh
```
