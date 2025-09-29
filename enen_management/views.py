from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from enen_management.models import Event
from .forms import EventForm
from .models import participant,Catagory
from django.utils.timezone import now
def home(request):
    return render(request,'home_page.html')

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def update_event(request,id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'update_event.html', {'form': form})

def delete_event(request,id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'delete_event.html', {'event': event})
def Dashboard(request):
    today=now().date()
    total_events=Event.objects.count()
    upcoming_events=Event.objects.filter(date__gte=today).count()
    past_events=Event.objects.filter(date__lt=today).count()
    total_participants=participant.objects.count()
    todays_events=Event.objects.filter(date=today).prefetch_related('participants')

    context = {
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'total_participants': total_participants,
        'todays_events': todays_events
    }
    
    return render(request, 'Dashboard.html', context)
def category_list(request):
    categories = Catagory.objects.all()  
    return render(request, 'Category_list.html', {'categories': categories})
def participant_list(request):
    participants = participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})
