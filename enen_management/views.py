from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from enen_management.models import Event
from .forms import EventForm
from .models import participant,Catagory
from django.utils.timezone import now
from django.contrib.auth import authenticate, login, logout


def superuser_required(user):
    return user.is_superuser


def custom_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html') 

@login_required
@user_passes_test(superuser_required)
def home(request):
    return render(request,'home_page.html')

@login_required
@user_passes_test(superuser_required)

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})
@login_required
@user_passes_test(superuser_required)

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})
@login_required
@user_passes_test(superuser_required)

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
@login_required
@user_passes_test(superuser_required)

def delete_event(request,id):
    event = get_object_or_404(Event, id=id)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'delete_event.html', {'event': event})
@login_required
@user_passes_test(superuser_required)
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
@login_required
def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(superuser_required)
def category_list(request):
    categories = Catagory.objects.all()  
    return render(request, 'Category_list.html', {'categories': categories})
@login_required
@user_passes_test(superuser_required)
def participant_list(request):
    participants = participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})

# show the dashbord cilck list
@login_required
def total_event_view(request):
    total_event=Event.objects.all()
    return render(request,'total_event.html',{'total_event':total_event})
@login_required
def past_events_view(request):
    today = now().date()
    past_events = Event.objects.filter(date__lt=today) 
    return render(request, 'past_events.html', {'past_events': past_events})
@login_required
def upcoming_event_view(request):
   today=now().today()
   upcoming_event=Event.objects.filter(date__gte=today)
   return render(request,'upcoming_event.html',{'upcoming_event':upcoming_event})
@login_required
def participant_view(request):
    participants = participant.objects.all() 
    return render(request, 'participant.html', {'participants': participants})
