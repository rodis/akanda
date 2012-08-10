from django.conf import settings


AKANDA_APPS = (
    'akanda.horizon.akanda',
)


INSTALLED_APPS = settings.INSTALLED_APPS + AKANDA_APPS
