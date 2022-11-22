from django.contrib import admin

# Register your models here.
from .models import Guestbook 

class GuestbookAdmin(admin.ModelAdmin):
    search_fields=['title', 'contents']

admin.site.register(Guestbook, GuestbookAdmin )
