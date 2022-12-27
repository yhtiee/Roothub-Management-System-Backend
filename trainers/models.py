from django.db import models

# Create your models here.

class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    qualification = models.CharField(max_length=100)
    course_teaching = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    account_number = models.CharField(max_length=15)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)
    profile_picture = models.ImageField(upload_to="users", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.other_names}, {self.phone_number}, {self.qualification}, {self.location}, {self.course_teaching}, {self.bank}, {self.account_number}, {self.registrationDate}, {self.email}"