from django.db import models
from PIL import Image
import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
class Student(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Phone=models.BigIntegerField()
    Password=models.CharField(max_length=50,default="",)


class UploadedImage(models.Model):
    imagekey=models.ForeignKey(Student,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    caption=models.TextField(max_length="20",default="Wow")

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            output_buffer = BytesIO()
            img.save(output_buffer, format='WEBP', quality=70)
            self.image = InMemoryUploadedFile(output_buffer, 'ImageField', f"{self.image.name.split('.')[0]}.webp", 'image/webp', sys.getsizeof(output_buffer), None)
        super().save(*args, **kwargs)
