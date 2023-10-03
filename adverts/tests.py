from django.test import TestCase
from .models import *

# Create your tests here.
class ModelTest(TestCase):
    
    def test_cat_city_ad(self):
        Category.objects.create(name='Sport')
        Category.objects.create(name='Other')
        City.objects.create(name='London')
        City.objects.create(name='Dublin')
        cat1 = Category.objects.get(name='Sport')
        cat2 = Category.objects.get(name='Other')
        city1 = City.objects.get(name='London')
        city2 = City.objects.get(name='Dublin')
        ad1 = Advert.objects.create(
            title='Hello',
            description='Test description',
            city= city1,
            category=cat1,
            )
        ad2 = Advert.objects.create(
            title='Hello2',
            description='Test description 2',
            city= city2,
            category=cat2,
            )
        self.assertEqual(ad1.title, 'Hello')
        self.assertEqual(ad2.description, 'Test description 2')
        self.assertEqual(ad2.category, cat2)