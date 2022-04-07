from django.db import models

from therapy_sessions.types import SessionCreateData


class Therapist(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=60)


class Patient(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=60)


class Session(models.Model):
    fee = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    therapist = models.ForeignKey(
        'therapy_sessions.Therapist',
        on_delete=models.PROTECT,
    )
    patient = models.ForeignKey(
        'therapy_sessions.Patient',
        on_delete=models.PROTECT,
    )

    @classmethod
    def create(cls, data: SessionCreateData) -> 'Session':
        assert data['fee'] > 0

        return cls.objects.create(
            therapist=data['therapist'],
            patient=data['patient'],
            fee=data['fee'],
        )


class Payment(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(
        'therapy_sessions.Session',
        on_delete=models.PROTECT,
    )
