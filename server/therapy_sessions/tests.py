from django.test import TestCase

from therapy_sessions.exceptions import PaymentTooHighException
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


def session_factory(patient, therapist) -> Session:
    return Session.create({
        'patient': patient,
        'therapist': therapist,
        'fee': 200,
    })


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

    def test_session_full_payment(self):
        session = session_factory(self.patient, self.therapist)

        result = session.add_payment(session.fee)

        self.assertIsNotNone(result)
        self.assertEqual(result.session, session)

    def test_session_several_valid_payments(self):
        session = session_factory(self.patient, self.therapist)

        session.add_payment(session.fee / 2)
        session.add_payment(session.fee / 2)

        self.assertEqual(
            len(session.payments.all()),
            2,
        )

    def test_payment_higher_than_fee(self):
        session = session_factory(self.patient, self.therapist)

        with self.assertRaises(PaymentTooHighException):
            session.add_payment(session.fee + 100)

    def test_partial_payments_higher_tan_fee(self):
        session = session_factory(self.patient, self.therapist)
        session.add_payment(session.fee)

        with self.assertRaises(PaymentTooHighException):
            session.add_payment(100)
