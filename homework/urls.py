from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseList.as_view(), name='courselist'),
    path('<int:pk>', views.hwlist, name='hwlist'),
    path('hwcreate', views.HWCreate.as_view(), name="hwcreate"),
    path('hwdetail/<int:pk>', views.HWDetail.as_view(), name="hwdetail"),

    path('codehw', views.CodeSubmits.as_view(), name="codehw"),
    path('coderv', views.codereview, name="codereview"),
    path('filehw', views.FileSubmits.as_view(), name="filehw"),
    path('mailhw', views.MailSubmits.as_view(), name="mailhw"),
    # path('submissions', views.SubmitList.as_view(), name="submissions"),
    path('sumbissions/<int:pk>', views.submitlist, name="submissions"),

    path('classregister', views.ClassRegister.as_view(), name="classregister"),
    path('registerclass/<int:pk>', views.registerclass, name="registerclass"),

    path('filedetail/<int:pk>', views.FileDetail.as_view(), name='filedetail'),
    path('codedetail/<int:pk>', views.CodeDetail.as_view(), name='codedetail'),
]
