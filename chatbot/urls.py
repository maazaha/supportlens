from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('api/traces', views.get_traces, name='get_traces'),
    path('api/traces/create', views.create_trace, name='create_trace'),
    path('api/analytics', views.get_analytics, name='get_analytics'),
    path('chat', views.chat, name='chat'),

    # Auth endpoints
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),

    # UI views
    path('', views.chat_view, name='chat_view'),
    path('dashboard', views.dashboard_view, name='dashboard_view'),
]
