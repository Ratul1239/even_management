
from django.contrib import admin
from django.urls import path
from enen_management.views import home,create_event,event_list ,update_event,delete_event,Dashboard,category_list,participant_list
urlpatterns = [
    path('', home, name='home'),
    path('home/',home),
    path('create_even/',create_event ,name='create_event'),
    path('event_list/',event_list,name='event_list'),
    path('update_event/<int:id>/', update_event, name='update_event'),
    path('delete_event/<int:id>/', delete_event, name='delete_event'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('category_list/', category_list, name='category_list'),
    path('participants/', participant_list, name='participant_list'),
]
