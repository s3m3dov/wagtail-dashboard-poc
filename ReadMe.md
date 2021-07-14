# Test: Analytics Dashboard #

## Python/Django Installation & Set-up ##

Clone Repo
```
git clone https://github.com/s3m3dov/test_prj_ad_wagtail.git
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

* website url: https://test-wagtail-ga-chartjs.herokuapp.com/
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
