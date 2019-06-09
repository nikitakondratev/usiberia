from django.db import models


class Article(models.Model):
    class Meta:
        db_table = 'article'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["create"]

    title = models.CharField("Заголовок", max_length=140)
    text = models.TextField("Текст статьи")
    description = models.TextField("Краткое описание", max_length=140, default="")
    image = models.ImageField("Изображение", upload_to="article/", blank=True)
    create = models.DateTimeField("Создано", auto_now_add=False)
    update = models.DateTimeField("Обновлено", auto_now=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.title
