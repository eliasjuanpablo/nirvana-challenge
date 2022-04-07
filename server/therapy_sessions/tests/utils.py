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

