# projects/serializers.py
from rest_framework import serializers
from .models import Project, Pledge
from users.models import CustomUser
# from django.utils import timezone

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    total_raised = serializers.SerializerMethodField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    location = serializers.CharField(max_length=200)
    owner = serializers.ReadOnlyField(source='owner.id')
    
    def get_total_raised(self, obj):
        total_pledges = obj.pledges.all()
        total = 0
        for pledge in total_pledges:
            total += pledge.amount
        return total    

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter = serializers.ReadOnlyField(source='supporter.id')
    date_created = serializers.DateTimeField(default=timezone.now())
    project_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.goal = validated_data.get('goal',instance.goal)
        instance.image = validated_data.get('image',instance.image)
        instance.is_open = validated_data.get('is_open',instance.is_open)
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.location = validated_data.get('location',instance.location)
        instance.owner = validated_data.get('owner',instance.owner)
        instance.save()
        return instance

class PledgeDetailSerializer(PledgeSerializer):
    project = ProjectSerializer(many=False, read_only=True)
    amount = serializers.IntegerField()

    def update(self, instance, validated_data):

        new_amount = validated_data.get('amount', instance.amount)
        if new_amount >= instance.amount:
            instance.amount = new_amount
            instance.save()
            return instance
        else:
            return 