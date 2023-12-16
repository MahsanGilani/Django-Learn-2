from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # author = 
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    # like = 
    
    def __str__(self) -> str:
        return self.title
    
    def cap_first(self):
        return self.content.capitalize()