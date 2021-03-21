from rest_framework import serializers
from api.models import Member, ActivityPeriod

# This is ActivityPeriod serializer that serialize Activity Period data.


class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


# This is Member Serializer which serialize member data.
class MemberSerializer(serializers.ModelSerializer):
    # This is related field of member.
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = Member
        fields = ['id', 'real_name', 'tz', 'activity_periods']
