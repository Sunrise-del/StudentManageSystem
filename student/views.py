from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from student.models import StudentPwd, StudentInfo, Course


# 检查是否登录
# 先调用check_login(add)，返回inner函数，此时调用add就相当于调用装饰器中的inner函数，参数是add的参数
def check_login(func):
    def inner(*args, **kwargs):
        # 判断是否登录 如果未登录，需要先登录
        if "user" not in args[0].session.keys():
            print(args[0])
            context = {
                "status": "你好，若想使用该系统，请登录"
            }
            return render(args[0], 'student/login.html', context)
        # 如果已登录，返回add函数，继续执行往下执行add函数
        return func(*args, **kwargs)

    return inner


# 主界面
@check_login
def index(request):
    stu_info = StudentInfo.objects.all()
    return render(request, 'student/index.html', {"stu_info": stu_info})


# 注册页面
# request里面包含了用户所有的请求数据
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
                return redirect('/student/index/')
            else:
                context = {
                    'status': '密码错误，请重新输入'
                }
                return render(request, 'student/login.html', context)
    else:
        return render(request, 'student/login.html')


# 退出登录
def logout(request):
    del request.session['user']
    return render(request, 'student/login.html')


# 增加数据
@check_login
def add(request):
    if request.method == "POST":
        # 获取用户浏览器中输入的数据
        stu_id = request.POST.get('stu_id')
        stu_name = request.POST.get('stu_name')
        stu_faculty = request.POST.get("stu_faculty")
        stu_major = request.POST.get("stu_major")
        # 将浏览器中的数据赋值至数据库
        StudentInfo.objects.create(stu_id=stu_id, stu_name=stu_name, stu_faculty=stu_faculty, stu_major=stu_major)
        return redirect('/student/index/')
    else:
        return render(request, 'student/add.html')


# 删除学生信息
@check_login
def delete(request):
    stu_id = request.GET.get("stu_id")
    StudentInfo.objects.filter(stu_id=stu_id).delete()
    return redirect('/student/index/')

# 查询学生信息
@check_login
def select(request):
    if request.method == "POST":
        stu_id = request.POST.get("stu_id")
        if StudentInfo.objects.filter(stu_id=stu_id):
            print("哈哈哈哈哈")
            stu_select_info = StudentInfo.objects.filter(stu_id=stu_id)
            return render(request, 'student/select.html', {"stu_select_info": stu_select_info})
        else:
            context = {
                'msg': True,
                'txt': "你输入的学生不存在，请重新输入"
            }
            return render(request, 'student/select.html', context)
    else:
        context = {
            'msg': True,
        }
        return render(request, 'student/select.html', context)


# 修改学生信息
@check_login
def update(request):
    if request.method == "POST":
        stu_id = request.GET.get('stu_id')
        stu_name = request.POST.get("stu_name")
        stu_faculty = request.POST.get("stu_faculty")
        stu_major = request.POST.get("stu_major")
        StudentInfo.objects.filter(stu_id=stu_id).update(stu_name=stu_name, stu_faculty=stu_faculty,
                                                         stu_major=stu_major)
        return redirect('/student/index/')
    else:
        stu_id = request.GET.get('stu_id')
        stu_info = StudentInfo.objects.get(stu_id=stu_id)
        return render(request, 'student/update.html', {"stu_info": stu_info})
