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

class CreateTrainer(generics.CreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class RetrieveTrainer(generics.RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class DeleteTrainer(generics.DestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class UpdateTrainer(generics.UpdateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class ListAllTrainer(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class GeneralTotalTriainer(APIView):
    def get(self, request):
        trainees = Trainer.objects.all()
        total = len(trainees)
        return Response(total, status=status.HTTP_200_OK)

class ListTrainerLocation(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        user_data = request.data
        myUser = request.user
        print(f"request----> {myUser}")
        location = user_data["username"]
        # users = User.objects.filter(username = user).select_related('profile')

        if location:
            # profile= Profile.objects.filter(user_id = users[0].id)
            # location = profile[0].location
            if location == "Uyo":
                trainees = Trainer.objects.filter(location = "Uyo")
                serializer = TrainerSerializer(trainees, context={"request":request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Lagos":
                trainees = Trainer.objects.filter(location = "Lagos")
                serializer = TrainerSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                trainees = Trainer.objects.filter(location = "Ibadan")
                serializer = TrainerSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "PH":
                trainees = Trainer.objects.filter(location = "Ibadan")
                serializer = TrainerSerializer(trainees, context = {"request": request}, many=True)
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

class TotalTrainerLocation(APIView):
    def post(self, request):
        my_users = request.data
        location = my_users["username"]
        # print(f"location--->{location}")
        # logged_user = User.objects.filter(username = user).select_related('profile')
        if location:
            # profile= Profile.objects.filter(user_id = logged_user[0].id)
            # location = profile[0].location
            if location == "General":
                trainees = Trainer.objects.all()
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Uyo":
                trainees = Trainer.objects.filter(location = "Uyo")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Lagos":
                trainees = Trainer.objects.filter(location = "Lagos")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                trainees = Trainer.objects.filter(location = "Ibadan")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Abakiliki":
                trainees = Trainer.objects.filter(location = "Abakiliki")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "PH":
                trainees = Trainer.objects.filter(location = "Ibadan")
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