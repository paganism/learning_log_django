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

    entries = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='text'
     )

    class Meta:
        model = Topic
        fields = ('id', 'text', 'date_added', 'owner', 'entries')


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ('id', 'text', 'date_added', 'topic_id')
