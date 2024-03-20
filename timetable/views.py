from .models import Course, Lecturer, Class
from .serializers import CourseSerializer, LecturerSerializer, ClassSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from users.models import User
from users.permissions import IsVerified


def get_course(id:str):
    try:
        course = Course.objects.get(course_code=id)
    except Course.DoesNotExist:
        return Response(
            {
                'success':False,
                'message':'Course does not exist'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return course


def get_lecturer(id:str):
    try:
        lecturer = Lecturer.objects.get(lecturer_id=id)
    except Lecturer.DoesNotExist:
        return Response (
            {
                'success':False,
                'message':'Lecturer does not exist'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return lecturer


def get_class(id:str):
    try:
        period = Class.objects.get(class_id=id)
    except Class.DoesNotExist:
        return Response(
            {
                'success':False,
                'message':'Class does not exist'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return period


@api_view(['POST'])
@permission_classes([IsVerified])
def add_course_view(request):
    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response (
                {
                    'success':True,
                    'message':'Course added successfully',
                    'info':serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response (
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([IsVerified])
def course_info_view(request, id:str):
    if request.method == 'GET':
        course = get_course(id=id)

        serializer = CourseSerializer(course)

        return Response(
            {
                'success':True,
                'course_info':serializer.data
            }, status=status.HTTP_200_OK
        )

    
@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_course_info_view(request, id:str):
    if request.method == 'PUT' or request.method == 'PATCH':
        course = get_course(id=id)

        serializer = CourseSerializer(course, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success':True,
                    'message':'Course info updated successfully',
                    'course_info':serializer.data
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_course_view(request, id:str):
    if request.method == 'DELETE':
        course = get_course(id=id)

        course.delete()

        return Response(
            {
                'success':True,
                'message':'Course successfully deleted'
            }, status=status.HTTP_204_NO_CONTENT
        )


@api_view(['POST'])
@permission_classes([IsVerified])
def add_lecturer_view(request):
    if request.method == 'POST':
        serializer = LecturerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success':True,
                    'message':'Lecturer added successfully',
                    'lecturer_info':serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([IsVerified])
def lecturer_info_view(request, id:str):
    if request.method == 'GET':
        lecturer = get_lecturer(id=id)

        serializer = LecturerSerializer(lecturer)

        return Response(
            {
                'success':True,
                'lecturer_info':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_lecturer_info_view(request, id:str):
    if request.method == 'PUT' or request.method == 'PATCH':
        lecturer = get_lecturer(id=id)

        serializer = LecturerSerializer(lecturer, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success':True,
                    'message':'Lecturer info updated successfully',
                    'lecturer_info':serializer.data
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_lecturer_view(request, id:str):
    if request.method == 'DELETE':
        lecturer = get_lecturer(id=id)

        lecturer.delete()

        return Response(
            {
                'success':True,
                'message':'Lecturer deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT
        )


@api_view(['POST'])
@permission_classes([IsVerified])
def add_class_view(request, course_id:str, lecturer_id:str):
    if request.method == 'POST':
        course = get_course(id=course_id)
        lecturer = get_lecturer(id=lecturer_id)

        serializer = ClassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(course=course, lecturer=lecturer)

            return Response(
                {
                    'success':True,
                    'message':'Class added successfully',
                    'class_info':serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'success':True,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([IsVerified])
def class_info_view(request, id:str):
    if request.method == 'GET':
        period = get_class(id=id)

        serializer = ClassSerializer(period)

        return Response(
            {
                'success':True,
                'class_info':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_class_view(request, id:str):
    if request.method == 'PUT' or request.method == 'PATCH':
        period = get_class(id=id)

        serializer = ClassSerializer(period, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'success':True,
                    'message':'Class info updated successfully',
                    'class_info':serializer.data
                }, status=status.HTTP_200_OK
            )
        return Response(
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_class_view(request, id:str):
    if request.method == 'DELETE':
        period = get_class(id=id)

        period.delete()

        return Response(
            {
                'success':True,
                'message':'Class deleted successfully'
            }, status=status.HTTP_204_NO_CONTENT
        )

        