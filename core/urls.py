from django.urls import path
from core.views import home, about, landmark_list

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path('landmarks/', landmark_list, name='landmark_list')
]