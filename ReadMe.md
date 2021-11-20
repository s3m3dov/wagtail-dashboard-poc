# Test: Analytics Dashboard #

## Python/Django Installation & Set-up ##

Clone Repo
```
git clone https://github.com/s3m3dov/poc-ad-wagtail.git
```

then
```
virtualenv .env
```
```
source .env/bin/activate
```

or
```
py -m venv env
```
```
env\Scripts\activate
```

then
```
pip install -r requirements.txt
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
python manage.py runserver
```

## Other Things To Consider ##

### Credentials for Hosted Website ###

* website url: http://178.128.32.114/
* username: home
* password: djangoapp

### Application Architecture & Urls ###
> Main Ones
* apps.analytics
* apps.dashboard - "/dashboard"
> Others
* apps.home - "/"
* apps.search - "/search"

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
