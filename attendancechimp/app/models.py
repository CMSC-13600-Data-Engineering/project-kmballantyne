from distutils.command import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your models here.

class Person(models.Model):
    auto_id = models.AutoField(primary_key=True)
    
    instructor = models.BooleanField(null=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
def create_user(name, email, password, is_instructor):
    
    user = User.objects.create_user(name, email, password)
    user.save()
    
    uni_per = Person(is_instructor=is_instructor, user=user)
    uni_per.save()
    
    return user, uni_per

# class StudentUsers(models.Model):
#    studentID = models.CharField(max_length=256, primary_key=True)
#    first_name = models.CharField(max_length=256)
#    last_name = models.CharField(max_length=256)
   
# class FacultyUsers(models.Model):
#     facultyID = models.CharField(max_length=256, primary_key=True)
#     first_name = models.CharField(max_length=256)
#     last_name = models.CharField(max_length=256)

class Course(models.Model):
    
    auto_id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=256)
    
    faculty = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    class_begin = models.TimeField()
    class_end = models.TimeField()
    
    mon_class = models.BooleanField(default=False)
    tues_class = models.BooleanField(default=False)
    wed_class = models.BooleanField(default=False)
    thurs_class = models.BooleanField(default=False)
    fri_class = models.BooleanField(default=False)
    
    # number = models.CharField(max_length=5)
    # students = models.ManyToManyField(Person)
    
def create_course(name, instructor, days, start, end):
    
    course = Course(name=name, instructor=instructor, class_begin=start, class_end=end)
    
    for d in days:
        if d == "M":
            course.mon_class = True
        if d == "Tu":
            course.tues_class = True
        if d == "W":
            course.wed_class = True
        if d == "Th":
            course.thurs_class = True
        if d == "F":
            course.fri_class = True
            
    course.save()
    
    return course
    
class Lecture(models.Model):
    date = models.DateField()
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)

# class HelperCourseStudent(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     student = models.ForeignKey(StudentUsers, on_delete=models.CASCADE)
    
class QRcode(models.Model):
    
    auto_id = models.AutoField(primary_key=True)
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    qrcode = models.CharField(max_length=32)
    
    def save(self, *args, **kargs):
        
        self.code = get_random_string(length=32)
        super(QRcode, self).save(*args, **kargs)
        
def create_qrcode(course):
    
    qrcode = QRcode(course=course)
    qrcode.save()
    
    return qrcode

class QRCodeUpload(models.Model):
    
    auto_id = models.AutoField(primary_key=True)
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    student = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    qr_image = models.ImageField(upload_to ='data')
    
    uploaded = models.DateTimeField(auto_now_add=True)
    
def process_upload(course, student, image):
    upload = QRCodeUpload(course=course, student=student, image=image)
    upload.save()
    return upload
    
    # dates = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    # student = models.ManyToManyField(HelperCourseStudent, through=HelperCourseStudent)
    # courses = models.ManyToManyField(HelperCourseStudent, through=HelperCourseStudent)
    # qrcode = models.ImageField(upload_to='images/')