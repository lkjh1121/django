from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse("<h1>guestbook</h1>")
    #html 문서와 파이썬 데이터를 연동해서 하나의 html파일을 만든다 
    return render(request, "guestbook/index.html")

def write(request): #guestbook_write.html 
    return render(request, "guestbook/guestbook_write.html")

def save(request): #데이터 읽어와서 저장하기 
    title = request.POST["title"]
    writer = request.POST["writer"]
    contents = request.POST["contents"]
    result = f"{title}<br/>{writer}<br/>{contents}<br/>"
    return HttpResponse(result)


def add(request):
    return render(request, "guestbook/add.html")

def add_result(request, x, y, oper):
    x = int(x)
    y = int(y)
    if oper=="1":
        result = f"<h1>{x}+{y}={x+y}</h1>"
    elif oper=="2":
        result = f"<h1>{x}-{y}={x-y}</h1>"
    elif oper=="3":
        result = f"<h1>{x}*{y}={x*y}</h1>"
    else: 
        result = f"<h1>{x}/{y}={x/y}</h1>"
    
    return HttpResponse(result)






