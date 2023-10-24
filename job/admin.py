from django.contrib import admin
from .models import Job, Company, Category

#class
class JobAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'location', 'company', 'job_type', 'vacancy', 'category' ]
    search_fields = [  'title', 'category', 'description' ]
    list_filter = [ 'vacancy', 'job_type', 'category', 'experience' ]



# Register your models here.

admin.site.register(Job,JobAdmin)
admin.site.register(Company)
admin.site.register(Category)
  
