from .models import Event
from .serializers import EventSerializer
from datetime import timedelta
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from users.models import User
from users.permissions import IsVerified


def get_event(id:str): # get one event
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response (
            {
                'success':True,
                'message':'Event not found!'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return event


def get_user(id:str): # get one user
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response (
            {
                'success':False,
                'message':'User not found'
            }, status=status.HTTP_404_NOT_FOUND
        )
    return user


@api_view(['POST'])
@permission_classes([IsVerified])
def add_event_view(request):
    if request.method == 'POST':
        user = request.user # logged in user

        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(posted_by=user)

            return Response (
                {
                    'success':True,
                    'message':'Event added successfully',
                    'event':serializer.data
                }, status=status.HTTP_201_CREATED
            )
        return Response (
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes([IsVerified])
def get_specific_event_view(request, id:str):
    if request.method == 'GET':
        event = get_event(id=id)

        serializer = EventSerializer(event)

        return Response (
            {
                'success':True,
                'event':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes({IsVerified})
def get_all_events_view(request):
    if request.method == 'GET':
        events = Event.objects.all()

        serializer = EventSerializer(events, many=True)

        return Response (
            {
                'success':True,
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes([IsVerified])
def get_events_by_specific_user(request, id:str):
    if request.method == 'GET':
        user = get_user(id=id)

        events = Event.objects.filter(posted_by=user)
        serializer = EventSerializer(events, many=True)

        return Response (
            {
                'success':True,
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes([IsVerified])
def search_events_view(request):
    if request.method == 'GET':
        query = request.query_params.get('query')

        if not query:
            return Response (
                {
                    'success':False,
                    'message':'Provide a search query'
                }, status=status.HTTP_400_BAD_REQUEST
            )

        events = Event.objects.filter(
            Q(title__icontains=query)
        )

        serializer = EventSerializer(events, many=True)

        return Response (
            {
                'success':True,
                'message':'Search results:',
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['PUT', 'PATCH'])
@permission_classes([IsVerified])
def update_event_view(request, id:str):
    if request.method == 'PUT' or request.method == 'PATCH':
        user = request.user
        event = get_event(id=id)

        if user != event.posted_by and not user.is_staff:
            return Response (
                {
                    'success':True,
                    'message':'You cannot perform this action'
                }, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EventSerializer(event, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response (
                {
                    'sucess':True,
                    'message':'Event info update successful',
                    'event':serializer.data
                }, status=status.HTTP_200_OK
            )
        return Response (
            {
                'success':False,
                'message':serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['DELETE'])
@permission_classes([IsVerified])
def delete_event_view(request, id:str):
    if request.method == 'DELETE':
        user = request.user
        event = get_event(id=id)

        if user != event.posted_by and not user.is_staff:
            return Response (
                {
                    'success':True,
                    'message':'You cannot perform this action'
                }, status=status.HTTP_400_BAD_REQUEST
            )

        event.delete()
        return Response (
            {
                'success':True,
                'message':'Event has been deleted'
            }, status=status.HTTP_204_NO_CONTENT
        )


@api_view(['GET'])
@permission_classes([IsVerified])
def events_in_coming_week_view(request):
    if request.method == 'GET':
        timeframe = timezone.now() + timedelta(days=7)
        events = Event.objects.filter(date__gte=timezone.now(), date__lte=timeframe)

        serializer = EventSerializer(events, many=True)

        return Response (
            {
                'success':True,
                'message':'Events in the next week:',
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )


@api_view(['GET'])
@permission_classes([IsVerified])
def events_in_coming_month_view(request):
    if request.method == 'GET':
        timeframe = timezone.now() + timedelta(days=31)
        events = Event.objects.filter(date__gte=timezone.now(), date__lte=timeframe)

        serializer = EventSerializer(events, many=True)

        return Response (
            {
                'success':True,
                'message':'Events in the next week:',
                'events':serializer.data
            }, status=status.HTTP_200_OK
        )