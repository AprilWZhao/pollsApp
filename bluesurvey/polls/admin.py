from django.contrib import admin

# Register your models here.
from django.contrib import admin
from polls.models import Choice, Question

# admin.site.register(Question)
#admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None,  {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['qustion_text']

admin.site.register(Question,QuestionAdmin)