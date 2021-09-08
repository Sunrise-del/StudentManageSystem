from django.shortcuts import render, HttpResponse


# Create your views here.

# 主界面
# request里面包含了用户所有的请求数据
def index(request):
    context = {
        "status":"未登录状态"
    }
    # return HttpResponse("哈哈")
    # return render(request, "student/index.html")
    return render(request, 'student/index.html', context)