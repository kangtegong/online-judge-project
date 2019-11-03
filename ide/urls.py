from django.urls import path
from . import views

urlpatterns = [
    path('ftz/', views.ftz, name="ftz"),
    path('probset/', views.ProbView.as_view(), name="probset"),
    path('save/', views.CodeSave.as_view(), name="codesave"),
]
