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
        
 class Category(models.Model):
     category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        Category.objects.filter().delete()
