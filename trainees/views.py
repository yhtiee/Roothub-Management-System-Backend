from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import *
from authentication.models import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CreateTrainee(generics.CreateAPIView):
    queryset = Trainees_general.objects.all()
    serializer_class = TraineeSerializer

class RetrieveTrainee(generics.RetrieveAPIView):
    queryset = Trainees_general.objects.all()
    serializer_class = TraineeSerializer

class DeleteTrainee(generics.DestroyAPIView):
    queryset = Trainees_general.objects.all()
    serializer_class = TraineeSerializer

class UpdateTrainee(generics.UpdateAPIView):
    queryset = Trainees_general.objects.all()
    serializer_class = TraineeSerializer

class ListAllTrainee(generics.ListAPIView):
    queryset = Trainees_general.objects.all()
    serializer_class = TraineeSerializer

class GeneralTotalTriainee(APIView):
    def get(self, request):
        trainees = Trainees_general.objects.all()
        total = len(trainees)
        return Response(total, status=status.HTTP_200_OK)

class ListTraineeLocation(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        user_data = request.data
        myUser = request.user
        print(f"request----> {myUser}")
        location= user_data["username"]
        # users = User.objects.filter(username = user).select_related('profile')

        if location:
            # profile= Profile.objects.filter(user_id = users[0].id)
            # location = profile[0].location
            if location == "Uyo":
                trainees = Trainees_general.objects.filter(location = "Uyo")
                serializer = TraineeSerializer(trainees, context={"request":request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Lagos":
                trainees = Trainees_general.objects.filter(location = "Lagos")
                serializer = TraineeSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                trainees = Trainees_general.objects.filter(location = "Ibadan")
                serializer = TraineeSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "PH":
                trainees = Trainees_general.objects.filter(location = "PH")
                serializer = TraineeSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    data={
                        "status": "error",
                        "msg": "no valid location found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    data={
                        "status": "error",
                        "msg": "no valid user found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

class TotalTraineeLocation(APIView):
    def post(self, request):
        my_users = request.data
        location= my_users["username"]
        # logged_user = User.objects.filter(username = user).select_related('profile')
        if location:
            # profile= Profile.objects.filter(user_id = logged_user[0].id)
            # location = profile[0].location
            if location == "General":
                trainees = Trainees_general.objects.all()
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Uyo":
                trainees = Trainees_general.objects.filter(location = "Uyo")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Lagos":
                trainees = Trainees_general.objects.filter(location = "Lagos")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Abakiliki":
                trainees = Trainees_general.objects.filter(location = "Abakiliki")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                trainees = Trainees_general.objects.filter(location = "Ibadan")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "PH":
                trainees = Trainees_general.objects.filter(location = "PH")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            else:
                return Response(
                    data={
                        "status": "error",
                        "msg": "no valid location found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                    data={
                        "status": "error",
                        "msg": "no valid user found"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )