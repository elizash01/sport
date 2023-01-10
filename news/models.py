from django.db import models

# Create your models here.
 
class News(models.Model):
    name = models.CharField(max_length=50, verbose_name='название спорта')
    forecast = models.CharField(max_length=147, verbose_name='прогноз')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')


    def __str__(self) -> str:
        return self.name


class Comments(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username     