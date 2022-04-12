from django.db import models


class Statistics(models.Model):
    date = models.DateField(
        verbose_name='дата события',
    )
    views = models.PositiveIntegerField(
        verbose_name='количество показов',
        blank=True
    )
    clicks = models.PositiveIntegerField(
        verbose_name='количество кликов',
        blank=True
    )
    cost = models.FloatField(
        verbose_name='стоимость кликов',
        blank=True
    )
