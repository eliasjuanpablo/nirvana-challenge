from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from therapy_sessions.tests.utils import patient_factory, therapist_factory


def create_session_endpoint() -> str:
    return reverse("create-session")


class TestSessionsApi(TestCase):
    def setUp(self):
        self.patient = patient_factory()
        self.therapist = therapist_factory()
        self.test_client = APIClient()

    def test_create_session(self):
        response = self.test_client.post(
            create_session_endpoint(),
            { 'patient_id': self.patient.id, 'fee': 200.0 }
        )

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json()["id"])

    def test_create_session_with_invalid_fee(self):
        response = self.test_client.post(
            create_session_endpoint(),
            { 'patient_id': self.patient.id, 'fee': -200.0 }
        )

        self.assertEqual(response.status_code, 400)
    
    def test_create_session_with_missing_keys_in_payload(self):
        response = self.test_client.post(
            create_session_endpoint(),
            { 'fee': 200.0 }
        )

        self.assertEqual(response.status_code, 400)