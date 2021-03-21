from django.shortcuts import redirect
from api.serializers import MemberSerializer
from api.models import Member
from rest_framework import status, generics
from rest_framework.response import Response
from api.manager import generating_data

import time

# Time delay mixin for delay api atleast 30 seconds


class TimeDelayMixin(object, ):

    def dispatch(self, request, *args, **kwargs):
        time.sleep(30)
        return super().dispatch(request, *args, **kwargs)


# Define home route
def home(request):
    # generating_data()
    return redirect('members')


# This is CBV for server and display all members and with its activity periods
class MemberListApiView(TimeDelayMixin, generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request):
        generating_data()
        queryset = self.get_queryset()
        serializer = MemberSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
