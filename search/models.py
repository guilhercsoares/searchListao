from django.db import models

# Create your models here.
class Name(models.Model):
	name_text = models.CharField(max_length=256)
