from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    
    def get_user_by_email(email: str):
        return User.objects.get(email=email)