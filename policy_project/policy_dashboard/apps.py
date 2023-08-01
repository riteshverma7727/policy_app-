# apps.py

from django.apps import AppConfig

class PolicyDashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'policy_dashboard'

    def ready(self):
        import policy_dashboard.signals  # Import the signals module

