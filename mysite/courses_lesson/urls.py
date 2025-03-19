from .views import *
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()

router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'teacher', TeacherViewSet, basename='teachers')
router.register(r'student', StudentViewSet, basename='students')
router.register(r'links', LinksViewSet, basename='links')
router.register(r'category', CategoryViewSet, basename='categories')
router.register(r'courses', CoursesViewSet, basename='courses')
router.register(r'lesson', LessonViewSet, basename='lessons')
router.register(r'assignment', AssignmentViewSet, basename='assignments')
router.register(r'exam', ExamViewSet, basename='exams')
router.register(r'question', QuestionViewSet, basename='questions')
router.register(r'answers', AnswersViewSet, basename='answers')
router.register(r'certificate', CertificateViewSet, basename='certificates')
router.register(r'review', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]