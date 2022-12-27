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

class CreateNYSC(generics.CreateAPIView):
    queryset = NYSC.objects.all()
    serializer_class = NYSCSerializer

class RetrieveNYSC(generics.RetrieveAPIView):
    queryset = NYSC.objects.all()
    serializer_class = NYSCSerializer

class DeleteNYSC(generics.DestroyAPIView):
    queryset = NYSC.objects.all()
    serializer_class = NYSCSerializer

class UpdateNYSC(generics.UpdateAPIView):
    queryset = NYSC.objects.all()
    serializer_class = NYSCSerializer

class ListAllNYSC(generics.ListAPIView):
    queryset =NYSC.objects.all()
    serializer_class = NYSCSerializer

class GeneralTotalNYSC(APIView):
    def get(self, request):
        trainees = NYSC.objects.all()
        total = len(trainees)
        return Response(total, status=status.HTTP_200_OK)

class ListNYSClocation(APIView):
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
                trainees = NYSC.objects.filter(location = "Uyo")
                serializer = NYSCSerializer(trainees, context={"request":request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Lagos":
                trainees = NYSC.objects.filter(location = "Lagos")
                serializer = NYSCSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                trainees = NYSC.objects.filter(location = "Ibadan")
                serializer = NYSCSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "PH":
                trainees = NYSC.objects.filter(location = "Ibadan")
                serializer = NYSCSerializer(trainees, context = {"request": request}, many=True)
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

class TotalNYSCLocation(APIView):
    def post(self, request):
        my_users = request.data
        location = my_users["username"]
        # logged_user = User.objects.filter(username = user).select_related('profile')
        if location:
            # profile= Profile.objects.filter(user_id = logged_user[0].id)
            # location = profile[0].location
            if location == "Uyo":
                trainees = NYSC.objects.filter(location = "Uyo")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Lagos":
                trainees = NYSC.objects.filter(location = "Lagos")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                trainees = NYSC.objects.filter(location = "Ibadan")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "PH":
                trainees = NYSC.objects.filter(location = "Ibadan")
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