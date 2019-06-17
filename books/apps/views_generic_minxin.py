from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.models import BookInfo
from apps.serializers import BookModelSerializer


class BooksView(ListCreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer


class BookView(RetrieveUpdateDestroyAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookModelSerializer
