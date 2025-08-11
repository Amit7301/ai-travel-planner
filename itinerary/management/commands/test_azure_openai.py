"""
Management command to test Azure OpenAI connection
Usage: python manage.py test_azure_openai
"""
from django.core.management.base import BaseCommand
from django.conf import settings
import requests
import json
from itinerary.azure_utils import get_azure_openai_headers, get_azure_openai_url

class Command(BaseCommand):
    help = 'Test Azure OpenAI API connection'

    def handle(self, *args, **options):
        try:
            # Validate configuration
            required_vars = [
                'AZURE_OPENAI_ENDPOINT',
                'AZURE_OPENAI_API_KEY',
                'AZURE_OPENAI_DEPLOYMENT_NAME'
            ]
            
            missing_vars = []
            for var in required_vars:
                if not hasattr(settings, var) or not getattr(settings, var):
                    missing_vars.append(var)
            
            if missing_vars:
                self.stdout.write(
                    self.style.ERROR(f'Missing environment variables: {", ".join(missing_vars)}')
                )
                return
            
            # Test API connection
            url = f"{settings.AZURE_OPENAI_ENDPOINT}/openai/deployments/{settings.AZURE_OPENAI_DEPLOYMENT_NAME}/chat/completions?api-version={getattr(settings, 'AZURE_OPENAI_API_VERSION', '2024-02-01')}"
            
            headers = {
                "Content-Type": "application/json",
                "api-key": settings.AZURE_OPENAI_API_KEY
            }

            
            data = {
                "messages": [
                    {"role": "user", "content": "Hello, this is a test message."}
                ],
                "max_tokens": 10
            }
            
            self.stdout.write('Testing Azure OpenAI connection...')
            response = requests.post(url, headers=headers, json=data, timeout=30)
            
            if response.status_code == 200:
                self.stdout.write(
                    self.style.SUCCESS('✓ Azure OpenAI connection successful!')
                )
                result = response.json()
                if 'choices' in result:
                    self.stdout.write(f"Response: {result['choices'][0]['message']['content']}")
            else:
                self.stdout.write(
                    self.style.ERROR(f'✗ Connection failed with status {response.status_code}')
                )
                self.stdout.write(f'Response: {response.text}')
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'✗ Error testing connection: {str(e)}')
            )
