from django.db import models

# Create your models here.

class Image(models.Models):
    image_path = models.ImageField('images/',default="")
    image_name= models.CharField(max_length=50)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name
