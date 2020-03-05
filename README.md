# mestagram
A django based web application allowing users to view my pictures.

## Features

- Django 2.0+
- Uses [Pipenv](https://github.com/kennethreitz/pipenv) - the officially recommended Python packaging tool from Python.org.
- Development, Staging and Production settings with [django-configurations](https://django-configurations.readthedocs.org).
- Get value insight and debug information while on Development with [django-debug-toolbar](https://django-debug-toolbar.readthedocs.org).
- Collection of custom extensions with [django-extensions](http://django-extensions.readthedocs.org).
- HTTPS and other security related settings on Staging and Production.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.

## Environment Variables
```SECRET_KEY=XXX
DEBUG=True
DB_NAME='mestagram'
DB_USER='don'
DB_PASSWORD='XXXX
DB_HOST='127.0.0.1'
MODE='prod'
ALLOWED_HOSTS='.localhost','.herokuapp.com','.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

## Deployment

It is possible to deploy to Heroku or to your own server.

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=os.config('SECRET_KEY')
```

## Built With

* [Django](https://docs.djangoproject.com/en/3.0/) - The web framework used
* [Pipenv](https://github.com/pypa/pipenv) - Dependency Management

## Versioning

We use [Git](https://git-scm.com/) for versioning. 

## Codebeat Grade

[![codebeat badge](https://codebeat.co/badges/f8107475-d62a-4d5c-b2cb-9c601ce9c48a)](https://codebeat.co/projects/github-com-d0nmoses-mestagram-master)

## Authors

* *Don Moses** - *Initial work* 

## License

The MIT License (MIT)

Copyright (c) 2020 Don Moses

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Acknowledgments

* Lawrence Karanja
* Ashley Zawadi

## PS

For search functionality, created categories are safari, home, house, beach
