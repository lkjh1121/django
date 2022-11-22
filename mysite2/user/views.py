from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome my home</h1>")

#GET 방식1
#/user/info?username=임꺽정&phone=010-0000-0001
def info(request):
    username = request.GET["username"]
    phone = request.GET["phone"]
    msg = f"username:{username}, phone:{phone}"
    return HttpResponse(msg)

#새로운 방식 GET방식 2
#user/info2/장길산/010-0000-3333
#urls.py 파일에서 /user/info2/<username>/<phone>
def info2(request, username, phone):
    msg = f"*** username:{username}, phone:{phone} ***"
    return HttpResponse(msg)

#user/add/4/5      => 4 + 5 = 9
#user/sub?x=5&y=8  => 5-8=-3 

#user/add/4/5   
def add(request, x, y):
    x = int(x)
    y = int(y)
    msg = f"<h1 style='color:red'>{x}+{y}={x+y}</h1>"
    return HttpResponse(msg)

#user/sub?x=5&y=8 
def sub(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    msg = f"<h1 style='color:red'>{x}-{y}={x-y}</h1>"
    return HttpResponse(msg)

#user/dan1/4
def gugudan1(request, dan):
    dan = int(dan)
    result=""
    for i in range(1, 10):
        result = result + f"{dan} X {i} = {dan*i}<br/>"

    return HttpResponse(result)

# sadari/w1/w2/h





