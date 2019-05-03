from django.shortcuts import render

# API imports
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status, viewsets

from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry

from .serializers import TopicSerializer, UserSerializer

from django.contrib.auth.models import User


class Topics(APIView):

    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(
            topics,
            many=True,
            context={'request': request}
            )

        return Response({'topics': serializer.data})


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = UserSerializers(snippet)
        return Response(serializer.data)

    class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer_class = UserSerializer
