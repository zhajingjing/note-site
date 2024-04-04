from django.db import models
from django.forms import ModelForm


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200,default='')
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=1000000)
    notes_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title


class Notes(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 0: notes by you  1: notes by AI
    type = models.IntegerField(default=0)
    reference_text = models.CharField(max_length=10000,default='',blank=True,null=True)
    notes_text = models.CharField(max_length=10000)
    create_user = models.CharField(max_length=20,default='')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notes_text
    
