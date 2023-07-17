# Django playground
This app was created just as example of:
- Serializer
- ModelViewSets
- Filters
- Complex ORM Querys


# How to setup the project
- Create docker image
```sh
docker-compose build
```

- Run docker image
```sh
docker-compose up
```

- Migrate database
```sh
docker exec -it django-reservations python manage.py makemigrations
docker exec -it django-reservations python manage.py migrate
```

- Create superuser (for admin login)

# Play with the API
- Go to:
```
http://127.0.0.1:8000/docs/
```

# Admin
Default user created:
```
root
12345
```

# Test
```sh
docker exec -it django-reservations python manage.py test
```

## Thanks!
Feel free to contact me by mail _hernan4790@gmail.com_ for any doubt.\
Enjoy :smile:!!