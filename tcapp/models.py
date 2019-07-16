from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(s):
    title_slug = slugify(s, allow_unicode=True)
    count_slug = Task.objects.all().filter(title__iexact=s).count()
    if count_slug > 0:
        return title_slug + '-' + str(int(count_slug + 1))
    else:
        return title_slug


class Task(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    body = models.TextField(blank=False, db_index=True)

    def get_absolute_url(self):
        return reverse('task_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('task_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('task_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

