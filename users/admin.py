from django.contrib import admin
from users.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','level']
    list_filter = ['level']
    search_fields = ['name']
    
admin.site.register(User,UserAdmin)
admin.site.register(Level)
admin.site.register(College)