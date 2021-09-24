from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # company = models.CharField(max_length=200)
    # location = models.CharField(max_length=200)
    # user_bio = models.TextField()
    # bio_pic = models.URLField()
    # date_joined = models.DateField()
    # project_owner = models.BooleanField()

    def __str__(self):
        return self.username

# Create your models here.
