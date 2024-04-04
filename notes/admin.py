from django.contrib import admin

# Register your models here.
from .models import Article
from .models import Notes

admin.site.register(Article)
admin.site.register(Notes)