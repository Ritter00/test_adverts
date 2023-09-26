from django.apps import AppConfig
import os


class AdvertsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adverts'
    
    def ready(self):
        super().ready()
        if os.environ.get('TEST_MODE'):
            from .create import create_superuser, create_ad
            create_superuser()
            create_ad()
