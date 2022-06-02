from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name=_("Наименование"),
        blank=False,
        null=False,
    )
    description = models.TextField(
        _("Описание"),
        blank=True,
        null=True,
    )
    cost = models.PositiveSmallIntegerField(
        _("Цена"),
        default=0,
    )

    class Meta:
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")
