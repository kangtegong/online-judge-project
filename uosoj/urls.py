from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ide/', include('ide.urls')),       
    path('dash/', include('dash.urls')), # main page
    path('board/', include('board.urls'), name="board"), # main page
    path('', include('accounts.urls')),
    path('homework/', include('homework.urls')),
    path('overview/', include('overview.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    path('browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),
    path('comments/', include('django_comments_xtd.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
