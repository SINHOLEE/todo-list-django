from .base import *

DEBUG = True

SECRET_KEY = '&=l50oh@g=ol0d%y^rzyldggv^(ehspz!o*32u_qg&&%dfyxde'


ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
