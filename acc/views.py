from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages

def index(request):
    return render(request, "acc/index.html")

def login_user(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        user = authenticate(username=un, password=up)

        if user:
            messages.success(request, "로그인 성공!")
            login(request, user)
            return redirect("acc:index")

        else:
            messages.error(request, "계정정보가 일치하지 않습니다.")
    return render(request, "acc/login.html")

def logout_user(request):
    messages.warning(request, "로그아웃 되었습니다.")
    logout(request)
    return redirect("acc:index")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        ua = request.POST.get("uage")
        uc = request.POST.get("ucom")
        ui = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, age=ua, comment=uc, pic=ui)
            return redirect("acc:login")
        except:
            messages.error(request, "이미 존재하는 계정입니다.")
    return render(request, "acc/signup.html")

def profile(request):
    return render(request, "acc/profile.html")

def delete(request):
    pwck = request.POST.get("pwck")
    up = request.user.password
    if check_password(pwck, up):
        request.user.pic.delete()
        request.user.delete()
        return redirect("acc:login")
    else:
        messages.error(request, "잘못된 접근입니다.")    
    return redirect("acc:profile")

def update(request):
    u = request.user
    if request.method == "POST":
        up = request.POST.get("upass")
        ua = request.POST.get("uage")
        uc = request.POST.get("ucom")
        ui = request.FILES.get("upic")
        if up:
            u.set_password(up)
        u.age = ua
        u.comment = uc
        if ui:
            u.pic.delete()
            u.pic = ui
        u.save()
        login(request, u)
        return redirect("acc:profile")

    return render(request, "acc/update.html")
# Create your views here.
