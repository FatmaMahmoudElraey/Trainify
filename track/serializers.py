from rest_framework import serializers
from .models import Tracks

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracks
        fields = '__all__' 
