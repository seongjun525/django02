from django.shortcuts import redirect, render
from .models import Board, Reply
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages

def index(request):
    cate = request.GET.get("cate", "")
    kw = request.GET.get("kw", "")

    if kw:
        if cate == "sub":
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == "wri":
            try:
                from acc.models import User
                u = User.objects.get(username=kw)
                b = Board.objects.filter(writer=u)
            except:
                b = Board.objects.none()
        elif cate == "con":
            b = Board.objects.filter(content__contains=kw)
        else:
            messages.error(request, "잘못된 접근입니다.") 
            b = Board.objects.all()
    else:
        b = Board.objects.all()
    b = b.order_by('-likey')
    page = request.GET.get("page", 1)
    pag = Paginator(b, 10)
    obj = pag.get_page(page)
    context = {
        "bset" : obj,
        "cate" : cate,
        "kw" : kw

    }
    return render(request, "board/index.html", context)

def detail(request, bpk):
    b = Board.objects.get(id=bpk)
    r = b.reply_set.all()
    context = {
        "b" : b,
        "rset" : r
    }
    return render(request, "board/detail.html", context)

def delete(request, bpk):
    b = Board.objects.get(id=bpk)
    if request.user == b.writer:
        b.delete()
    else:
        messages.error(request, "삭제에 실패하였습니다.")
    return redirect("board:index")

def create(request):
    if request.method == "POST":
        us = request.POST.get("usub")
        uc = request.POST.get("ucon")
        Board(subject=us,content=uc, writer=request.user, pubdate=timezone.now()).save()
        return redirect("board:index")
    return render(request, "board/create.html")

def update(request, bpk):
    b = Board.objects.get(id=bpk)

    if request.user != b.writer:
        messages.error(request, "잘못된 접근입니다.")
        return redirect("board:index")
    else:   
        if request.method == "POST":
            us = request.POST.get("usub")
            uc = request.POST.get("ucon")
            b.subject = us
            b.content = uc
            b.save()
            return redirect("board:detail", bpk)
    context = {
        "b" : b
    }
    return render(request, "board/update.html", context)

def creply(request, bpk):
    c = request.POST.get("com")
    b = Board.objects.get(id=bpk)
    Reply(b=b, replyer=request.user, comment=c, pubdate=timezone.now()).save()
    return redirect("board:detail", bpk)

def deply(request, bpk,rpk):
    r = Reply.objects.get(id=rpk)
    if request.user == r.replyer:
        messages.error(request, "잘못된 접근입니다.")
    r.delete()
    return redirect("board:detail", bpk)

def likey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.add(request.user)
    return redirect("board:detail", bpk)

def unlikey(request, bpk):
    b = Board.objects.get(id=bpk)
    b.likey.remove(request.user)
    return redirect("board:detail", bpk)
# Create your views here.