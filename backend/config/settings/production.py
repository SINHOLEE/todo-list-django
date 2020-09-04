from config.util import get_server_info_value
from .base import *

SETTING_PRD_DIC = get_server_info_value("production")
SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]

DEBUG = True

ALLOWED_HOSTS = [
            SETTING_PRD_DIC['DATABASES']["default"]["HOST"],
            'localhost',
            '127.0.0.1',
            '0.0.0.0',

            ]

DATABASES = {
    'default': SETTING_PRD_DIC['DATABASES']["default"]
}

