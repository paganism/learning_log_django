from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken import views
from .views import *


urlpatterns = [
    path('topics', Topics.as_view()),
    path('entries', Entries.as_view()),
    path('users', Users.as_view()),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('auth-token/', views.obtain_auth_token, name='auth-token')
]
