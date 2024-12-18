from django.apps import AppConfig


class JKH_siteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'JKH_site'

    def ready(self):
        import JKH_site.signals
