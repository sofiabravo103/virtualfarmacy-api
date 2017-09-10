# virtualfarmacy-api
API to query classified Venezuelan prescription drug tweets

## Setup

### Dependencies

Install requirements with pip: 

`$pip install -r requirements.txt`

### Environ
Create a file called `.env` inside `config/` and add the following lines:

```
DATABASE_URL=postgres://username:password@localhost:5432/db_name
DJANGO_SECRET_KEY=add_your_secret_key_here
```

Replace username, password and db_name with your postgres info, generate a secret key and add it replacing `add_your_secret_key_here`. [Here](http://www.miniwebtool.com/django-secret-key-generator/) is a link to generate secret keys for django.

### Tests

To run all tests use pytest:

`$ pytest`
