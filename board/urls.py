from django.urls import path
from . import views

urlpatterns = [

    path('', views.PostView.as_view(), name='freeboardlist'),
    path('newpost/', views.PostCreate.as_view(), name='new'),
    path('detail/<int:pk>', views.PostDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.PostUpdate.as_view(), name='change'),
    path('delete/<int:pk>', views.PostDelete.as_view(), name='del'),

]