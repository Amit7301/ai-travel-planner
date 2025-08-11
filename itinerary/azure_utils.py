"""
Utility functions for Azure OpenAI integration
"""
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def validate_azure_config():
    """
    Validate Azure OpenAI configuration
    """
    required_settings = [
        'AZURE_OPENAI_ENDPOINT',
        'AZURE_OPENAI_API_KEY', 
        'AZURE_OPENAI_DEPLOYMENT_NAME'
    ]
    
    missing_settings = []
    for setting in required_settings:
        if not hasattr(settings, setting) or not getattr(settings, setting):
            missing_settings.append(setting)
    
    if missing_settings:
        raise ValueError(f"Missing required Azure OpenAI settings: {', '.join(missing_settings)}")
    
    return True

def get_azure_openai_headers():
    """
    Get headers for Azure OpenAI API requests
    """
    return {
        "Content-Type": "application/json",
        # "api-key": settings.AZURE_OPENAI_API_KEY
        "Authorization": "Bearer "+settings.AZURE_OPENAI_API_KEY
    }

def get_azure_openai_url():
    """
    Construct Azure OpenAI API URL
    """
    endpoint = settings.AZURE_OPENAI_ENDPOINT.rstrip('/')
    deployment = settings.AZURE_OPENAI_DEPLOYMENT_NAME
    api_version = getattr(settings, 'AZURE_OPENAI_API_VERSION', '2024-02-01')
    
    return f"{endpoint}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
