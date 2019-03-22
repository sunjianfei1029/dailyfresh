#coding=utf-8

from django.shortcuts import render,redirect
from models import *
from hashlib import sha1
from django.contrib.auth import authenticate

# 跳转到注册页面
def register(request):
    return render(request,'df_user/register.html')

# 注册功能
def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname=post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')

    # 判断两次密码是否一致
    if upwd != upwd2:
        return redirect('/user/register')

    # 没有问题，创建对象
    user = UserInfo()
    user.uname=uname
    user.uemail=uemail
    # 密码加密，然后再保存到对象
    s1=sha1()
    s1.update(upwd)
    upwd3=s1.hexdigest()
    user.upwd=upwd3

    # 把user对象保存到数据科
    user.save()
    # 注册成功后调整到登录页面
    return redirect('/user/login')

# 加载登录页面
def login(request):
    return render(request,'df_user/login.html')

# 登录验证
def login_handle(request):
    # 接受用户录入的用户名和密码
    post=request.POST
    uname = post.get('username')
    upwd = post.get('pwd')

    # 校验数据
    if not all([uname,upwd]):
        context = {'errmsg':'数据不完整'}
        return render(request,'df_user/login.html',context)

    # 使用django框架自带的认证校验用户名和密码
    # user = authenticate(username=uname,password=upwd)
    # 使用传统方式验证用户经和密码
    s1 = sha1()
    s1.update(upwd)
    upwd2 = s1.hexdigest()
    try:
        user = UserInfo.objects.get(uname=uname, upwd=upwd2)
    except :
        user = None


    if user is not None:
       return render(request, 'df_index/index.html')

    else:
        # 报错
        context = {'errmsg': '用户名密码不正确'}
        return render(request, 'df_user/login.html', context)


    return render(request,'df_user/login.html',{'errmsg':'用户名或密码不正确'})
