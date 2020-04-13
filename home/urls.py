from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name='home'),
    path('<int:items_id>/',views.detail,name='detail'),
    path('afterlogin',views.afterlogin,name='afterlogin'),
    path('upload/',views.upload,name='upload'),
    path('uploadetail',views.uploadetail,name='uploadetail'),
    path('profile/',views.profile,name='profile'),
    
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
