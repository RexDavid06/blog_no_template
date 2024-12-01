from django.apps import AppConfig


class BlogmeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogmeapp'


    def ready(self):
        import blogmeapp.signals
