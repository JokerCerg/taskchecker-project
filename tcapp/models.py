from django.db import models
from django.shortcuts import reverse


class Task(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)

    def get_absolute_url(self):
        return reverse('task_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

