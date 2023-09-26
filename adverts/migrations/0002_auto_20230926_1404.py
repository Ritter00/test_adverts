# Generated by Django 4.2.5 on 2023-09-26 14:04

from django.db import migrations
from django.contrib.auth import get_user_model

UserModel = get_user_model()
user = ['admin', 'adminpassword', 'admin@example.com']

def create_example(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    if not UserModel.objects.filter(username=user[0]).exists():
        UserModel.objects.create_superuser(username=user[0], email=user[2], password=user[1],)
    City = apps.get_model("adverts", "City")
    Category = apps.get_model("adverts", "Category")
    Advert = apps.get_model("adverts", "Advert")
    City.objects.using(db_alias).bulk_create([
            City(name="London",),
            City(name="Dublin",),
        ])
    Category.objects.using(db_alias).bulk_create([
            City(name="Sport",),
            City(name="Other",),
        ])
    city_1, created = City.objects.get_or_create(name='Dublin')
    city_2, created = City.objects.get_or_create(name='London')
    cat_1, created = Category.objects.get_or_create(name='Sport')
    cat_2, created = Category.objects.get_or_create(name='Other')
    Advert.objects.using(db_alias).bulk_create([
        Advert(title ='It is adverts',description = 'hello world',city = city_2,category = cat_2),
        Advert(title ='selling a ball',description = 'it is a the good ball',city = city_2,category = cat_1),
        Advert(title ='selling house',description = 'it is the big house',city = city_1,category = cat_1),
    ])
class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_example),
    ]