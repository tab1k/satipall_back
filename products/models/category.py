from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name=_("Наименование"),
        blank=False,
        null=True,
    )
    
    class Meta:
        verbose_name = _("Категория товаров")
        verbose_name_plural = _("Категории товаров")
