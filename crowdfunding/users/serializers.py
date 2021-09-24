from rest_framework import serializers
from .models import CustomUser
from django.utils import timezone

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    company = serializers.CharField(max_length=200)
    location = serializers.CharField(max_length=200)
    user_bio = serializers.CharField(max_length=None, default="")
    bio_pic = serializers.URLField(default="")
    date_joined = serializers.DateField(default=timezone.now())
    project_owner = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.user_bio = validated_data.get('user_bio', instance.user_bio)
        instance.bio_pic = validated_data.get('bio_pic', instance.bio_pic)
        instance.location = validated_data.get('location', instance.location)
        instance.project_owner = validated_data.get('is_open', instance.project_owner)
        instance.save()
        return instance