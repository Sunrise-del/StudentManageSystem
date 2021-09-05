from django.db import models

# Create your models here.
# 课程表
class CourseModel(models.Model):
    course_id = models.CharField(max_length=15, verbose_name='课程ID')
    course_name = models.CharField(max_length=30,verbose_name='课程名称')
    grade = models.IntegerField(default=60,verbose_name='分数')
    class Meta():
        db_table = 'course'

    def __str__(self):
        return "课程ID： 课程： 分数： ".format(self.course_id,self.course_name,self.grade)
