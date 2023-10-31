from django.contrib import admin
from .models import Job, Company, Category, JobApply
from django_summernote.admin import SummernoteModelAdmin

#class
class JobAdmin(SummernoteModelAdmin):
    list_display = [ 'title', 'location', 'company', 'job_type', 'vacancy', 'category' ]
    search_fields = [  'title', 'category', 'description' ]
    list_filter = [ 'vacancy', 'job_type', 'category', 'experience' ]
    summernote_fields = '__all__'



# Register your models here.

admin.site.register(Job,JobAdmin)
admin.site.register(Company)
admin.site.register(Category)
admin.site.register(JobApply)
