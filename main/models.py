from django.db import models

# Create your models here.

class Personal(models.Model):
    name = models.CharField(max_length=255,verbose_name='Имя')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    iban_number = models.CharField(max_length=255, verbose_name='ИИН')
    state_address = models.CharField(max_length=255, verbose_name='Место проживания:')
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'id: {self.id}, Имя: {self.name}'

    class Meta:
        verbose_name = 'Весь персонал'
        verbose_name_plural = 'Весь персонал'
        ordering = ['name']
