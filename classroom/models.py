from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=200, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username
