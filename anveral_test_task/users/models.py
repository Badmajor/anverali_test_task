from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    contact = models.CharField(
        'Контакты',
        max_length=256,
        blank=True,
    )
    experience = models.TextField(
        'Опыт'
    )


class Order(models.Model):
    title = models.CharField(
        'Название',
        max_length=256,
    )
    owner = models.ForeignKey(
        CustomUser,
        related_name='order',
        on_delete=models.CASCADE,
    )
    contractor = models.ForeignKey(
        CustomUser,
        related_name='project',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'заказы'
        default_related_name = 'order'

    def __str__(self):
        return self.title
