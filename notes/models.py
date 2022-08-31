from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    reminder = models.CharField(max_length=300, verbose_name='Reminder', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category id')

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Notes'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'
