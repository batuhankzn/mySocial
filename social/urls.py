from django.urls import path
from . import views


app_name = 'social'

urlpatterns = [
    path('', views.index,name="index"),
    path('beeps/', views.beeps,name="beeps"),
    path('addbeeps/', views.addbeeps,name="addbeeps"),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('myaccount/', views.myaccount,name="myaccount"),

]

