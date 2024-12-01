from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title}  {self.date_posted}"
    
    class Meta:
        ordering = ['-date_posted']



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='profiles')


    def __str__(self):
        return f"{self.user}  {self.image}"