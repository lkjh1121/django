from django.db import models

# Create your models here.
#models.Model 이라는 클래스를 상속 받아서 테이블에 대한 정의를 같이 한다 

class Guestbook(models.Model): #반드시 상속을 받아야 테이블도 만들어 주고 한다 
    #id = models.BigAutoField() #auto increment 
    #자동으로 만들어진다. 
    title = models.CharField(max_length=600)
    writer = models.CharField(max_length=40)
    wdate = models.DateTimeField() 
    contents = models.TextField()
    hit= models.IntegerField()

    #파이썬의 연산자 중복 기능  자바 toString()
    def __str__(self):
        return self.title

#print( Board() )
