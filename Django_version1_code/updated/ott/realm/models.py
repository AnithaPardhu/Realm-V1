from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
import uuid

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profiles', null=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
    child_profile = models.BooleanField(default=False)
    pin = models.CharField(max_length=10, blank=True, null=True)
    

    def __str__(self):
        return self.name





from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile_number = models.CharField(max_length=20)
    
    # Field to store session keys
   

    def __str__(self):
        return self.username




def video_upload_path(instance, filename):
    return f"videos/{filename}"


from django.db import models
from django import forms

class Genres(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('movies', 'Movies'),
        ('tv_shows', 'TV Shows'),
        ('documentaries', 'Documentaries'),
        ('others', 'Others'),
    ]
    GENRES_CHOICES = [
        ('1', 'Crime'),
        ('2', 'Thriller'),
        ('3', 'Romantic'),
        ('4', 'Horror'),
        ('5', 'Drama'),
        ('6', 'Romantic Comedy'),
        ('7', 'Science Fiction'),
        ('8', 'Action'),
        # Add more genre choices here
    ]
    CONTENT_AGE_RATINGS = [
        ('18+', '18+'),
        ('13+', '13+'),
        ('7+', '7+'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    scheduled_time = models.DateTimeField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES)
    genres = models.ForeignKey(Genres, on_delete=models.CASCADE)
    content_age_rating = models.CharField(max_length=255, choices=CONTENT_AGE_RATINGS)
    def __str__(self):
        return self.title
    
import pytz
from django.utils import timezone

    
class Notification(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_ist_timestamp(self):
        ist_timezone = pytz.timezone("Asia/Kolkata")
        return self.timestamp.astimezone(ist_timezone)

    def __str__(self):
        return f"{self.video.title} Notification"





from django.conf import settings
from django.db import models

class Watchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)  # Using string 'Video' here
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)  # Using string 'Profile' here
    

# models.py

from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

class SelectedProfile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=255)

    def __str__(self):
        return self.profile_name
    


class ProfileWatchlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=255)  # Add this line for the profile name

    def save(self, *args, **kwargs):
        # Automatically populate the profile_name field when saving
        self.profile_name = self.profile.name
        super().save(*args, **kwargs)


from django.contrib.auth.models import User

from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Other user-related fields
    # ...


class RealmProfile(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    pin = models.CharField(max_length=4)
    # Other profile-related fields
    # ...


from django.conf import settings
from django.db import models

class UniqueToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=16)

    def __str__(self):
        return self.token


class Restrict(models.Model):
    profile_name = models.CharField(max_length=255)
    user_id = models.IntegerField()
    movie_title = models.CharField(max_length=255)

    def __str__(self):
        return self.profile_name


# models.py
from django.db import models
from django.contrib.auth.models import User

class ProfileGenreSelection(models.Model):
    profile_name = models.CharField(max_length=100)  # Store the profile name
    user_id = models.CharField(max_length=100)
    genre = models.ForeignKey('Genres', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile_name} - {self.user_id} - {self.genre}'
    

from django.conf import settings

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.user.username} - ${self.amount}'

