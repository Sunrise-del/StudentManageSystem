from django.db import models


# Create your models here.
# 课程表
class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True, verbose_name='课程ID')
    course_name = models.CharField(max_length=30, verbose_name='课程名称')
    grade = models.IntegerField(default=60, verbose_name='分数')

    # 模型元数据，可以将不是字段的所有数据放在这个内部类中。
    # class Meta():
    #     db_table = 'student'

    def __str__(self):
        return "课程ID： 课程： 分数： ".format(self.course_id, self.course_name, self.grade)


class StudentInfo(models.Model):
    stu_id = models.BigAutoField(primary_key=True, verbose_name="学生ID")
    stu_name = models.CharField(max_length=30, verbose_name="学生姓名")
    stu_faculty = models.CharField(max_length=20, verbose_name="院系")
    stu_major = models.CharField(max_length=30, verbose_name="专业")


class StudentPwd(models.Model):
    stu_id = models.BigAutoField(primary_key=True, verbose_name="学生ID")
    username = models.CharField(max_length=10, verbose_name="用户名")
    password = models.CharField(max_length=10, verbose_name="密码")

