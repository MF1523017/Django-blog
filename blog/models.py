from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class BlogPost(models.Model):
	title=models.CharField(max_length=150)
	body=models.TextField()
	timestamp=models.DateTimeField()
	class Meta:
		ordering=('-timestamp',)

class BlogPostForm(forms.ModelForm):
	#title=forms.ChoiceField(choices=[('1','1'),('2','2')])
	class Meta:
		model=BlogPost
		exclude=('timestamp',)
