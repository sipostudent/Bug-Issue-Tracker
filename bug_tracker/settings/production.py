import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Allowed Hosts
ALLOWED_HOSTS = [
    '127.0.0.1',
    'b-i-tracker.herokuapp.com',
]

# stripe keys
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

# postgres
DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
}