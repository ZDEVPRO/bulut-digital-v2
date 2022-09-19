from django.db import models
from django.utils.safestring import mark_safe


class Logo(models.Model):
    title = models.CharField(max_length=600)
    image = models.ImageField(upload_to='logo/')
    favicon = models.ImageField(upload_to='favicon/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sayt Logotipi'
        verbose_name_plural = 'Sayt Logotipi'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    def favicon_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.favicon.url))


class Contact(models.Model):
    full_name = models.CharField(max_length=600)
    phone = models.CharField(max_length=600)
    message = models.TextField()
    ip = models.CharField(max_length=300)
    create_time = models.TimeField(auto_now=True)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Aloqa Bo`limi'
        verbose_name_plural = 'Aloqa Bo`limi'
