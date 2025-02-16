from django.db import models
import random
import string
from django.utils.timezone import now


# Create your models here.

#this is a function to generate a random short code for the urls
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


#this is the database model for the shortened urls (stores device id, original url, short code, created at, click count, and last clicked)
class ShortenedURL(models.Model):
    device_id = models.CharField(max_length=100, null=True, blank=True)  
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)
    last_clicked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.original_url} -> {self.short_code}" #string representation of the model