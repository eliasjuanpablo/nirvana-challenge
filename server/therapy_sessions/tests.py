from django.test import TestCase

from therapy_sessions.models import Patient, Session, Therapist


def patient_factory() -> Patient:
    return Patient.objects.create(
        email='test@test.com',
        name='Test Patient',
    )


def therapist_factory() -> Therapist:
    return Therapist.objects.create(
        email='test@test.com',
        name='Test Therapist',
    )


class TherapySessionTests(TestCase):
    def setUp(self):
        self.patient = patient_factory()
        self.therapist = therapist_factory()

    def test_session_create(self):
        fee = 200.0
        session = Session.create({
            'patient': self.patient,
            'therapist': self.therapist,
            'fee': fee,
        })

        self.assertEqual(session.patient_id, self.patient.id)
        self.assertEqual(session.therapist_id, self.therapist.id)
        self.assertEqual(session.fee, fee)
        self.assertIsNotNone(session.created_at)

    def test_session_create_with_invalid_fee(self):
        fee = -200.0

        with self.assertRaises(AssertionError):
            Session.create({
                'patient': self.patient,
                'therapist': self.therapist,
                'fee': fee,
            })
