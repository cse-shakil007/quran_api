from rest_framework import serializers

from .models import Ayah, Surah, JuzModel

class SurahAyahSerializer(serializers.ModelSerializer):
    ayah_id = serializers.IntegerField(source='id')
    
    class Meta:
        model = Ayah
        fields = ["ayah_id", "audio", "audio_secondary", "ayah", "pronunciation", "meaning", "juz"]

class JuzAyahSerializer(serializers.ModelSerializer):
    ayah_id = serializers.IntegerField(source='id')
    surah_id = serializers.IntegerField(source='sura_id')
    
    class Meta:
        model = Ayah
        fields = ["surah_id", "ayah_id", "audio", "audio_secondary", "ayah", "pronunciation", "meaning"]

class AyahSerializer(serializers.ModelSerializer):
    ayah_id = serializers.IntegerField(source='id')
    surah_id = serializers.IntegerField(source='sura_id')
    
    class Meta:
        model = Ayah
        fields = ["surah_id", "ayah_id", "audio", "audio_secondary", "ayah", "pronunciation", "meaning", "juz"]
    
    """def to_representation(self, instance):
        response = super().to_representation(instance)
        response['sura'] = SurahSerializer(instance.sura).data
        return response"""

class SurahSerializer(serializers.ModelSerializer):
    surah_id = serializers.IntegerField(source='id')
    class Meta:
        model = Surah
        fields = ["surah_id","name", "bangla_name", "bangla_name_translation", "number_of_ayahs","revelation_type"]


class SurahByIdSerializer(serializers.ModelSerializer):
    surah_id = serializers.IntegerField(source='id')
    ayahs = SurahAyahSerializer(source='sura',many=True)
    class Meta:
        model = Surah
        fields = ["surah_id", "name", "bangla_name", "bangla_name_translation", "number_of_ayahs","revelation_type", "ayahs"]
    

class JuzSerializer(serializers.ModelSerializer):
    juz = serializers.IntegerField(source='juz_number')
    ayahs = JuzAyahSerializer(source='juz',many=True)
    class Meta:
        model = JuzModel
        fields =  ["juz",  "ayahs"] 




