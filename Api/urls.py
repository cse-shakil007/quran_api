from django.urls import path
from .views import SurahAPIView, SurahByIdAPIView, JuzAPIView, AyahApiView, RandomAyahAPIView, SurahAyahApiView

urlpatterns = [
    path('surah/<str:key>/',SurahAPIView.as_view(),name="sura"),
    path('surah/<int:id>/<str:key>/',SurahByIdAPIView.as_view(),name="surah"),
    path('juz/<int:id>/<str:key>/',JuzAPIView.as_view(),name="juz"),
    path('ayah/<int:id>/<str:key>/',AyahApiView.as_view(),name="ayah"),
    path('ayah/random/<str:key>/',RandomAyahAPIView.as_view(),name="random_ayah"),
    path('surah/<int:surah_id>:<int:ayah_num>/<str:key>/',SurahAyahApiView.as_view(),name="surah_ayah"),
]
