from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_signup', views.student_signup, name='student_signup'),
    path('student_signin', views.student_signin, name='student_signin'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]