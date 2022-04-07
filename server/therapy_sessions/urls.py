from django.urls import path

from therapy_sessions.views import CreateSessionView


urlpatterns = [
    path(
        "api/v1/sessions/",
        CreateSessionView.as_view(),
        name="create-session",
    ),
]
