from django.db import models

# Create your models here.
class Other_roles(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone_number = models.CharField(max_length=11)
    role = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    account_number = models.CharField(max_length=15)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)
    profile_picture = models.ImageField(upload_to="users", null=True, blank=True)


    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.other_names}, {self.phone_number}, {self.role}, {self.location}, {self.bank}, {self.account_number}, {self.registrationDate}, {self.email}"