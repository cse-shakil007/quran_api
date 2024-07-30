from django.shortcuts import render

from .models import Surah, JuzModel, Ayah, SecurityKey
from .serializers import SurahSerializer, SurahByIdSerializer, JuzSerializer, AyahSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
import json
import random
from django.shortcuts import get_object_or_404
from django.http import Http404


def error404(request, exception): 
    context = {
        "code": status.HTTP_404_NOT_FOUND,
        "status": "RESOURCE_NOT_FOUND",
        "data": "Not found."
    }
    return HttpResponse(json.dumps(context), content_type='application/json')  

class SurahAPIView(APIView):
    def get(self, request, key, format=None): 
        try:
            result = get_object_or_404(SecurityKey, is_active=True, key=key)
        except Http404:
            context = {
                "code": status.HTTP_404_NOT_FOUND,
                "status": "RESOURCE_NOT_FOUND",
                "data": "Not found."
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        if result.key == key:
            instance = Surah.objects.filter(is_active=True) 
            serializer = SurahSerializer(instance, many = True)
            context = {
                "code": status.HTTP_200_OK,
                "status": "OK",
                "data":serializer.data
            }
            return HttpResponse(json.dumps(context), content_type='application/json')  

class SurahByIdAPIView(APIView):
    def get_object(self, id):
        try:
            return Surah.objects.get(is_active=True, id=id)
        except Surah.DoesNotExist:
            return None

    def get(self, request, id, key, format=None): 
        try:
            result = get_object_or_404(SecurityKey, is_active=True, key=key)
        except Http404:
            context = {
                "code": status.HTTP_404_NOT_FOUND,
                "status": "RESOURCE_NOT_FOUND",
                "data": "Not found."
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        if result.key == key:
            instance = self.get_object(id)
            cou = Surah.objects.filter(is_active=True).count()
            if not instance:
                context = {
                    "code": status.HTTP_404_NOT_FOUND,
                    "status": "NOT FOUND",
                    "data": "Surah Id should be between 1 and " + str(cou) +"."
                }
                return HttpResponse(json.dumps(context), content_type='application/json')

            serializer = SurahByIdSerializer(instance)
            context = {
                "code": status.HTTP_200_OK,
                "status": "OK",
                "data":serializer.data
            }
            return HttpResponse(json.dumps(context), content_type='application/json')


class JuzAPIView(APIView):
    def get_object(self, id):
        try:
            return JuzModel.objects.get(is_active=True, id=id)
        except JuzModel.DoesNotExist:
            return None

    def get(self, request, id, key, format=None): 
        try:
            result = get_object_or_404(SecurityKey, is_active=True, key=key)
        except Http404:
            context = {
                "code": status.HTTP_404_NOT_FOUND,
                "status": "RESOURCE_NOT_FOUND",
                "data": "Not found."
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        if result.key == key:
            instance = self.get_object(id)
            cou = JuzModel.objects.filter(is_active=True).count()
            if not instance:
                context = {
                    "code": status.HTTP_404_NOT_FOUND,
                    "status": "NOT FOUND",
                    "data": "Juz number should be between 1 and " + str(cou) +"."
                }
                return HttpResponse(json.dumps(context), content_type='application/json')

            serializer = JuzSerializer(instance)
            context = {
                "code": status.HTTP_200_OK,
                "status": "OK",
                "data":serializer.data
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

class AyahApiView(APIView):
    def get_object(self, id):
        try:
            return Ayah.objects.get(is_active=True, id=id)
        except Ayah.DoesNotExist:
            return None

    def get(self, request, id, key, format=None): 
        try:
            result = get_object_or_404(SecurityKey, is_active=True, key=key)
        except Http404:
            context = {
                "code": status.HTTP_404_NOT_FOUND,
                "status": "RESOURCE_NOT_FOUND",
                "data": "Not found."
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        if result.key == key:
            instance = self.get_object(id)
            cou = Ayah.objects.filter(is_active=True).count()
            if not instance:
                context = {
                    "code": status.HTTP_404_NOT_FOUND,
                    "status": "NOT FOUND",
                    "data": "Please specify an Ayah Id (1 to "+str(cou) +")." 
                }
                return HttpResponse(json.dumps(context), content_type='application/json')

            serializer = AyahSerializer(instance)
            context = {
                "code": status.HTTP_200_OK,
                "status": "OK",
                "data":serializer.data
            }
            return HttpResponse(json.dumps(context), content_type='application/json')

class RandomAyahAPIView(APIView):
    def get_object(self, random_num):
        try:
            return Ayah.objects.get(is_active=True, id=random_num)
        except Ayah.DoesNotExist:
            return None

    def get(self, request, key, format=None): 
        try:
            result = get_object_or_404(SecurityKey, is_active=True, key=key)
        except Http404:
            context = {
                "code": status.HTTP_404_NOT_FOUND,
                "status": "RESOURCE_NOT_FOUND",
                "data": "Not found."
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        if result.key == key:
            cou = Ayah.objects.filter(is_active=True).count()
            random_num = 0
            if cou > 0:
                random_num =  random.randint(1, cou)
            instance = self.get_object(random_num)
            cou = Ayah.objects.filter(is_active=True).count()
            if not instance:
                context = {
                    "code": status.HTTP_404_NOT_FOUND,
                    "status": "NOT FOUND",
                    "data": "Please specify an Ayah Id (1 to "+str(cou) +")." 
                }
                return HttpResponse(json.dumps(context), content_type='application/json')

            serializer = AyahSerializer(instance)
            context = {
                "code": status.HTTP_200_OK,
                "status": "OK",
                "data":serializer.data
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        
class SurahAyahApiView(APIView):
    def get_object(self, surah_id, ayah_num):
        try:
            return Ayah.objects.get(is_active=True, sura_id = surah_id, ayah_num=ayah_num)
        except Ayah.DoesNotExist:
            return None

    def get(self, request, surah_id, ayah_num, key, format=None): 
        try:
            result = get_object_or_404(SecurityKey, is_active=True, key=key)
        except Http404:
            context = {
                "code": status.HTTP_404_NOT_FOUND,
                "status": "RESOURCE_NOT_FOUND",
                "data": "Not found."
            }
            return HttpResponse(json.dumps(context), content_type='application/json')
        if result.key == key:
            instance = self.get_object(surah_id, ayah_num)

            cou = Surah.objects.filter(is_active=True).count()
            try:
                result = get_object_or_404(Surah, is_active=True, id=surah_id)
            except Http404:
                context = {
                    "code": status.HTTP_404_NOT_FOUND,
                    "status": "NOT FOUND",
                    "data": "Surah Id should be between 1 and " + str(cou) +"."
                }
                return HttpResponse(json.dumps(context), content_type='application/json')
            if not instance:
                cout = Surah.objects.get(is_active=True, id = surah_id)
                context = {
                    "code": status.HTTP_404_NOT_FOUND,
                    "status": "NOT FOUND",
                    "data": "Please specify an Ayah Id (1 to "+str(cout.number_of_ayahs) +")." 
                }
                return HttpResponse(json.dumps(context), content_type='application/json')
            serializer = AyahSerializer(instance)
            context = {
                "code": status.HTTP_200_OK,
                "status": "OK",
                "data":serializer.data
            }
            return HttpResponse(json.dumps(context), content_type='application/json')












