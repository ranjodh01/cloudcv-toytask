from django.db import models
from django.db.models import ImageField, signals
# Create your models here.

class Image(models.Model):
	image = models.ImageField("Select an Image", upload_to='photos')
	ques = models.CharField("Question?", max_length=30)