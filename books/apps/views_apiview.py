from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.models import BookInfo

# 增加操作
from apps.serializers import BookModelSerializer


class BooksView(APIView):

    def get(self, request):
        '''
        :param request:
        :return: 查询所有图书
        '''
        books = BookInfo.objects.all()
        ser = BookModelSerializer(books, many=True)
        return Response(ser.data)

    def post(self, request):
        """
        :param request:
        :return: 新增图书
        """
        data_dict = request.data
        ser = BookModelSerializer(data=data_dict)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class BookView(APIView):

    def get(self, request, pk):
        '''

        :param request:
        :param pk:
        :return: 查询单一图书
        '''
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception:
            return Response({'errors': '未找到该书'}, status=400)
        ser = BookModelSerializer(book)
        return Response(ser.data)

    def put(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 修改图书
        '''
        data_dict = request.data
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception:
            return Response({'errors': '未找到该书'}, status=400)

        ser = BookModelSerializer(book, data=data_dict)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)

    def delete(self, request, pk):
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
