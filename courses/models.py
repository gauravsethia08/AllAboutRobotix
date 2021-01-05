from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_title = models.CharField(max_length=20, unique=True, choices=[('Computer Vision', 'Computer Vision'), ('Controls', 'Controls'), ('Kinematics', 'Kinematics')])
    course_descr = models.TextField()
    no_modules = models.IntegerField()
    course_fee = models.FloatField()
    course_cover_img = models.ImageField(upload_to = 'pics')

    def __str__(self):
        return self.course_title

class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    moduel_no = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module_desc = models.TextField()
    no_text = models.IntegerField()
    no_videos = models.IntegerField()
    no_assignment = models.IntegerField()

    def __str__(self):
        text = self.course.course_title + " - " + str(self.moduel_no)
        return text

class ModuleContent(models.Model):
    content_id = models.AutoField(primary_key=True)
    content_no = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    content_type = models.CharField(max_length=20,choices=[('Text', 'Text'), ('Video', 'Video'), ('Assignment', 'Assignment')])
    content_link = models.CharField(max_length=200)
    time_req = models.FloatField()

    def __str__(self):
        text = self.course.course_title + "-" + str(self.module.moduel_no) + "-" + str(self.content_no)
        return text

