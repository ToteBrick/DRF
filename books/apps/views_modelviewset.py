from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from apps.serializers import BookModelSerializer, BookSerializer1, BookSerializer2
from apps.models import BookInfo


class BookInfoModelViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()

    # serializer_class = BookModelSerializer
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BookSerializer2
        elif self.action == 'list':
            return BookModelSerializer
        else:
            return BookSerializer1

    @action(methods=['get'], detail=True)
    def show(self, request, pk):
        book = self.get_object()
        ser = self.get_serializer(book)
        return Response(ser.data)
