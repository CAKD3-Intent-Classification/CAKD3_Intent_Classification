from typing import List
from django.db import models
from django.urls import reverse

# Create your models here.
class Theme(models.Model):
    theme_name = models.CharField('theme_name',max_length=250)

    map_img = models.ImageField(blank=False, upload_to='images',null=False)

    graph_img = models.ImageField(blank=False, null=False, upload_to='images')

    good = models.CharField('good_top3',max_length=250)

    bad = models.CharField('bad_top3',max_length=250)
    
    def __str__(self):
        return self.theme_name

    def get_absolute_url(self):
        return reverse('theme:theme_detail', kwargs={'pk':self.id})

    def good_list(self):
        return self.good.split(',')

    def bad_list(self):
        return self.bad.split(',')



class Place(models.Model):
    place_name = models.CharField('place_name',max_length=250)

    map_img = models.ForeignKey(Theme, on_delete=models.CASCADE)

    point = models.CharField('point',max_length=250)

    graph_img = models.ImageField(blank=False, null=False, upload_to = 'images')

    wordcloud_img = models.ImageField(blank=False, null=False, upload_to = 'images')

    solutions = models.CharField('solutions',max_length=250)

    def __str__(self):
        return self.place_name

    def get_absolute_url(self):
        return reverse('theme:place_detail', kwargs={'pk':self.id})

    def points(self):
        return self.point.split(',')

    def solution_list(self):
        return self.solutions.split(',')



