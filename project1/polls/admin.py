""" admin page functions for polls"""
from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.site_header = "Kaviya"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Django"


class ChoiceInLine(admin.TabularInline):
    """ choice line functions"""
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """ functions for question on admin"""
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
