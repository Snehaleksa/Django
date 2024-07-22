from django.contrib import admin
from .models import Student
from .models import Class

# Register your models here.


admin.site.register(Student)



class ClassAdmin(admin.ModelAdmin):
    list_display=('Name','Gender','Age','Date','District','Phone','Username','Password')
    fieldsets = ((None, {'fields':('Name','Age','Date')}),)
    search_fields=('Name','Date')

admin.site.register(Class,ClassAdmin)    