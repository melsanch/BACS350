from django.db import models
from django.urls.base import reverse_lazy

class Superhero(models.Model):
    name = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    description = models.TextField()
    strength = models.CharField(max_length=100)
    weakness = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse_lazy('hero_detail', args=[str(self.id)])

class Article(models.Model):
    Hero = models.CharField(max_length=200)
    order = models.IntegerField()
    title = models.CharField(max_length=200)
    markdown = models.TextField()
    html = models.TextField()

    def export_record(self):
        return [self.Hero, self.order, self.title]

    def import_record(values):
        c = Article.objects.get_or_create(Hero=values[0], order=values[1])[0]
        c.title = values[2]
        c.save()
    
    def __str__(self):
        return f'{self.Hero.title} - {self.order} - {self.title}'
# Create your models here.
