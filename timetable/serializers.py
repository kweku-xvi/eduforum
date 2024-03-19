from rest_framework import serializers
from .models import Course, Lecturer, Class


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'course_type', 'credit_hours']

    
class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['lecturer_id', 'name', 'email', 'office_location']

        read_only_fields = ['lecturer_id']


class ClassSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField()
    lecturer = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ['class_id', 'course', 'lecturer', 'week_day', 'time_start', 'time_end', 'class_location']

        read_only_fields = ['class_id']

    
    def get_course(self, obj):
        return obj.course.course_name if obj.course else None

    
    def get_lecturer(self, obj):
        return obj.lecturer.name if obj.lecturer else None