from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from therapy_sessions.tests.utils import patient_factory, session_factory, therapist_factory


def add_payment_endpoint(session_id: int) -> str:
    return reverse("add-payment", args=[session_id])


class TestPaymentsApi(TestCase):
    def setUp(self):
        self.patient = patient_factory()
        self.therapist = therapist_factory()
        self.session = session_factory(self.patient, self.therapist)
        self.test_client = APIClient()

    def test_add_valid_payment(self):
        response = self.test_client.post(
            add_payment_endpoint(self.session.id),
            { 'amount': self.session.fee },
        )
        payment = self.session.payments.first()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['id'], payment.id)

    def test_add_invalid_payment(self):
        response = self.test_client.post(
            add_payment_endpoint(self.session.id),
            { 'amount': -200 },
        )

        self.assertEqual(response.status_code, 400)