from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default="Unknown")
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    is_cancelled = models.BooleanField(default=False) 
    status = models.CharField(max_length=20, default="booked") 


    def __str__(self):
        return f"{self.full_name} - {self.date} at {self.time}"

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=20)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.mood}"
    
    from django.db import models
from django.contrib.auth.models import User

class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=20)  # Mood can be "Happy", "Sad", etc.
    note = models.TextField(blank=True)  # Optional note field for extra details
    date = models.DateField(auto_now_add=True)  # Auto-fill the current date

    def __str__(self):
        return f"{self.user.username} - {self.mood} on {self.date}"
