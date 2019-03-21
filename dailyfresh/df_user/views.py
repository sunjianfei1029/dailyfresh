#coding=utf-8

from django.shortcuts import render,redirect
from models import *
from hashlib import sha1

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