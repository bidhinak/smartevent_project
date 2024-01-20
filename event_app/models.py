from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import DO_NOTHING


# Create your models here.
class Login(AbstractUser):
    is_teacher=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)


class teacher(models.Model):
    DEPARTMENT = (
        ('CS', 'Computer science'),
        ('BCA', 'computer application'),
        ('FT', 'Food technology'),
        ('Physics', 'physics'),
        ('Maths','maths')
    )

    name1=models.ForeignKey(Login,on_delete=models.CASCADE)
    teacher_name=models.CharField(max_length=50)
    staff_id=models.IntegerField()
    email=models.EmailField()
    phone_no=models.CharField(max_length=10)
    department=models.CharField(max_length=30,choices=DEPARTMENT)

    def __str__(self):
        return self.teacher_name


class student(models.Model):
    DEPARTMENT = (
        ('CS', 'Computer science'),
        ('BCA', 'computer application'),
        ('FT', 'Food technology'),
        ('Physics', 'physics'),
        ('Maths','maths')
    )

    name2=models.ForeignKey(Login,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=50)
    admission_no=models.CharField(max_length=10)
    email=models.EmailField()
    phone_no=models.CharField(max_length=10)
    department=models.CharField(max_length=30,choices=DEPARTMENT)

class club(models.Model):
    club_name=models.CharField(max_length=50)
    staff_incharge=models.ForeignKey(teacher,on_delete=models.CASCADE)
    club_logo=models.FileField(upload_to="images/")

class event(models.Model):
    club_name=models.ForeignKey(club,on_delete=models.CASCADE)
    event_name=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    event_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()

class notification(models.Model):
     date=models.DateField()
     description=models.TextField()

class Feedback(models.Model):
    user=models.ForeignKey(Login,on_delete=DO_NOTHING)
    date=models.DateField(auto_now=True)
    feedback=models.TextField()
    reply=models.TextField(blank=True,null=True,)