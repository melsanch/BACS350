from django.contrib import admin

from .models import Article, Superhero

admin.site.register(Superhero)
admin.site.register(Article)
# Register your models here.
