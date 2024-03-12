from . import views
from django.urls import path


urlpatterns = [
    path('add', views.add_event_view, name='add_events'),
    path('all', views.get_all_events_view, name='get_all_events'),
    path('search', views.search_events_view, name='search_events'),
    path('<str:id>/update', views.update_event_view, name='update_events'),
    path('<str:id>/delete', views.delete_event_view, name='delete_events'),
    path('next-week', views.events_in_coming_week_view, name='events_in_next_week'),
    path('next-month', views.events_in_coming_month_view, name='events_in_next_month'),
    path('<str:id>', views.get_specific_event_view, name='get_specific_event'),
    path('user/<str:id>', views.get_events_by_specific_user, name='get_events_by_specific_user'),
]