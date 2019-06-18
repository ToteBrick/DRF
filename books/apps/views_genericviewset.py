from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from apps.serializers import BookModelSerializer
from apps.models import BookInfo


class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
        list:
        返回图书列表数据

        retrieve:
        返回图书详情数据

        latest:
        返回最新的图书数据

        read:
        修改图书的阅读量
        """
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer
    # 认证
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    # 权限
    permission_classes = [IsAuthenticated]  # 授权登录用户

    # 限制访问次数
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    # throttle_scope  指定类视图限流名字，来限制访问次数
    # 过滤字段
    # filter_fields = ('btitle', 'bread')  # 127.0.0.1:8000/books/?btitle=西游记
    # 排序
    filter_backends = [OrderingFilter]
    ordering_fields = ('bread', 'id')  # 127.0.0.1:8000/books/?ordering=-bread

    # 指定分页类
    class PageNum(PageNumberPagination):
        page_size = 3  # 每页默认大小
        page_size_query_param = 'page_size'  # 查询参数
        max_page_size = 6  # 最大显示条数

    # 指定分页
    pagination_class = PageNum  # 127.0.0.1:8000/books_set/?page=1&page_size=2

    # detail为False 表示不需要处理具体的BookInfo对象
    @action(methods=['get'], detail=False)
    def latest(self, request):
        """
        返回最新的图书信息
        """
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    # detail为True，表示要处理具体与pk主键对应的BookInfo对象
    @action(methods=['put'], detail=True)
    def read(self, request, pk):
        """
        修改图书的阅读量数据
        """
        book = self.get_object()
        book.bread = request.data.get('bread')
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
