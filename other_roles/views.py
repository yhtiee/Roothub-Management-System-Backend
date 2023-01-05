from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .serializers import *
from authentication.models import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

class CreateOtherRoles(generics.CreateAPIView):
    queryset = Other_roles.objects.all()
    serializer_class = OtherRolesSerializer

class RetrieveOtherRoles(generics.RetrieveAPIView):
    queryset = Other_roles.objects.all()
    serializer_class = OtherRolesSerializer

class DeleteOtherRoles(generics.DestroyAPIView):
    queryset = Other_roles.objects.all()
    serializer_class = OtherRolesSerializer

class UpdateOtherRoles(generics.UpdateAPIView):
    queryset = Other_roles.objects.all()
    serializer_class = OtherRolesSerializer

class ListAllOtherRoles(generics.ListAPIView):
    queryset = Other_roles.objects.all()
    serializer_class = OtherRolesSerializer

class GeneralTotalOtherRoles(APIView):
    def get(self, request):
        trainees = Other_roles.objects.all()
        total = len(trainees)
        return Response(total, status=status.HTTP_200_OK)

class ListOtherRolesLocation(APIView):
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
                trainees = Other_roles.objects.filter(location = "Uyo")
                serializer = OtherRolesSerializer(trainees, context={"request":request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Lagos":
                trainees = Other_roles.objects.filter(location = "Lagos")
                serializer = OtherRolesSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                trainees = Other_roles.objects.filter(location = "Ibadan")
                serializer = OtherRolesSerializer(trainees, context = {"request": request}, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            elif location == "PH":
                trainees = Other_roles.objects.filter(location = "Ibadan")
                serializer = OtherRolesSerializer(trainees, context = {"request": request}, many=True)
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

class TotalOtherRolesLocation(APIView):
    def post(self, request):
        my_users = request.data
        location= my_users["username"]
        # logged_user = User.objects.filter(username = user).select_related('profile')
        if location:
            # profile= Profile.objects.filter(user_id = logged_user[0].id)
            # location = profile[0].location
            if location == "General":
                trainees = Other_roles.objects.all()
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Uyo":
                trainees = Other_roles.objects.filter(location = "Uyo")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Lagos":
                trainees = Other_roles.objects.filter(location = "Lagos")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Abakiliki":
                trainees = Other_roles.objects.filter(location = "Abakiliki")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                trainees = Other_roles.objects.filter(location = "Ibadan")
                total = len(trainees)
                return Response(total, status=status.HTTP_200_OK)
            elif location == "PH":
                trainees = Other_roles.objects.filter(location = "PH")
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