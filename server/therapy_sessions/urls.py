from django.urls import path

from therapy_sessions.views import AddPaymentView, ListCreateSession, PatientsView


urlpatterns = [
    path(
        "api/v1/sessions/",
        ListCreateSession.as_view(),
        name="list-create-session",
    ),
    path(
        "api/v1/sessions/<int:id>/payments",
        AddPaymentView.as_view(),
        name="add-payment",
    ),
    path(
        "api/v1/patients",
        PatientsView.as_view(),
        name="list-patients",
    ),
]
