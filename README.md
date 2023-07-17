# Django playground
This app was created just as example of:
- Serializer
- ModelViewSets
- Filters
- Complex ORM Querys

# TODO
- Create filters with DjangoFiltersBackend in the viewset
- Create some rules in the serializer to avoid creating rules with fixed_price or price_modifier without mandatory fields
- Create tests for the viewset
- Use Django 4.0 async properties to improve performance in the
    calculate_final_price method (invoce async each day calculation)
- Documentation and type hints in the code


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
docker exec -it django-south python manage.py makemigrations
docker exec -it django-south python manage.py migrate
```

- Create superuser (for admin login)

# Play with the API
- Go to:
```
http://127.0.0.1:8000/docs/
```

Enjoy!