from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from therapy_sessions.tests.utils import patient_factory, session_factory, therapist_factory


def get_patients_endpoint() -> str:
    return reverse("list-patients")


class TestPaymentsApi(TestCase):
    def setUp(self):
        self.therapist = therapist_factory()
        self.patient = patient_factory()
        self.test_client = APIClient()

    def test_list_patients(self):
        response = self.test_client.get(
            get_patients_endpoint()
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['id'], self.patient.id)