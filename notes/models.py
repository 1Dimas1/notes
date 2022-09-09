from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime


class Note(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title', blank=True)
    text = models.TextField(verbose_name='Text', blank=True)
    reminder = models.DateField(max_length=100, verbose_name='Reminder', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Notes'

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Categories'
