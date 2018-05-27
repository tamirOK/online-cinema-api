from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Episode(models.Model):
    episode_number = models.PositiveIntegerField()
    name = models.CharField(max_length=500, blank=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, related_name="episodes")
    description = models.CharField(max_length=200, blank=True)
    released_date = models.DateField()

    def __str__(self):
        return "Episode {} of the {} show".format(self.name, self.season.show.name)

    class Meta:
        unique_together = ("episode_number", "season")


class Season(models.Model):
    season_number = models.PositiveIntegerField()
    description = models.CharField(max_length=500, blank=True)
    show = models.ForeignKey('Show', on_delete=models.CASCADE, related_name="seasons")

    def __str__(self):
        return "Season {} of the {} show".format(self.season_number, self.show)

    class Meta:
        unique_together = ("season_number", "show")


class Show(models.Model):
    name = models.CharField(max_length=100)
    released_date = models.DateField()
    directors = models.ManyToManyField("Person", related_name="directed_shows")
    actors = models.ManyToManyField("Person", related_name="acted_shows")
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Person(AbstractUser):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    birth_date = models.DateField(null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    country = models.CharField(max_length=100, blank=True)
