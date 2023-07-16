from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from apps.serializers import UserModelSerializer


class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        if cache.get('users') is not None:
            json = cache.get('users')
            return Response(json)
        data = self.serializer_class(self.get_queryset(), many=True).data
        cache.set('users', data, timeout=300)
        return Response(data)
