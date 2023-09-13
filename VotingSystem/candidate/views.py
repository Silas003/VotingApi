from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from .models import Aspirant,Vote
from .serializer import AspirantSerializer,VoteSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.db.models import Count
from datetime import timezone,timedelta,datetime
from rest_framework import permissions
from .permissions import TimeLimitPermission
@api_view(['GET'])
def home(request:Request):
    aspirant=Aspirant.objects.all()
    serializer=AspirantSerializer(instance=aspirant)
    response={
        "data":serializer.data
    }
    return Response(data=response,status=status.HTTP_200_OK)


class ListView(generics.ListCreateAPIView):
    queryset=Aspirant.objects.all()
    serializer_class=AspirantSerializer



class VoteView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes=[TimeLimitPermission]
        # queryset=Vote.objects.all()
        # serializer_class=VoteSerializer
        #    def post(self,request:Request):
        #         vote=Vote.objects.all()
        #         data=request.data
        #         serializer=VoteSerializer(instance=vote,data=data)
        #         if serializer.is_valid():
        #             serializer.save()
        #             return Response(data={'message':'vote successful'},status=status.HTTP_201_CREATED)
        #         return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
       




class Collective(APIView):
    def get(self,request:Request):
        cand_count=(Vote.objects.values('name__first_name','name__second_name').annotate(vote_count=Count('id')).order_by('name__first_name','name__second_name'))
        result_data=[]
        for entry in cand_count:
            first_name=entry['name__first_name']
            second_name=entry['name__second_name']
            vote_count=entry['vote_count']
            final_result={
                'name':f'{first_name} {second_name}',
                'vote_count':vote_count
            }
            result_data.append(final_result)
        return Response(result_data)