from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Root URL -> Landing Page
    path('home/', views.home, name='home'),  # Home Pag
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('about/', views.about, name='about'), 
   path('book/', views.book, name='book'),
   path('dashboard/', views.dashboard, name='dashboard'),
   path('cancel/', views.cancel_appointment, name='cancel_appointment'),
  path('check_history/', views.check_history, name='check_history'),
 path('wellness-tips/', views.wellness_tips, name='wellness_tips'),
      path('mood-tracker/', views.mood_tracker, name='mood_tracker'),
]