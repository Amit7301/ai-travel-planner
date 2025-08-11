from django.db import models
from django.contrib.auth.models import User

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    days = models.IntegerField()
    budget = models.CharField(max_length=50, choices=[
        ('budget', 'Budget-friendly'),
        ('mid-range', 'Mid-range'),
        ('luxury', 'Luxury')
    ], default='mid-range')
    travel_style = models.CharField(max_length=50, choices=[
        ('adventure', 'Adventure'),
        ('cultural', 'Cultural'),
        ('relaxation', 'Relaxation'),
        ('family', 'Family-friendly'),
        ('business', 'Business')
    ], default='cultural')
    generated_itinerary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.source} to {self.destination} - {self.days} days"
