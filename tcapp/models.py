from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


def gen_slug(title):
    title_slug = slugify(title, allow_unicode=True)
    check_slug = Task.objects.all().filter(slug__iexact=title_slug).exists()
    n = 1
    while check_slug != 0:
        test_slug = title_slug + '-' + str(n)
        n += 1
        check_slug = Task.objects.all().filter(slug__iexact=test_slug).exists()
        print(check_slug)
        if check_slug == 0:
            title_slug = test_slug
    return title_slug


class Task(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField(blank=False, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

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

