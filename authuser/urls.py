from django.urls import path
from . import views


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('sighupsubmit',views.sighupsubmit,name='sighupsubmit'),
    path('loginsubmit',views.loginsubmit,name='loginsubmit'),
    path('logout',views.logout,name='logout'),
]
