from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response

from apps.models import BookInfo

# 增加操作
from apps.serializers import BookModelSerializer


class BooksView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request):
        '''
        :param request:
        :return: 查询所有图书
        '''
        return self.list(request)

    def post(self, request):
        """
        :param request:
        :return: 新增图书
        """
        return self.create(request)


class BookView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer

    def get(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 查询单一图书
        '''
        return self.retrieve(request, pk)

    def put(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 修改图书
        '''
        return self.update(request, pk)

    def delete(self, request, pk):
        '''
        :param request:
        :param pk:
        :return: 删除图书
        '''
        return self.destroy(request, pk)
