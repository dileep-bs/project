# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.exceptions import APIException,PermissionDenied,NotFound,NotAcceptable
from django.shortcuts import render
from rest_framework.response import Response
from .models import Member,time
from .serializers import MemberSerializers,TimeSerializer,AddMemberSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import authentication


# views here.

class getMembers(APIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = MemberSerializers 

    def get(self,request):

        queryset = Member.objects.all()

        if queryset.count()  ==  0:
            raise NotFound

        serializer = MemberSerializers(queryset,many = True)
        response = {'ok':True,'member':serializer.data}
        return Response(response,status = status.HTTP_200_OK)

class addMember(APIView):
    permission_classes = []  
    authentication_classes = []
    serializer_class  =  AddMemberSerializer

    def post(self,request):
        serializer = AddMemberSerializer(data = request.data,partial = True)
        if serializer.is_valid(raise_exception = True) :
            serializer.save()
            response = {'ok':True,'member':serializer.data}
            return Response(response,status = status.HTTP_201_CREATED)
        return Response(response,status = status.HTTP_400_BAD_REQUEST)

class addTime(APIView):
    permission_classes = []  
    authentication_classes = []
    serializer_class  =  TimeSerializer

    def post(self,request):
        serializer = TimeSerializer(data = request.data,partial = True)
        if serializer.is_valid(raise_exception = True) :
            serializer.save()
            response = {'ok':True,'member':serializer.data}
            return Response(response,status = status.HTTP_201_CREATED)
        return Response(response,status = status.HTTP_400_BAD_REQUEST)