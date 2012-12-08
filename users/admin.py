from django.contrib import admin
from users.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','level']
    list_filter = ['level']
    search_fields = ['name']

class CollegeAdmin(admin.ModelAdmin):
    list_display = ['name','city','state']
    list_filter = ['city']
    search_fields = ['name']
admin.site.register(User,UserAdmin)
admin.site.register(Level)
admin.site.register(College,CollegeAdmin)