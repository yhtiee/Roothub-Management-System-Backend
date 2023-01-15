from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from authentication.models import *
from django.contrib.auth.models import User
from interns.models import *
from trainees.models import *

# Create your views here.
class PopularCoursesLocation(APIView):
    def post(self, request):
        my_users = request.data
        location = my_users["username"]
        generalData = {"Backend Web Development":0,"Frontend Web Development":0, "Visual Communications":0, "UI/UX":0, "Data Analysis":0, "App Developement":0, "Computer Basics":0, "Video Editing":0, "Photography":0, "Content Development":0}
        uyoData = {"Backend Web Development":0,"Frontend Web Development":0, "Visual Communications":0, "UI/UX":0, "Data Analysis":0, "App Developement":0, "Computer Basics":0, "Video Editing":0, "Photography":0, "Content Development":0}
        abakilikiData = {"Backend Web Development":0,"Frontend Web Development":0, "Visual Communications":0, "UI/UX":0, "Data Analysis":0, "App Developement":0, "Computer Basics":0, "Video Editing":0, "Photography":0, "Content Development":0}
        lagosData = {"Backend Web Development":0,"Frontend Web Development":0, "Visual Communications":0, "UI/UX":0, "Data Analysis":0, "App Developement":0, "Computer Basics":0, "Video Editing":0, "Photography":0, "Content Development":0}
        phData = {"Backend Web Development":0,"Frontend Web Development":0, "Visual Communications":0, "UI/UX":0, "Data Analysis":0, "App Developement":0, "Computer Basics":0, "Video Editing":0, "Photography":0, "Content Development":0}
        ibadanData = {"Backend Web Development":0,"Frontend Web Development":0, "Visual Communications":0, "UI/UX":0, "Data Analysis":0, "App Developement":0, "Computer Basics":0, "Video Editing":0, "Photography":0, "Content Development":0}
        if location:
            if location == "General":
                internData = Interns.objects.all().values()
                traineesData = Trainees_general.objects.all().values()
                totalData = []
                for x in internData:
                    if x in totalData:
                        pass
                    else:
                        totalData.append(x)
                for a in traineesData:
                    if a in totalData:
                        pass
                    else:
                        totalData.append(a)
                for data in totalData:
                    course = data["course_learning"]
                    if course in generalData:
                        generalData[course] += 1
                    else:
                        generalData[course] = 1
                return Response(generalData, status=status.HTTP_200_OK)
            elif location == "Uyo":
                internData = Interns.objects.filter(location = location).values()
                traineesData = Trainees_general.objects.filter(location = location).values()
                totalData = []
                for x in internData:
                    if x in totalData:
                        pass
                    else:
                        totalData.append(x)
                for a in traineesData:
                    if a in totalData:
                        pass
                    else:
                        totalData.append(a)
                for data in totalData:
                    course = data["course_learning"]
                    if course in uyoData:
                        uyoData[course] += 1
                    else:
                        uyoData[course] = 1
                return Response(uyoData, status=status.HTTP_200_OK)
            elif location == "Abakiliki":
                internData = Interns.objects.filter(location = location).values()
                traineesData = Trainees_general.objects.filter(location = location).values()
                totalData = []
                for x in internData:
                    if x in totalData:
                        pass
                    else:
                        totalData.append(x)
                for a in traineesData:
                    if a in totalData:
                        pass
                    else:
                        totalData.append(a)
                for data in totalData:
                    course = data["course_learning"]
                    if course in abakilikiData:
                        abakilikiData[course] += 1
                    else:
                        abakilikiData[course] = 1
                return Response(abakilikiData, status=status.HTTP_200_OK)
            elif location == "Lagos":
                internData = Interns.objects.filter(location = location).values()
                traineesData = Trainees_general.objects.filter(location = location).values()
                totalData = []
                for x in internData:
                    if x in totalData:
                        pass
                    else:
                        totalData.append(x)
                for a in traineesData:
                    if a in totalData:
                        pass
                    else:
                        totalData.append(a)
                for data in totalData:
                    course = data["course_learning"]
                    if course in lagosData:
                        lagosData[course] += 1
                    else:
                        lagosData[course] = 1
                return Response(lagosData, status=status.HTTP_200_OK)
            elif location == "Ibadan":
                internData = Interns.objects.filter(location = location).values()
                traineesData = Trainees_general.objects.filter(location = location).values()
                totalData = []
                for x in internData:
                    if x in totalData:
                        pass
                    else:
                        totalData.append(x)
                for a in traineesData:
                    if a in totalData:
                        pass
                    else:
                        totalData.append(a)
                for data in totalData:
                    course = data["course_learning"]
                    if course in ibadanData:
                        ibadanData[course] += 1
                    else:
                        ibadanData[course] = 1
                return Response(ibadanData, status=status.HTTP_200_OK)
            elif location == "PH":
                internData = Interns.objects.filter(location = location).values()
                traineesData = Trainees_general.objects.filter(location = location).values()
                totalData = []
                for x in internData:
                    if x in totalData:
                        pass
                    else:
                        totalData.append(x)
                for a in traineesData:
                    if a in totalData:
                        pass
                    else:
                        totalData.append(a)
                for data in totalData:
                    course = data["course_learning"]
                    if course in phData:
                        phData[course] += 1
                    else:
                        phData[course] = 1
                return Response(phData, status=status.HTTP_200_OK)
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