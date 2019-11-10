# Demands Automotive Parts #

## Objectives ##

###### CRUD of demands of automotive parts

## Setting Up Environment ##

### Development ###

#### Download and install docker-ce ####

* Linux: https://www.digitalocean.com/community/tutorials/como-instalar-e-usar-o-docker-no-ubuntu-16-04-pt

#### Download and install docker-compose ####

https://docs.docker.com/compose/install/#install-compose

#### Setting Up Database Connection ####

If needed, open `demandsProject/settings.py` and change environment variables.

### Test the endpoints

The endpoints can be tested with a Collection of Postman inside the project,
search for: `finxi-django.postman_collection.json`

##### If you will test the endpoints, primary create an `User`,
 after that, associate an `User Detail` to an `User` and finishing create a `Demand`

#### Composing up! ####

In your application directory, run:

```bash
docker-compose up -d
```

#### Composing down :( ####

To shut down the application, enter your application directory and run:

```bash
docker-compose down
```
