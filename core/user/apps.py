from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.user'

    def ready(self) -> None:
        import core.user.signals.code_verification
