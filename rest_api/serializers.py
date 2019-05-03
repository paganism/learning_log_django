from rest_framework import serializers
from django.contrib.auth.models import User
from learning_logs.models import Topic, Entry


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    # owner_id = UserSerializer()
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Topic

        fields = ('id', 'text', 'date_added', 'owner')
