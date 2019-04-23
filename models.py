from django.conf import settings
from django.db import models
#from django.utils import timezone

COURSE_CHOICES = (
    ('B.T','B.Tech'),
    ('M.T','M.Tech'),
    ('B.B','BBA'),
    ('M.B','MBA'),
    ('B.S','Basic Science'),
    ('L','Law'),
    )

BLOCK_CHOICES = (
    ('N.B','NEW BLOCK'),
    ('N.B.X','NBX'),
    ('M.B','MESS BLOCK'),
    ('M.M','MM'),
    ('I.T','IT'),
    ('I.H','IH'),
    )

WHERETO_CHOICES = (
    ('LG','LG'),
    ('P','PARENT'),
    ('O','OTHER'),
   
    )

class Registration(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    course = models.CharField(max_length=20,choices=COURSE_CHOICES)
    year = models.IntegerField()
    srn = models.CharField(max_length=14)
    gname = models.CharField(max_length=20)
    gaddress = models.TextField()
    gmobile = models.BigIntegerField()
    password = models.CharField(max_length=20)
    

class LeaveApplication(models.Model):
    name = models.CharField(max_length=30)
    block = models.CharField(max_length = 20, choices = BLOCK_CHOICES)
    room_no = models.IntegerField()
    whereto = models.CharField(max_length = 20, choices = WHERETO_CHOICES)
    stu_mob_no = models.BigIntegerField()
    parent_name = models.CharField(max_length=30)
    par_mob_no = models.BigIntegerField()
    leaving_date = models.DateTimeField(blank=True,null=True)
    arriving_date = models.DateTimeField(blank=True,null=True)


class Complaint(models.Model):
    name = models.CharField(max_length = 30)
    mobile_no = models.BigIntegerField()
    email_id = models.EmailField()
    block = models.CharField(max_length = 20, choices = BLOCK_CHOICES)
    room_no = models.IntegerField()
    subject = models.CharField(max_length = 30)
    complaint = models.TextField()


