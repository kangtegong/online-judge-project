from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('news/', views.news, name="news"),
    path('note/', views.note, name="note"),
    path('note/<int:note_pk>', views.note_detail, name="note_detail"),

    path('profile/', views.profile, name="profile"),
    path('myclass/', views.myclass, name="myclass"),

    path('calendar/', views.calendar, name="calendar"),
    path('event/<int:event_pk>', views.event, name="event"),
    path('mycode/', views.mycode, name="mycode"),
    
]
