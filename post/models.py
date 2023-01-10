from django.db import models

# Create your models here.
class Legends(models.Model):
    qwer = models.CharField(max_length=50)
    asd = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.qwer


class Weekly(models.Model):
    name = models.CharField(max_length=50)
    pochta = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.pochta