from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models

from cms.apps.pages.models import DEFAULT_LANGUAGE, LANGUAGES_ENGLISH_DICTIONARY
from cms.apps.pages.models import LANGUAGES_ENGLISH


class MultilingualObject(models.Model):
    admin_name = models.CharField(
        max_length=4096,
        help_text="Name of the object that will be used within the admin",
        verbose_name="Name"
    )

    admin_description = models.TextField(
        blank=True,
        null=True,
        help_text="Short description that will be used within the admin",
        verbose_name="Description"
    )

    admin_notes = models.TextField(
        blank=True,
        null=True,
        help_text="A set of notes that will be used within the admin",
        verbose_name="Notes"
    )

    default_language = models.CharField(
        max_length=2,
        choices=LANGUAGES_ENGLISH,
        default=DEFAULT_LANGUAGE,
        db_index=True,
        help_text="The default language that will be used when a language object isn't found"
    )

    def translation_objects(self):
        return self.translation_object.objects.filter(parent=self)

    def get_translation_add_url(self):
        return '{}?parent={}'.format(
            reverse('admin:{}_{}_add'.format(
                self.translation_object._meta.app_label,
                self.translation_object._meta.model_name
            )),
            self.pk
        )

    class Meta:
        abstract = True


class MultilingualTranslation(models.Model):
    language = models.CharField(
        max_length=2,
        choices=LANGUAGES_ENGLISH,
        default=DEFAULT_LANGUAGE,
        db_index=True,
        help_text="The language that this translation is for"
    )

    version = models.PositiveIntegerField(
        default=1,
        help_text="Priority is given to the higher number. <br> Using versions you are able to create new language versions without publishing them"
    )

    published = models.BooleanField(
        default=False,
        help_text="Unchecking this box will leave this translation as unpublished and it will not be used on the website"
    )

    def __unicode__(self):
        return self.parent.admin_name

    def human_language(self):
        return LANGUAGES_ENGLISH_DICTIONARY[self.language]

    def get_change_url(self):
        return reverse('admin:{}_{}_change'.format(
            self._meta.app_label,
            self._meta.model_name
        ), args=[self.pk])

    class Meta:
        abstract = True
