from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30,null=False)
    description = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null = False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="files/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to="files/resource")
    length = models.IntegerField(null=False)

class CourseProperty(models.Model):
    description = models.CharField(max_length=100)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)

    class Meta:
        abstract = True

          
class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

class Video(models.Model):
    title = models.CharField(max_length=100,null=False)
    course = models.ForeignKey(Course,null=False,on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=50,null=False)
    is_preview = models.BooleanField(default=False)

