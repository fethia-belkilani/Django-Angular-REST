from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views
from django.contrib.auth import views as auth_views




urlpatterns=[
    path('profile/',views.ProfileView.as_view()),
    path('api/auth/', views.CustomAuthToken.as_view())

]
urlpatterns= format_suffix_patterns(urlpatterns) 