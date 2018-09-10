from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        print(request.POST.get('expire_time', None))
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        print(user, pwd)
        if user == 'root' and pwd == '123':
            # 生成随机字符串
            # 写到用户浏览器cookie
            # 保存到session中
            # 在随机字符串对应的字典中设置相关内容
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('expire_time', None) == 'on':
                request.session.set_expiry(10)

            return redirect('/index/')

    else:
        return render(request, 'login.html')


def index(request):
    if request.session.get('is_login', None):
        v = request.session['username']
        # return HttpResponse(v)
        return render(request, 'index.html', {'username': request.session['username']})
        # 另一种写法
        # return render(request, 'index.html')
        # html中直接使用{{ request.session.username }}
    else:
        return HttpResponse("输入错误")


def logout(request):
    request.session.clear()
    return redirect('/login/')


def test(request):
    print("-------------->: testtttttttttttttttttttt")
    return HttpResponse("OK")

