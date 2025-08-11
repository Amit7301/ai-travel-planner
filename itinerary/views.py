from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ItineraryForm
from .models import Itinerary
from .services import ItineraryGenerator

def home(request):
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            itinerary = form.save(commit=False)
            if request.user.is_authenticated:
                itinerary.user = request.user
            
            # Generate itinerary using OpenAI
            generator = ItineraryGenerator()
            generated_content = generator.generate_itinerary(
                itinerary.source,
                itinerary.destination,
                itinerary.days,
                itinerary.budget,
                itinerary.travel_style
            )
            
            itinerary.generated_itinerary = generated_content
            itinerary.save()
            
            messages.success(request, 'Your itinerary has been generated successfully!')
            return redirect('itinerary_detail', pk=itinerary.pk)
    else:
        form = ItineraryForm()
    
    # Show recent itineraries
    recent_itineraries = Itinerary.objects.all().order_by('-created_at')[:6]
    
    return render(request, 'itinerary/home.html', {
        'form': form,
        'recent_itineraries': recent_itineraries
    })

def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk)
    return render(request, 'itinerary/detail.html', {'itinerary': itinerary})

@login_required
def my_itineraries(request):
    itineraries = Itinerary.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(itineraries, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'itinerary/my_itineraries.html', {'page_obj': page_obj})

def all_itineraries(request):
    itineraries = Itinerary.objects.all().order_by('-created_at')
    paginator = Paginator(itineraries, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'itinerary/all_itineraries.html', {'page_obj': page_obj})
