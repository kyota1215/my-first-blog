from django.db import models
from django.conf import settings
from django.utils import timezone 

# Create your models here.
class User(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


class Post(models.Model):
    
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_data = models.DateTimeField(default = timezone.now)
    published_data = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title 
    

