from rest_framework import serializers
from django.utils.timesince import timesince

from accounts.api.serializers import UserDisplaySerializer

from ..models import Tweet #from tweets.models import Tweet


class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    date_display = serializers.SerializerMethodField()
    time_since = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            "user",
            "content",
            "timestamp",
            "date_display",
            "time_since",
        ]

    def get_date_display(self,obj):
        return obj.timestamp.strftime("%b %d %I:%M %p")

    def get_time_since(self,obj):
        return timesince(obj.timestamp) + " ago"