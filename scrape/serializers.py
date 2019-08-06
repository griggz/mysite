from django.contrib.auth import get_user_model, authenticate, login, logout
from django.db.models import Q
from django.urls import reverse
from django.utils import timezone

from rest_framework import serializers

from .models import Results, Yelp

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True,
                                     read_only=True)

    class Meta:
        model = User
        fields = [
            'username'
        ]


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = (
            'author',
            'date',
            'rating',
            'review'
        )


class ScrapeSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='scrape-api:detail',
        lookup_field='slug'
    )
    scrape_date = serializers.DateField(default=timezone.now())
    user = UserPublicSerializer(read_only=True)
    reviews = ResultsSerializer(many=True, read_only=True)
    owner = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Yelp
        fields = (
            'user',
            'owner',
            'url',
            'business_name',
            'link',
            'scrape_date',
            'slug',
            'reviews',
        )

        @staticmethod
        def create(validated_data):
            link = validated_data.pop('link')
            biz_url = link.rsplit('biz/', 1)
            if '?' in biz_url[1]:
                business = biz_url[1].split('?')[0]
            else:
                business = biz_url[1]

            instance = Yelp.objects.create(**validated_data)
            instance.business_name.add(business)
            return Yelp.objects.create(**validated_data)

    def get_owner(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            if request.user == request.user:
                return True
        return False
