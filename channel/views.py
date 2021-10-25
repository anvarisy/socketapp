from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class Homepage(View):
    def get(self, request):
        return HttpResponse('koala')

class Roompage(View):
    def get(self, request):
        return JsonResponse({"Status":"OK"})