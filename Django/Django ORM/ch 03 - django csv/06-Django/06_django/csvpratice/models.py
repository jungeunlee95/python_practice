from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    audience = models.IntegerField()
    genre = models.TextField()
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    
    def __repr__(self):
        return f"<{self.title} : {self.genre}>"
    
    def __str__(self):
        return f"<{self.title} : {self.genre}>"