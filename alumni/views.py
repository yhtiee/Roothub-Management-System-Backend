from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import *
from authentication.models import *
from django.contrib.auth.models import User
# Create your views here.

class CreateAlumni(generics.CreateAPIView):
    query_set = Trainees_alumni.objects.all()
    serializer_class = AlumniSerializer

class TotalAlumni(APIView):
    def get(self, request):
        data = Trainees_alumni.objects.all()
        total = len(data)
        return Response(data={
            "total":total
        }, status=status.HTTP_200_0K)

class ListAllAlumni(generics.ListAPIView):
    queryset = Trainees_alumni.objects.all()
    serializer_class = AlumniSerializer

class ListAlumni(APIView):
    def post(self, request):
        my_users = request.data
        location = my_users["username"]
        # users = User.objects.filter(username = user).select_related('profile')
      
        if location:
            # profile= Profile.objects.filter(user_id = users[0].id)
            # location = profile[0].location
            print(f"location--->{location}")
            if location == "Uyo":
                alumni = Trainees_alumni.objects.filter(location = "Uyo")
                serializer = AlumniSerializer(alumni, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Lagos":
                alumni = Trainees_alumni.objects.filter(location = "Lagos")
                serializer = AlumniSerializer(alumni, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "PH":
                alumni = Trainees_alumni.objects.filter(location = "PH")
                serializer = AlumniSerializer(alumni, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                alumni = Trainees_alumni.objects.filter(location = "Ibadan")
                serializer = AlumniSerializer(alumni, context={'request': request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data={
                    "status": "error",
                    "message": "no valid location"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data = {
                "status": "error",
                "message": "no user found"
            }, status=status.HTTP_400_BAD_REQUEST)
                    
class GetAlumni(generics.RetrieveAPIView):
    queryset = Trainees_alumni.objects.all()
    serializer_class = AlumniSerializer

class DeleteAlumni(generics.DestroyAPIView):
    queryset = Trainees_alumni.objects.all()
    serializer_class = AlumniSerializer

class UpdateAlumni(generics.UpdateAPIView):
    queryset = Trainees_alumni.objects.all()
    serializer_class = AlumniSerializer

class TotalAlumniLocation(APIView):
    def post(self, request):
        my_users = request.data
        location = my_users["username"]
        # users = User.objects.filter(username = user).select_related('profile')
        if location:
            # profile= Profile.objects.filter(user_id = users[0].id)
            # location = profile[0].location
            if location == "General":
                alumni = Trainees_alumni.objects.all()
                total = len(alumni)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Uyo":
                alumni = Trainees_alumni.objects.filter(location = "Uyo")
                total = len(alumni)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Lagos":
                alumni = Trainees_alumni.objects.filter(location = "Lagos")
                total = len(alumni)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Abakiliki":
                alumni = Trainees_alumni.objects.filter(location = "Abakiliki")
                total = len(alumni)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "PH":
                alumni = Trainees_alumni.objects.filter(location = "PH")
                total = len(alumni)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                alumni = Trainees_alumni.objects.filter(location = "Ibadan")
                total = len(alumni)
                return Response(total, status=status.HTTP_200_OK)
            else:
                return Response(data={
                    "status": "error",
                    "message": "no valid location"
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data = {
                "status": "error",
                "message": "no user found"
            }, status=status.HTTP_400_BAD_REQUEST)
