from django.db import models


# Define Teacher model
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
