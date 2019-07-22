from django.test import TestCase
from .models import Location, Category, Image


# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Paris')
        self.location.save()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        Location.objects.all().delete()
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        new_location_name = 'India'
        self.location.update_location(self.location.id, new_location_name)
        updated_location = Location.objects.filter(location_name='India')
        self.assertTrue(len(updated_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


# class CategoryTestClass(TestCase):
#     def setUp(self):
#         self.category = Category(Name='Cars')
#         self.category.save()
#
#     def tearDown(self):
#         Category.objects.all().delete()
#
#     def test_instance(self):
#         self.assertTrue(isinstance(self.category, Category))
#
#     def test_save_category(self):
#         Category.objects.all().delete()
#         self.category.save_category()
#         categories = Category.objects.all()
#         self.assertTrue(len(categories) > 0)
#
#     def test_update_category(self):
#         new_category_name = 'Food'
#         self.category.update_category(self.category.id, new_category_name)
#         updated_category = Category.objects.filter(Name='Food')
#         self.assertTrue(len(updated_category) > 0)
#
#     def test_delete_category(self):
#         self.category.delete_category()
#         category = Category.objects.all()
#         self.assertTrue(len(category) == 0)
#
#
# class ImageTestClass(TestCase):
#     def setUp(self):
#         self.location = Location(location_name='Nairobi')
#         self.location.save()
#
#         self.category = Category(Name='Cars')
#         self.category.save()
#
#         self.image_ferrari = Image(Name='image_ferrari', description='this is a test instance',
#                                    location=self.location, category=self.category)
#         self.image_ferrari.save_image()
#
#         self.image_gucci = Image(Name='image_gucci', description='this is a test instance',
#                                  location=self.location, category=self.category)
#         self.image_gucci.save_image()
#
#     def test_instance(self):
#         self.assertTrue(isinstance(self.image_ferrari, Image))
#
#     def tearDown(self):
#         Image.objects.all().delete()
#         Location.objects.all().delete()
#         Category.objects.all().delete()
#
#     def test_save_image(self):
#         self.image_ferrari.save_image()
#         images = Image.objects.all()
#         self.assertTrue(len(images) > 0)
#
#     def test_update_image(self):
#         self.image_ferrari.save_image()
#         self.image_ferrari.update_image(self.image_ferrari.id, 'media/test_image.jpg')
#         updated_image = Image.objects.filter(image='media/test_image.jpg')
#         self.assertTrue(len(updated_image) > 0)
#
#     def test_delete_image(self):
#         self.image_ferrari.save_image()
#         self.image_ferrari.delete_image()
#         self.image_gucci.delete_image()
#         images = Image.objects.all()
#         self.assertTrue(len(images) == 0)
#
#     def test_get_image_by_id(self):
#         got_image = self.image_ferrari.get_image_by_id(self.image_ferrari.id)
#         image = Image.objects.filter(id=self.image_ferrari.id)
#         self.assertTrue(got_image, image)
#
#     def test_filter_by_location(self):
#         location = 'Nairobi'
#         got_image = self.image_ferrari.filter_by_location(location)
#         self.assertTrue(len(got_image) > 1)
#
#     def test_search_by_category(self):
#         category = 'Cars'
#         got_image = self.image_ferrari.search_by_category(category)
#         self.assertTrue(len(got_image) > 1)