from django.urls import path,include
from .views import home,download_resume
urlpatterns = [
    path('',home),
    path('download/',download_resume),
]
