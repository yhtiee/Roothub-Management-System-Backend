from django.db import models

# Create your models here.
class Trainees_alumni(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    location = models.CharField(max_length=50)
    registrationDate = models.DateField("Registration Date")
    completionDate = models.DateField("Completion Date")
    profile_picture = models.ImageField(upload_to="users", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.other_names}, {self.phone_number}, {self.course_duration}, {self.location}, {self.course}, {self.completionDate}, {self.email}"