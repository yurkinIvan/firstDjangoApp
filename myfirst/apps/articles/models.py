import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_image       = models.ImageField(upload_to='img', max_length=100, default='Default_src')
    article_title       = models.CharField('Название статьи', max_length = 200)
    article_description = models.CharField('Описание статьи', max_length = 450)
    article_text        = models.TextField('Текст статьи')
    pub_date            = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    # For russian lang
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    # All the comments will be bind to the articles. Comment will be delete with the article.
    article      = models.ForeignKey(Article, on_delete = models.CASCADE)
    
    author_name  = models.CharField('Автор комментария', max_length = 50)
    comment_text = models.CharField('Текст комментария', max_length = 200)
    pub_date     = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'