from django.db import models

# Create your models here.
class Trainees_general(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    course_learning = models.CharField(max_length=50)
    course_duration = models.CharField(max_length=50)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=50)
    training_fee = models.DecimalField(max_digits=10, decimal_places=2, default=100000.00)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)
    profile_picture = models.ImageField(upload_to="users", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.other_names}, {self.phone_number}, {self.course_duration}, {self.location}, {self.course_learning}, {self.balance}, {self.amount_paid}, {self.registrationDate}, {self.email}"