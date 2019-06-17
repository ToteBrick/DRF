from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from apps.models import BookInfo
from apps.serializers import BookModelSerializer


class BooksView(viewsets.ViewSet):

    def list(self, request):
        '''查询所有图书'''
        books = BookInfo.objects.all()
        ser = BookModelSerializer(books, many=True)
        return Response(ser.data)

    def create(self, request):
        """
         :param request:
         :return: 新增图书
         """
        data_dict = request.data
        ser = BookModelSerializer(data=data_dict)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class BookView(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        '''查询单一图书'''
        book = BookInfo.objects.get(pk=pk)
        ser = BookModelSerializer(book)
        return Response(ser.data)

    def update(self, request, pk=None):
        '''更新图书'''
        data_dict = request.data
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception:
            return Response({'errors': '未找到该书'}, status=400)

        ser = BookModelSerializer(book, data=data_dict)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def destory(self, request, pk=None):
        '''
         :param request:
         :param pk:
         :return: 删除图书
         '''
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception:
            return Response({'errors': '未找到该书'}, status=400)
        book.delete()
        return HttpResponse(status=204, content='删除成功！')
