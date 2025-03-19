from django_filters import FilterSet
from .models import *


class CoursesFilter(FilterSet):
    class Meta:
        model = Courses
        fields = {
            'category': ['exact'],
            'level': ['exact'],
            'price': ['gt', 'lt']

        }

class ReviewFilter(FilterSet):
    class Meta:
        model = Review
        fields = {
            'course': ['exact'],
            'user': ['exact'],
            'rating': ['gt', 'lt']

        }