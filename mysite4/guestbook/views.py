from django.shortcuts import render
from django.http import HttpResponse


dataList = [
    {"id":1, "title":"제목1", "contents":"내용1", "writer":"작성자1"},
    {"id":2, "title":"제목2", "contents":"내용2", "writer":"작성자2"},
    {"id":3, "title":"제목3", "contents":"내용3", "writer":"작성자3"},
    {"id":4, "title":"제목4", "contents":"내용4", "writer":"작성자4"},
    {"id":5, "title":"제목5", "contents":"내용5", "writer":"작성자5"},
]

# Create your views here.
def list(request):
    return render(request, "guestbook/list.html", {"title":"방명록", 
                                                    "dataList":dataList}) 

from .forms import GuestbookForm
from django.utils import timezone 

def write(request):
    form = GuestbookForm()
    return render(request, "guestbook/guestbook_write.html", {"form":form})

def save(request):
    form = GuestbookForm(request.POST)
    guestbook = form.save(commit=False) #데이터를 임시로 디비에 저장 
    #Commit=False 로 주면 아직 확정 상태가 아니다 
    guestbook.wdate = timezone.now() 
    guestbook.hit = 0 
    guestbook.save() # 확정
    #다른페이지로 이동시킨다 
    return HttpResponse("success")






