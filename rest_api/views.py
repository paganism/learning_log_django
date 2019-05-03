from django.shortcuts import render

# API imports
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from rest_framework import status

from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry

from .serializers import TopicSerializer


class Topics(APIView):

    def get(self, request):
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True, context={'request': request })

        # serializer_context = {'request': Request(request),}

        return Response({'topics': serializer.data})
