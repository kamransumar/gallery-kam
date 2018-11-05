from django.db import models
from django.db.models import Q
import datetime as dt

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()


class categories(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()


class Picture(models.Model):
    title = models.CharField(max_length=60)
    categories = models.ManyToManyField(categories)
    picture = models.ImageField(upload_to='pictures/')
    date_posted = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_picture(self):
        self.save()

    @classmethod
    def all_pictures(cls):
        pictures = cls.objects.all()
        return pictures

    @classmethod
    def search_by_category(cls, search_term):
        pictures = cls.objects.filter(Q(categories__category=search_term) | Q(
            title__icontains=search_term) | Q(location__location=search_term))

        return pictures
