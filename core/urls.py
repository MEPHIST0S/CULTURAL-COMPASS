from django.urls import path
from core.views import home, about, landmark_list, landmark_detail, guide_view, premium

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path('landmarks/', landmark_list, name='landmark_list'),
    path('landmark/<int:landmark_id>/', landmark_detail, name='landmark_detail'),
    path('guides/', guide_view, name='guides'),
    path("premium/", premium, name="premium")
]