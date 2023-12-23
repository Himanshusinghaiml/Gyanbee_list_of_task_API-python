from django.contrib import admin
from .models import tasktable
# Register your models here.
 
@admin.register(tasktable)
class tasktableadmin(admin.ModelAdmin):
    list_display=('id','title','description','completed')