from django.contrib import admin

# Register your models here. 

from django.contrib.auth.admin import UserAdmin 

from .models import Custom 

class CustomUserAdmin(UserAdmin): 
    list_display=  (
      'username'  'first_name' , 'last_name', 'points', 'address', 'phone'
    )
admin.site.register(Custom, CustomUserAdmin) 

