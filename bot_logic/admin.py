from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'test', 'multi_answer')
    list_filter = ('test', 'category')
    search_fields = ('text__contains',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'is_right')
    list_filter = ('question__test',)
    search_fields = ('pk', 'question__text__contains', 'text__contains')


admin.site.register(Student)
admin.site.register(StudentCondition)
admin.site.register(StudentAnswer)
admin.site.register(StudentTest)
admin.site.register(Test)
