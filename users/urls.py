from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf.urls import include


from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('account/', include('account.urls')),
]
