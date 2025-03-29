from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import *

class LessonInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Lesson
    extra = 1

class AnswersInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Answers
    extra = 1

class QuestionInline(admin.TabularInline, TranslationInlineModelAdmin):
    model = Question
    extra = 1

@admin.register( Lesson, Assignment, Answers)
class ALLAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',)
        }

@admin.register(Courses)
class CourseAdmin(TranslationAdmin):
    inlines = [LessonInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
@admin.register(Exam)
class ExamAdmin(TranslationAdmin):
    inlines = [QuestionInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Question)
class QuestionAdmin(TranslationAdmin):
    inlines = [AnswersInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Links)
admin.site.register(Certificate)
admin.site.register(Category)
admin.site.register(Review)

