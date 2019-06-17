
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.models import BookInfo

# 增加操作
from apps.serializers import  BookModelSerializer


class BooksView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request):
        '''
        :param request:
        :return: 查询所有图书
        '''
        books = self.get_queryset()
        ser = self.serializer_class(books, many=True)
        return Response(ser.data)

    def post(self, request):
        """
        :param request:
        :return: 新增图书
        """
        data_dict = request.data
        ser = self.get_serializer(data=data_dict)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)


class BookView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer

    def put(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 修改图书
        '''
        data_dict = request.data
        try:
            book = self.get_object()
        except Exception:
            return Response({'errors': '未找到该书'}, status=400)

        ser = self.get_serializer(book, data=data_dict)
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
            book = self.get_object()
        except Exception:
            return Response({'errors': '未找到该书'}, status=400)
        book.delete()
        return HttpResponse(status=204, content='删除成功！')
