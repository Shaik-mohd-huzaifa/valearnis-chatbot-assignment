from django.urls import path
from . import views

urlpatterns = [
    path("chat", views.chatbot_view, name="some_view"),
    path("ask", views.ask, name="ask questions"),
]
