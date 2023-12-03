from django.db import models  ### что за база данных django.db? Что там находится?
from django.utils import timezone


class Mebel(models.Model):  ### в models.Model передает данные из БД django.db?
    # id задается по умолчанию
    link = models.TextField('Ссылка')
    price = models.DecimalField(max_digits=12, decimal_places=2)  # DecimalField -- с возможностью дробного значения
    description = models.TextField('Описание')
    parse_datetime = models.DateTimeField(auto_now_add=True, blank=True)  ### что значит blank=True?    (deafault=timezone.now())

    def get_absolute_url(self):
        return self.link

    def __str__(self):
        return f'{self.price} | {self.description[:60]}' ### возвращает то, что получили выше: self.price -- это и есть price?


    class Meta:
        verbose_name = 'Мебель'  # откуда django знает вместо чего и где подставлять 'Мебель'?
        verbose_name_plural = 'Мебель'
        ordering = ['price']