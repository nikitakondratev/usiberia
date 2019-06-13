from django.db import models
from django.urls import reverse


class Article(models.Model):
    class Meta:
        db_table = 'article'
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-create"]

    title = models.CharField("Заголовок", max_length=70)
    text = models.TextField("Текст статьи")
    description = models.TextField("Краткое описание", max_length=340, default="")
    image = models.ImageField("Изображение", upload_to="../media/images", blank=True,
                              default="../static\images\logo.png")
    create = models.DateTimeField("Создано", auto_now_add=False)
    update = models.DateTimeField("Обновлено", auto_now=True)
    moder = models.BooleanField("Модерация", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    # def book_detail_view(request, pk):
    #     try:
    #         book_id = Article.objects.get(pk=pk)
    #     except Article.DoesNotExist:
    #         raise Http404("Article does not exist")
    #
    #     # book_id=get_object_or_404(Book, pk=pk)
    #
    #     return render(
    #         request,
    #         'news/article_detail.html',
    #         context={'article': book_id, }
    #     )
