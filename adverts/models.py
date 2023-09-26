from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128,)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории обьявлений'
        

class City(models.Model):
    name = models.CharField(max_length=128,)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города объявлений'
        

class Advert(models.Model):
    title = models.CharField(max_length=254, verbose_name='Заголовок объявления')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    description = models.TextField(verbose_name='Текст объявления',)
    views = models.PositiveIntegerField(verbose_name='Количество просмотров',  default=0)
    city = models.ForeignKey(City, related_name='city',  on_delete= models.CASCADE)
    category = models.ForeignKey(Category, related_name='category',  on_delete= models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'