from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=100, null=False)
    email=models.CharField(max_length=110)
    phone=models.CharField(max_length=20)
    desc=models.TextField(max_length=200, null=False)
    date=models.DateField()
 
    def __str__(self):                                      #this will show the name of the person in the admin portal
        return f"{self.name}  {self.email}"                         