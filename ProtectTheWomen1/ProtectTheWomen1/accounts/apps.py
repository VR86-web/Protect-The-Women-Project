from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProtectTheWomen1.accounts'

    def ready(self):
        import ProtectTheWomen1.accounts.signals
