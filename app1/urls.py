from django.urls import path
from . import views
urlpatterns = [
    path('', views.start),
    path('registration', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),

]