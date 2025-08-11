from django.apps import AppConfig

class ItineraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'itinerary'
    
    def ready(self):
        # Validate Azure OpenAI configuration on startup
        try:
            from .azure_utils import validate_azure_config
            validate_azure_config()
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"Azure OpenAI configuration validation failed: {e}")
