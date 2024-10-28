from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import serializers, viewsets
from apiv1.models.book import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "price"]
        extra_kwargs = {
            "title": {
                "error_messages": {
                    "blank": "タイトルは空にできません。",
                }
            },
            "price": {
                "error_messages": {
                    "invalid": "価格には有効な整数を入力してください。",
                }
            },
        }


class BookViewSet(viewsets.ModelViewSet):
    """本モデルのCRUD用APIクラス"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
