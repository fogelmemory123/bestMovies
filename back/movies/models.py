from django.db import models

class Movie(models.Model):
    poster = models.ImageField(upload_to='posters/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    director = models.CharField(max_length=100)
    main_actors = models.CharField(max_length=200, help_text="הפרד את שמות השחקנים בפסיקים")
    year_of_release = models.PositiveIntegerField()

    def __str__(self):
        return self.title