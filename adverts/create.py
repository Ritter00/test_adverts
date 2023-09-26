from django.contrib.auth.models import User
from .models import *

def create_superuser():
    username = 'admin'
    password = 'adminpassword'
    email = 'admin@example.com'

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        
def create_ad():
    if not City.objects.filter(name='London').exists():
        City.objects.create(name='London')
    city_1 = City.objects.get(name='London')
    city_2, created = City.objects.get_or_create(name='Dublin')
    if not Category.objects.filter(name='Sport').exists():
        Category.objects.create(name='Sport')
    cat_1 = Category.objects.get(name='Sport')
    
    cat_2, created = Category.objects.get_or_create(name='Adverts')
    print(cat_2)
    ad_1, cr = Advert.objects.get_or_create(
        title ='selling a ball',
        description = 'it is a the good ball',
        city = city_1,
        category = cat_1,
    )
    ad_2, cr = Advert.objects.get_or_create(
        title ='It is adverts',
        description = 'hello world',
        city = city_2,
        category = cat_2,
    )
    ad_2, cr = Advert.objects.get_or_create(
        title ='selling house',
        description = 'it is the big house',
        city = city_1,
        category = cat_2,
    )

if __name__ == '__main__':
    create_superuser()