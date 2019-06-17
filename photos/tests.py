from django.test import TestCase
from .models import Image

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        self.nairobi = Location(location='Nairobi')
        self.nairobi.save_location()

        self.landscape = Category(category='Nature')
        self.landscape.save_category()

        self.new_image = Image(image_name='Test Name',image_description='Test Description',image_location=self.nairobi,image_category=self.landscape)
        self.new_image.save_image()

        def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        self.new_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_filter_by_location(self):
        filtered_images = Image.filter_by_location('Nairobi')
        self.assertTrue(len(filtered_images)>0)

    def test_search_image(self):
        image = Image.search_by_category('Nature')
        self.assertTrue(len(image)>0)

    def test_get_image_by_id(self):
        images = Image.get_image_by_id(self.new_image.id)
        self.assertTrue(images == self.new_image)

    def test_delete_image(self):

        images = Image.get_image_by_id(self.new_image.id)
        self.new_image.delete_image()
        self.assertTrue(len(images)==0)
