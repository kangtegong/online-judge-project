from django.urls import path
from . import views

urlpatterns = [
    path('<int:subno>/', views.getClass, name="getClass"),
    path('overviewlist/', views.OverviewList.as_view(), name="overviewlist"),
]
