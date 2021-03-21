from django.shortcuts import redirect
from django.http import JsonResponse
from api.serializers import MemberSerializer
from api.models import Member
from rest_framework import status, generics
from rest_framework.response import Response
from api.manager import generating_data

import time
import json

# Time delay mixin for delay api atleast 30 seconds


class TimeDelayMixin(object, ):

    def dispatch(self, request, *args, **kwargs):
        time.sleep(30)
        return super().dispatch(request, *args, **kwargs)


# Define home route
def home(request):
    # generating_data()
    return redirect('members')

# #Define home route
# def home(request):
#     members = Member.objects.all()
#     serializer = MemberSerializer(members, many=True)
#     return JsonResponse(serializer.data, safe=False)


# This is CBV for server and display all members and with its activity periods
class MemberListApiView(TimeDelayMixin, generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def list(self, request):
        generating_data()
        queryset = self.get_queryset()
        serializer = MemberSerializer(queryset, many=True)

        #Write json data in an output.json file.
        with open("output.json", "w") as fw: 
            json.dump(serializer.data, fw)
            
        return Response(serializer.data, status=status.HTTP_200_OK)
