from django.contrib import admin
from .models import SecurityKey, Surah, JuzModel, Ayah
from import_export.admin import ImportExportModelAdmin

admin.site.register(SecurityKey)

@admin.register(Surah)
class SurahAdmin(ImportExportModelAdmin):
    class Meta:
        model = Surah
    list_display = ["id", "bangla_name", "number_of_ayahs", "revelation_type"]
    ordering = ["id", "bangla_name", "number_of_ayahs", "revelation_type"]
    
@admin.register(JuzModel)
class JuzModelAdmin(ImportExportModelAdmin):
    class Meta:
        model = JuzModel
    list_display = ["id", "juz_number"]
    ordering = ["id", "juz_number"]
        
@admin.register(Ayah)
class AyahAdmin(ImportExportModelAdmin):
    class Meta:
        model = Ayah
    list_display = ["id", "pronunciation"]
    ordering = ["id", "pronunciation"]