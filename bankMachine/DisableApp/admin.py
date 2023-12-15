from django.contrib import admin
from DisableApp.models import Accountdetails
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','gender','address','phone','acc')
admin.site.register(Accountdetails,StudentAdmin)