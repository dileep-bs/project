from rest_framework import serializers
from .models import Member,time

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = time
        fields=('start_time','end_time')

class MemberSerializers(serializers.ModelSerializer):
    activity_periods = TimeSerializer(read_only=True, many=True)
    class Meta:
        model = Member
        fields = ('id','real_name','tz','activity_periods')

class AddMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields='__all__'