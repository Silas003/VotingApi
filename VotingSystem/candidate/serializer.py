from rest_framework import serializers
from .models import Aspirant,Vote


class AspirantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aspirant
        fields=['id','first_name','second_name','image']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields=['name','votes']