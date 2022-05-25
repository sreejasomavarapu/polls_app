from django.contrib import admin
from .models import *
# Register your models here.
# register only after migrating i.e running make migrations and migrate commands 
# 'Choice' object has no attribute 'model', got this error 
# seperate lines 
# AttributeError: 'Choice' object has no attribute 'urls' ->this error when written in same line
# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header="Pollster Admin" 
admin.site.site_title="Pollster Admin Area" # title of the page
admin.site.index_title="Welcome to Pollster Admin" # in the first page

class ChoiceInline(admin.TabularInline):
    model=Choice
    #extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{'fields':['question_title']}),
        #('Date Information',{'fields':['pub_date'],'classes':['collapse']}) 
        # this is editable as we did auto_now_add so we get an error if we put it here. We need to import 
        # timezone to get editable one
    ]
    inlines=[ChoiceInline]

admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)