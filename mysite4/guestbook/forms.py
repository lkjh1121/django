from django import forms 
from guestbook.models import Guestbook 

#guestbook_write.html 이 파일의 태그들과 모델단의 변수들을 연결시킨다 
class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook 
        fields = ['title', 'writer', 'contents']
        labels = {  'title':'제목', 
                    'writer':'작성자', 
                    'contents':'내용'}
