from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название должности')
    slug = models.SlugField(verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название Проекта")
    image = models.ImageField(upload_to='media/project', verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    customer = models.CharField(max_length=255, verbose_name='Заказчик')
    date = models.DateField(auto_now_add=False, verbose_name="Дата сдачи пректа")
    link = models.CharField(max_length=300, blank=True, verbose_name="Ссылка на проект")
    slug = models.SlugField(verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Person(models.Model):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    date_joined = models.DateField(verbose_name='С каких пор работает', auto_now_add=False)
    description = models.TextField(verbose_name='Описание')
    position = models.ForeignKey(Position, verbose_name='Должность', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Фото', upload_to='media/persons')
    age = models.PositiveIntegerField(default=16, verbose_name='Возраст')
    email = models.EmailField(verbose_name='Почта', max_length=255, blank=False)
    telegram = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
