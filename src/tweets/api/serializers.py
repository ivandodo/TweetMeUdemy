from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer

from ..models import Tweet #from tweets.models import Tweet


class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer()
    class Meta:
        model = Tweet
        fields = [
            "user",
            "content",
        ]