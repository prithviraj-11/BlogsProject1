from django.contrib import admin
from .models import UserInfo,BlogDetails
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display=['username','password']

class BlogDetailsAdmin(admin.ModelAdmin):
    list_display=['id','title','author','content','photo','creation_date','published_date','user']

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(BlogDetails,BlogDetailsAdmin)