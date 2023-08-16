from django.contrib import admin
from django.urls import path
from authentication import views

urlpatterns = [

    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('login_after_signup',views.login_after_signup,name='account_created'),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout',views.logout_account,name='logout'),
    path('login_failed',views.login_failed,name='login_failed'),
    # path('verify/<str:id>',views.verify,name='verification')
    path('create_new_project',views.createProject,name='newproject'),
    path('result',views.result,name='result')
]
