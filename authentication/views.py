from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Appointment
from django.contrib import messages
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse


# Landing page
def landing(request):
    return render(request, "authentication/landingpage.html")

# Home page
def home(request):
    if request.user.is_authenticated:
        fname = request.user.first_name
        return render(request, "authentication/index.html", {'fname': fname})
    return redirect('signin')

# Signup page
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Try another one.")
            return redirect('signup')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters.")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('signup')

        myuser = User.objects.create_user(username=username, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been created successfully.")
        return redirect('signin')

    return render(request, "authentication/signup.html")

# Signin page
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, f"Welcome back, {fname}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('signin')

    return render(request, "authentication/signin.html")

# Signout page
def signout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('landing')


# About page
def about(request):
    return render(request, "authentication/about.html")

from django.shortcuts import render
from django.http import HttpResponse

# Simple view for booking an appointment

def book(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        date = request.POST.get("date")
        time = request.POST.get("time")
        notes = request.POST.get("notes")

        # Save appointment to the database
        Appointment.objects.create(
            user=request.user,
            full_name=full_name,
            date=date,
            time=time,
            notes=notes
        )

        # Show success message and redirect to dashboard
        messages.success(request, "Appointment successfully booked!")
        return redirect("book")  # Make sure 'dashboard' is the correct URL name in urls.py

    return render(request, "book.html")
from .models import Appointment  # Make sure this is at the top
from django.contrib import messages

from django.shortcuts import render
from .models import Appointment
from django.utils.timezone import now

def dashboard(request):
    # Fetch the user's upcoming appointment (future appointments only)
    upcoming_appointment = Appointment.objects.filter(user=request.user, date__gte=now().date()).order_by('date', 'time').first()

    # Fetch past appointments (appointments that have already happened)
    past_appointments = Appointment.objects.filter(user=request.user, date__lt=now().date()).order_by('-date', '-time')

    return render(request, "dashboard.html", {
        "upcoming_appointment": upcoming_appointment,
        "past_appointments": past_appointments
    })
def cancel_appointment(request):
    if request.method == "POST":
        appointment_id = request.POST.get("appointment_id")
        try:
            appointment = Appointment.objects.get(id=appointment_id, user=request.user)
            appointment.delete()
            messages.success(request, "Appointment cancelled successfully.")
        except Appointment.DoesNotExist:
            messages.error(request, "Appointment not found or unauthorized.")

        return HttpResponseRedirect(reverse('cancel_appointment'))

    appointments = Appointment.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, "cancel_appointment.html", {"appointments": appointments})
# Check appointment history
def check_history(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'check_history.html', {'appointments': appointments})

# views.py
def wellness_tips(request):
    user = request.user
    return render(request, 'wellness_tips.html', {'username': user.first_name})

from django.shortcuts import render, redirect
from .models import MoodEntry
from django.contrib.auth.decorators import login_required

@login_required
def mood_tracker(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        note = request.POST.get('note')
        # Create and save the mood entry to the database
        MoodEntry.objects.create(user=request.user, mood=mood, note=note)

    # Fetch all mood entries for the logged-in user
    mood_entries = MoodEntry.objects.filter(user=request.user)

    return render(request, 'mood_tracker.html', {'mood_entries': mood_entries})
