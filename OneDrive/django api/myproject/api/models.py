from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)  # Поле для изображения

    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Второе имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="пaроль")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




