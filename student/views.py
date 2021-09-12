from django.shortcuts import render, HttpResponse

# Create your views here.

from student.models import StudentPwd, StudentInfo, Course


# 主界面
# request里面包含了用户所有的请求数据
def index(request):
    if "user" in request.session.keys():
        context = {
            'length': 1
        }
        return render(request, 'student/index.html', context)
    else:
        context = {
            "status": "游客"
        }
        return render(request, 'student/index.html', context)


# 注册页面
def sign_up(request):
    if request.method == "POST":
        # 获取用户浏览器中输入的数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        if len(StudentPwd.objects.filter(username=username)):
            context = {
                'status': '该用户名已存在，请重新输入'
            }
            return render(request, 'student/sign_up.html', context)
        # 将浏览器中的数据赋值至数据库
        StudentPwd.objects.create(username=username, password=password)
        # stu_pwd = StudentPwd()
        # stu_pwd.username = username
        # stu_pwd.password = password
        # stu_pwd.save()
        context = {
            "status": "注册成功，请登录"
        }
        return render(request, 'student/login.html', context)
    else:
        return render(request, 'student/sign_up.html')


# 登录页面
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not all([username, password]):
            context = {
                "status": "您还有未输入的选项，请重新输入"
            }
            return render(request, 'student/login.html', context)
        else:
            if StudentPwd.objects.filter(username=username, password=password):
                # request.session['username'] = username
                # 用以下方法，将用户的信息存放到session中，session在中间件中是默认启用的
                request.session['user'] = {
                    'username': username,
                    'password': password
                }
                context = {
                    'status': username,
                    'length': 1
                }
                return render(request, 'student/index.html', context)
            else:
                context = {
                    'status': '密码错误，请重新输入'
                }
                return render(request, 'student/login.html', context)
    else:
        context = {
            'status': '你好，若想使用该系统，请登录',
        }
        return render(request, 'student/login.html', context)


# 退出登录
def logout(request):
    del request.session['user']
    return render(request, 'student/index.html')


# 增加数据
def add(request):
    if request.method == "POST":
        # 获取用户浏览器中输入的数据
        stu_id = request.POST.get('stu_id')
        stu_name = request.POST.get('stu_name')
        stu_faculty = request.POST.get("stu_faculty")
        stu_major = request.POST.get("stu_major")

        # 将浏览器中的数据赋值至数据库
        StudentInfo.objects.create(stu_id=stu_id, stu_name=stu_name, stu_faculty=stu_faculty, stu_major=stu_major)
        # stu_data = StudentInfo()
        # stu_data.stu_name = stu_name
        # stu_data.stu_faculty = stu_faculty
        # stu_data.stu_major = stu_major
        # stu_data.save()
        context = {
            "txt": "添加学生信息成功",
            "length": 1,
        }
        return render(request, 'student/index.html', context)
    else:
        return render(request, 'student/add.html')


# 删除学生信息
def delete(request):
    if request.method == "POST":
        stu_id = request.POST.get("stu_id")
        # filter查询字段时 如果不存在，返回false，不会报错。get会报错
        if StudentInfo.objects.filter(stu_id=stu_id):
            StudentInfo.objects.get(stu_id=stu_id).delete()
            context = {
                "txt": '删除学生信息成功',
                'length': 1,
            }
            return render(request, 'student/index.html', context)
        else:
            context = {
                'txt': "你输入的学生姓名不存在，请重新输入"
            }
            return render(request, 'student/delete.html', context)
    else:
        return render(request, 'student/delete.html')


# 查询学生信息
def select(request):
    if request.method == "POST":
        stu_id = request.POST.get("stu_id")
        if StudentInfo.objects.filter(stu_id=stu_id):
            stu_data = StudentInfo.objects.get(stu_id=stu_id)
            stu_name = stu_data.stu_name
            stu_faculty = stu_data.stu_faculty
            stu_major = stu_data.stu_major
            context = {
                'msg': True,
                'stu_id':stu_id,
                'stu_name': stu_name,
                'stu_faculty': stu_faculty,
                'stu_major': stu_major,
                'status': '查询结果如下:'
            }
            return render(request, 'student/select.html', context)
        else:
            context = {
                'txt': "你输入的学生姓名不存在，请重新输入"
            }
            return render(request, 'student/select.html', context)
    else:
        return render(request, 'student/select.html')


# 修改学生信息
def update(request):
    if request.method == "POST":
        stu_id = request.POST.get("stu_id")
        stu_name = request.POST.get("stu_name")
        stu_faculty = request.POST.get("stu_faculty")
        stu_major = request.POST.get("stu_major")
        if StudentInfo.objects.filter(stu_id=stu_id):
            StudentInfo.objects.filter(stu_id=stu_id).update(stu_name=stu_name, stu_faculty=stu_faculty, stu_major=stu_major)
            context = {
                'stu_id': stu_id,
                'stu_name': stu_name,
                'stu_faculty': stu_faculty,
                'stu_major': stu_major,
                'status': '修改成功！结果如下：',
                'msg': True
            }
            return render(request, 'student/select.html', context)
    else:

        return render(request, 'student/update.html')
