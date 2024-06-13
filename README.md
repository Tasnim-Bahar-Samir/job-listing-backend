# Job Listing Project-API

## A Job listing project for candidates and companies. 

## Tech Stack

[![Django](https://img.shields.io/badge/web%20framework-django-black.svg?style=for-the-badge&logo=Django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Web%20browsable%20API-drf-802D2D.svg?style=for-the-badge&logo=drf)](https://www.django-rest-framework.org/)

[![API Documentation](https://img.shields.io/badge/API%20Documentation-swagger-298E35.svg?style=for-the-badge&logo=swagger)](https://swagger.io/)

[![Language](https://img.shields.io/badge/language-python-3773A4.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![PackageManager](https://img.shields.io/badge/package%20manager-pypi-FDDF76.svg?style=for-the-badge&logo=pypi)](https://pypi.org/)

[![License](https://img.shields.io/badge/license-Proprietary-F40D12.svg?style=for-the-badge&logo=adblock)](https://github.com/next-moov/next-moov-fe/blob/master/LICENSE)

## How to use

```sh
python -m venv venv
```

```sh
source venv/bin/activate
```
```sh
pip install -r requirements.txt
```

```sh
python manage.py migrate
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG`

`CORS_ALLOWED_ORIGINS`

### Database

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`


## Run Shell
To setup default data run this comand

```sh
python manage.py shell
```

```sh
exec(open('shell.py').read())
```

## Setup Social Auth

- Strp 1: Set site ID
![Screenshot](./_data/img/add_sites.png)
for example
1. localhost:3000

- Strp 2: Add Socialapp
![Screenshot](./_data/img/add_social_app.png)
You have to same perform for each social application

### Google
- Step 3: Configuration
The "Authorized redirect URIs" used when creating the credentials must include your full domain and end in the callback path.

For production example: 
1. https://{YOUR_DOMAIN}/api/auth/callback/google
2. https://{YOUR_DOMAIN}/api/calender/google

For development example: 
1. http://localhost:3000/api/auth/callback/google
2. http://localhost:3000/api/calender/google

For more details: https://next-auth.js.org/providers/google#configuration

### Facebook
- Step 3: Configuration
The "Authorized redirect URIs" used when creating the credentials must include your full domain and end in the callback path.
1. https://{YOUR_DOMAIN}/api/auth/callback/facebook

For more details: https://next-auth.js.org/providers/facebook

