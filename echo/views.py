from django.shortcuts import HttpResponse,redirect,render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response as response
# Create your views here.
from echo.models import Meizis
from echo.serializers import MeiziSerializer
import xml.sax

from echo.models import Person

class XMLHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.buffer = ""
        self.mapping = {}

    def startElement(self, name, attributes):
        self.buffer = ""

    def characters(self, data):
        self.buffer += data

    def endElement(self, name):
        self.mapping[name] = self.buffer

    def getDict(self):
        return self.mapping


@api_view(['GET', 'POST'])
def echo(request, format=None):
    if request.method == 'GET':
        meizis = Meizis.objects.all()
        serializer = MeiziSerializer(meizis, many=True)
        return response(serializer.data)

    elif request.method == 'POST':
        serializer = MeiziSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create(request):
    # 新建一个对象的方法有以下几种：
    Person.objects.create(name='xiaoli', age=18)
    s = Person.objects.get(name='xiaoli')
    return HttpResponse(str(s))