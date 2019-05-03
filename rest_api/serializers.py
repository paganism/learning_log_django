from rest_framework import serializers
from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry


# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff')


class TopicSerializer(serializers.ModelSerializer):

    owner = UserSerializer()

    class Meta:
        model = Topic
        fields = ('id', 'text', 'date_added', 'owner')


class EntrySerializer(serializers.ModelSerializer):

    # topic_id = TopicSerializer()

    class Meta:
        model = Entry
        fields = ('id', 'text', 'date_added', 'topic_id')
