from __future__ import unicode_literals
import re
import json

from django.conf import settings
from django.core.exceptions import ValidationError, ImproperlyConfigured
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext as _
from django.utils.timezone import now
from django.utils.encoding import python_2_unicode_compatible


# Create your models here



class CategoryManager(models.Manager):
    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category)
                                   .lower())

        new_category.save()
        return new_category


@python_2_unicode_compatible
class Category(models.Model):
    category = models.CharField(
        verbose_name=_("Category"),
        max_length=250, blank=True,
        unique=True, null=True)

    objects = CategoryManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category


@python_2_unicode_compatible
class SubCategory(models.Model):
    sub_category = models.CharField(
        verbose_name=_("Sub-Category"),
        max_length=250, blank=True, null=True)

    category = models.ForeignKey(
        Category, null=True, blank=True,
        verbose_name=_("Category"))

    objects = CategoryManager()

    class Meta:
        verbose_name = _("Sub-Category")
        verbose_name_plural = _("Sub-Categories")

    def __str__(self):
        return self.sub_category + " (" + self.category.category + ")"


@python_2_unicode_compatible
class QuizModel(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=60, blank=False)

    description = models.TextField(verbose_name=_("Description"), blank=True, help_text=_("a description of the quiz"))

    url = models.SlugField(max_length=60, blank=False, help_text=_("a user friendly url"),
                           verbose_name=_("user friendly url"))

    category = models.ForeignKey(Category, null=True, blank=True, verbose_name=_("Category"))

    random_order = models.BooleanField(blank=False, default=False, verbose_name=_("Random Order"),
                                       help_text=_("Display the questions in "
                                                   "a random order or as they "
                                                   "are set?"))

    unique_together = ("title", "url")

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/quiz/' + str(self.url) + '/'









