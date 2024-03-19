from . import views
from django.urls import path


urlpatterns = [
    path('course/add', views.add_course_view, name='add_course'),
    path('course/<str:id>', views.course_info_view, name='course_info'),
    path('course/<str:id>/update', views.update_course_info_view, name='update_course_info'),
    path('course/<str:id>/delete', views.delete_course_view, name='delete_course_info'),
    path('lecturer/add', views.add_lecturer_view, name='add_lecturer'),
    path('lecturer/<str:id>', views.lecturer_info_view, name='lecturer_info'),
    path('lecturer/<str:id>/update', views.update_lecturer_info_view, name='update_lecturer_info'),
    path('lecturer/<str:id>/delete', views.delete_lecturer_view, name='delete_lecturer_info'),
    path('class/add/l-<str:lecturer_id>/c-<str:course_id>', views.add_class_view, name='add_class'),
    path('class/<str:id>', views.class_info_view, name='get_class_info'),
    path('class/<str:id>/update', views.update_class_view, name='update_class'),
    path('class/<str:id>/delete', views.delete_class_view, name='delete_class'),
]