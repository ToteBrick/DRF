from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from apps.serializers import BookModelSerializer
from apps.models import BookInfo


class BookInfoModelViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer
