from django.urls import path

from therapy_sessions.views import AddPaymentView, CreateSessionView


urlpatterns = [
    path(
        "api/v1/sessions/",
        CreateSessionView.as_view(),
        name="create-session",
    ),
    path(
        "api/v1/sessions/<int:id>/payments",
        AddPaymentView.as_view(),
        name="add-payment",
    ),
]
