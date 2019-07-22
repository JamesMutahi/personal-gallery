# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

Deafult_desc = '''Lorem ipsum dolor sit amet,
agam probatus indoctum cu quo.
Est eu quod rationibus,
nam platonem sententiae no.
Eu mel vero oporteat elaboraret.'''


class Category(models.Model):
    Name = models.CharField(max_length=30)

    @property
    def preview(self):
        first = self.images.last()
        return first.image.url

    def __str__(self):
        return self.Name


# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=255)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)


class Image(models.Model):
    Name = models.CharField(max_length=60)
    description = models.TextField(default=Deafult_desc)
    category = models.ForeignKey(Category, related_name="images")
    location = models.ForeignKey(Location)
    submited = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    @property
    def allinfo(self):
        info = {
            'name': self.Name,
            'desc': self.description,
            'image': self.image.url,
            'id': self.id,
        }
        return str(info)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, Name=None, category=None):
        self.Name = Name if Name else self.Name
        self.category = category if category else self.category
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls, search_term):
        locations = cls.objects.filter(location__location_name__icontains=search_term)
        return locations

    class Meta:
        ordering = ['submited']
