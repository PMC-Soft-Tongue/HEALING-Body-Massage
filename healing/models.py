from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Comments(models.Model):
    text = models.TextField(max_length=900)
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        default_related_name = 'comments'
        ordering = ['created_at']