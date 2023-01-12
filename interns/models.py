from django.db import models

# Create your models here.
class Interns(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    course_learning = models.CharField(max_length=50, default="Frontend Web Development")
    course_duration = models.CharField(max_length=50, default="3 Months")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=20000.00)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=80000.00)
    training_fee = models.DecimalField(max_digits=10, decimal_places=2, default=100000.00)
    location = models.CharField(max_length=50)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)
    profile_picture = models.ImageField(upload_to="users", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.other_names}, {self.phone_number}, {self.location}, {self.attached_area} {self.registrationDate}, {self.email}"