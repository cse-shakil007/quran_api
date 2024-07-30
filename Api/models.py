from django.db import models
from django.utils.translation import gettext_lazy as _


class SecurityKey(models.Model):
    key =  models.CharField(max_length=100, null=False, blank=False, verbose_name=_("key"), help_text=_("format: required, max_length=100"))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['key']

    class Meta:
        verbose_name = 'SecurityKey'
        verbose_name_plural = 'SecurityKey'

    def __str__(self):
        return self.key



class Surah(models.Model):
    STATUS = (
        ('মক্কা', 'মক্কা'),
        ('মদিনা', 'মদিনা'),
    )

    id = models.IntegerField(primary_key=True)
    name =  models.CharField(max_length=100, null=False, blank=False, verbose_name=_("name"), help_text=_("format: required, max_length=100"))
    bangla_name = models.CharField(max_length=100, null=False, blank=False, verbose_name=_("bangla_name"), help_text=_("format: required, max_length=100"))
    bangla_name_translation = models.CharField(max_length=100, null=False, blank=False, verbose_name=_("bangla_name_translation"), help_text=_("format: required, max_length=100"))
    number_of_ayahs = models.IntegerField(default=0)
    revelation_type = models.CharField(choices=STATUS, max_length=20, default='মক্কা')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['bangla_name']

    class Meta:
        verbose_name = 'Surah'
        verbose_name_plural = 'Surah'

    def __str__(self):
        return self.bangla_name 

class JuzModel(models.Model):
    id = models.IntegerField(primary_key=True)
    juz_number = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['juz_number']

    class Meta:
        verbose_name = 'JuzModel'
        verbose_name_plural = 'JuzModel'

    def __str__(self):
        return str(self.juz_number)

class Ayah(models.Model):
    id = models.IntegerField(primary_key=True)
    sura = models.ForeignKey(Surah, null=False, related_name='sura', blank=False, on_delete=models.CASCADE)
    ayah_num = models.IntegerField()
    audio = models.CharField(max_length=300, null=False, blank=False, verbose_name=_("audio"), help_text=_("format: required, max_length=300"))
    audio_secondary = models.CharField(max_length=300, null=False, blank=False, verbose_name=_("audio_secondary"), help_text=_("format: required, max_length=300"))
    ayah = models.CharField(max_length=300, null=False, blank=False, verbose_name=_("ayah"), help_text=_("format: required, max_length=300"))
    pronunciation = models.CharField(max_length=300, null=False, blank=False, verbose_name=_("pronunciation"), help_text=_("format: required, max_length=300"))
    meaning = models.CharField(max_length=300, null=False, blank=False, verbose_name=_("meaning"), help_text=_("format: required, max_length=300"))
    juz = models.ForeignKey(JuzModel, null=False, related_name='juz', blank=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['pronunciation']

    class Meta:
        verbose_name = 'Ayah'
        verbose_name_plural = 'Ayah'

    def __str__(self):
        return self.pronunciation




