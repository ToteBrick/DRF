from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.models import BookInfo
from apps.serializers import BookModelSerializer


class BooksView(ListCreateAPIView):
    '''查询所有、保存图书'''
    queryset = BookInfo.objects.all()  # 指定查询集
    serializer_class = BookModelSerializer  # 指定序列化器


class BookView(RetrieveUpdateDestroyAPIView):
    '''查询单一图书、修改、删除图书'''
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer
