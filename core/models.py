from distutils.command.upload import upload
from django.db import models
import uuid 

def upload_image_formater(instance, filename):
  return f"{str(uuid.uuid4())}-{filename}"

class Photo(models.Model):
  image = models.ImageField(upload_to=upload_image_formater, blank=True, null=True)