from . import views
from django.urls import path

urlpatterns = [
    path('signup', views.sign_up_view, name='sign_up'),
    path('verify-user', views.verify_user_view, name='verify_user'),
    path('login', views.login_view, name='login'),
    path('password-reset', views.password_reset_view, name='password_reset'),
    path('password-reset-confirm', views.password_reset_confirm_view, name='password_reset_confirm'),
    path('users', views.get_all_users_view, name='get_all_users'),
    path('user/<str:id>', views.get_specific_user_view, name='get_specific_user'),
    path('user/<str:id>/update', views.update_user_info_view, name='update_user_info'),
    path('user/<str:id>/delete', views.delete_user_view, name='delete_user'),
    path('search', views.search_users_view, name='search_users'),
]