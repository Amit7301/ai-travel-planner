import requests
import json
from django.conf import settings
from .azure_utils import get_azure_openai_headers, get_azure_openai_url
import logging

logger = logging.getLogger(__name__)

class ItineraryGenerator:
    def __init__(self):
        self.url = get_azure_openai_url()
        self.headers = get_azure_openai_headers()
    
    def generate_itinerary(self, source, destination, days, budget, travel_style):
        prompt = f"""
        Create a detailed {days}-day travel itinerary from {source} to {destination}.
        
        Travel preferences:
        - Budget: {budget}
        - Travel style: {travel_style}
        - Duration: {days} days
        
        Please include:
        1. Day-by-day breakdown with specific activities
        2. Recommended accommodations
        3. Transportation suggestions
        4. Must-visit attractions
        5. Local food recommendations
        6. Estimated costs for major expenses
        7. Travel tips and important notes
        
        Format the response in a clear, organized manner with proper headings and bullet points.
        """
        
        data = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a professional travel planner with extensive knowledge of destinations worldwide. Provide detailed, practical, and engaging travel itineraries."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": 2000,
            "temperature": 0.2,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }
        
        try:
            logger.info(f"Generating itinerary for {source} to {destination}")
            response = requests.post(self.url, headers=self.headers, json=data, timeout=60)
            
            # Log response status for debugging
            logger.info(f"Azure OpenAI API response status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                if 'choices' in result and len(result['choices']) > 0:
                    content = result['choices'][0]['message']['content']
                    logger.info("Successfully generated itinerary")
                    return content
                else:
                    logger.error("No choices in API response")
                    return "Sorry, there was an error generating your itinerary. Please try again."
            
            elif response.status_code == 401:
                logger.error("Authentication failed - check your API key")
                return "Authentication error. Please check your Azure OpenAI configuration."
            
            elif response.status_code == 404:
                logger.error("Deployment not found - check your deployment name")
                return "Deployment not found. Please check your Azure OpenAI deployment name."
            
            elif response.status_code == 429:
                logger.error("Rate limit exceeded")
                return "Service is currently busy. Please try again in a few moments."
            
            else:
                logger.error(f"API request failed with status {response.status_code}: {response.text}")
                return f"Sorry, there was an error (Status: {response.status_code}). Please try again."
                
        except requests.exceptions.Timeout:
            logger.error("Request timeout")
            return "The request timed out. Please try again."
            
        except requests.exceptions.ConnectionError:
            logger.error("Connection error")
            return "Unable to connect to the service. Please check your internet connection."
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            return "There was an error processing the response. Please try again."
            
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return f"An unexpected error occurred: {str(e)}"