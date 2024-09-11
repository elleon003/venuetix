from django.urls import path
from . import views 

app_name = 'events'

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('<slug:category_slug>/', views.event_list, name='event_list_by_category'),
    path('<int:id>/<slug:slug>/', views.event_detail, name='event_detail')
]
