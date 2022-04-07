from random import random
from therapy_sessions.models import Patient, Session, Therapist


def patient_factory(model=Patient) -> Patient:
    return model.objects.create(
        email='test@test.com',
        name='Test Patient' + str(random()),
    )


def therapist_factory(model=Therapist) -> Therapist:
    return model.objects.create(
        email='test@test.com',
        name='Test Therapist' + str(random()),
    )


def session_factory(patient, therapist, model=Session) -> Session:
    return model.create({
        'patient': patient,
        'therapist': therapist,
        'fee': 200,
    })
