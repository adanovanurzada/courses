from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Courses)
class CoursesTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('name_lesson', 'content')


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('name_assignment', 'description')


@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ('name_exam',)


@register(Question)
class QuestionTranslationOptions(TranslationOptions):
    fields = ('name_questions',)


@register(Answers)
class AnswersTranslationOptions(TranslationOptions):
    fields = ('answers',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('comment',)