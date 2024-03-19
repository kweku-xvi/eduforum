from .models import Course, Lecturer, Class
from django.contrib import admin


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'course_type', 'credit_hours')


class LecturerAdmin(admin.ModelAdmin):
    list_display = ('lecturer_id', 'name', 'email', 'office_location')


class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'course', 'lecturer', 'week_day', 'time_start', 'time_end')


admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Class, ClassAdmin)
