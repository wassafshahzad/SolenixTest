from django.apps import AppConfig


class LocationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'location'

    def ready(self) -> None:
        import location.signals
        return super().ready()