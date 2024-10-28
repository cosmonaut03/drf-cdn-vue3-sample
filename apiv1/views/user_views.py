from typing import Any
from typing_extensions import Self
from venv import logger
from rest_framework import serializers, views, status
from rest_framework.request import Request
from rest_framework.response import Response
from apiv1.models.user import User
from drf_spectacular.utils import extend_schema


class UserRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserListCreateView(serializers.ModelSerializer):
    pass


@extend_schema(responses=UserRetriveSerializer, tags=["user"])
class UserRetriveUpdateDeleteView(views.APIView):
    def get(self: Self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """ユーザ詳細情報の取得"""
        pk = kwargs["pk"]
        user = User.objects.alive().filter(pk=pk).first()

        if user is None:
            logger.error("userが存在しません")
            return Response("userが存在しません", status=status.HTTP_404_NOT_FOUND)

        serializer = UserRetriveSerializer(instance=user)

        return Response(serializer.data, status=status.HTTP_200_OK)
