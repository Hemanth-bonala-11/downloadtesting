from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Details(models.Model):
    firstNname=models.CharField(max_length=122)
    lastName = models.CharField(max_length=122)
    mailId=models.EmailField(max_length=122)
    phoneNumber=models.IntegerField()
    password=models.CharField(max_length=122)
    gender=models.CharField(max_length=6)
    # email_token = models.CharField(max_length=200)
    # is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.firstNname+" "+self.lastName
class Project(models.Model):
    username=models.CharField(max_length=122)
    projectname=models.CharField(max_length=122)
    dataset=models.FileField(upload_to="datasets")
    #edafile=models.FileField(upload_to="edafiles")
    #final_model=models.FileField(upload_to="final_model")







