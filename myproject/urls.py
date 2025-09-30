from django.contrib import admin
from django.urls import path
from enen_management.views import (
    custom_login, custom_logout, Dashboard, home, create_event,
    event_list, update_event, delete_event, category_list, participant_list,past_events_view,total_event_view,upcoming_event_view,participant_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', custom_login, name='login'),         
    path('login/', custom_login, name='login'),   
    path('logout/', custom_logout, name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('create_event/', create_event, name='create_event'),
    path('update_event/<int:id>/', update_event, name='update_event'),
    path('delete_event/<int:id>/', delete_event, name='delete_event'),
    path('category_list/', category_list, name='category_list'),
    path('participants/', participant_list, name='participant_list'),
    path('event_list/', event_list, name='event_list'),
    path('past_events/', past_events_view, name='past_events'),
    path('total_events/', total_event_view, name='total_events'),
    path('upcoming_event/', upcoming_event_view, name='upcoming_event'),
    path('participants/', participant_view, name='participants')

]
