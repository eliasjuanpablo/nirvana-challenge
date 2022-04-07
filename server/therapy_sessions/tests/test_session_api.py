from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from therapy_sessions.tests.utils import patient_factory, session_factory, therapist_factory


def list_create_session_endpoint() -> str:
    return reverse("list-create-session")


class TestSessionsApi(TestCase):
    def setUp(self):
        self.patient = patient_factory()
        self.therapist = therapist_factory()
        self.test_client = APIClient()

    def test_create_session(self):
        response = self.test_client.post(
            list_create_session_endpoint(),
            { 'patient_id': self.patient.id, 'fee': 200.0 }
        )

        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(response.json()["id"])

    def test_create_session_with_invalid_fee(self):
        response = self.test_client.post(
            list_create_session_endpoint(),
            { 'patient_id': self.patient.id, 'fee': -200.0 }
        )

        self.assertEqual(response.status_code, 400)
    
    def test_create_session_with_missing_keys_in_payload(self):
        response = self.test_client.post(
            list_create_session_endpoint(),
            { 'fee': 200.0 }
        )

        self.assertEqual(response.status_code, 400)

    def test_list_sessions_ordered_by_date(self):
        sessions = [
            session_factory(self.patient, self.therapist),
            session_factory(self.patient, self.therapist),
            session_factory(self.patient, self.therapist),
        ]

        response = self.test_client.get(
            list_create_session_endpoint(),
        )

        self.assertEqual(
            [s["id"] for s in response.json()],
            list(reversed([s.id for s in sessions])),
        )
