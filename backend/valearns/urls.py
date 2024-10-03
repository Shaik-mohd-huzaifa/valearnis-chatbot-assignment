from django.urls import path
from valearns import views

urlpatterns = [
    path("chat", views.chatbot_view, name="some_view"),
]
