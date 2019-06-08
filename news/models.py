from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, help_text="Введите заголовок")

    def __str__(self):
        return self.title
