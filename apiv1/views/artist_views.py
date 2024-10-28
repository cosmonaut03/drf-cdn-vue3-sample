from typing import Any
from apiv1.models.artist import Artist
from rest_framework.response import Response
from rest_framework import status, views, serializers

from drf_spectacular.utils import extend_schema


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class ArtistListCreateView(views.APIView):
    @extend_schema(
        responses=ArtistSerializer(many=True), summary="アーティストリストの取得"
    )
    def get(self, request, *args: Any, **kwargs: Any) -> Response:
        serializer = ArtistSerializer(instance=Artist.objects.all(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    @extend_schema(responses=ArtistSerializer, summary="アーティストの作成")
    def post(self, request, *args, **kwargs):
        pass


class ArtistRetrieveUpdateDestroyAPIView(views.APIView):
    @extend_schema(responses=ArtistSerializer)
    def get(self, request, *args, **kwargs):
        pass
