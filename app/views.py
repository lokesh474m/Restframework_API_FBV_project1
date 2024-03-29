from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def collegeJsonData(request):
    SOD=College.objects.all()
    JOD=CollegeModelSerializer(SOD,many=True)
    jsondata=JOD.data
    return Response(jsondata)