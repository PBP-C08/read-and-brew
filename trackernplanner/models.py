from django.db import models
from booklist.models import Buku
from django.contrib.auth.models import User

# Tracker model for Guest
class BookTracker(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
    )

    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    page = models.PositiveIntegerField()
    progress = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    tracked_at = models.DateTimeField(auto_now_add=True)

# Tracker model for Member
class BookTrackerMember(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    page = models.PositiveIntegerField()
    progress = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')