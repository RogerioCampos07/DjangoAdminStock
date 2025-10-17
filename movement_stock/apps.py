from django.apps import AppConfig


class MovementStockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movement_stock'

    def ready(self):  # noqa: PLR6301
        import movement_stock.signals  # noqa F401
