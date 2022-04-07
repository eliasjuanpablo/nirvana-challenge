from django.db import models

from therapy_sessions.exceptions import PaymentTooHighException
from therapy_sessions.types import SessionCreateData


class Therapist(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=60)


class Patient(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=60)

    @classmethod
    def get_by_id(cls, id: int) -> 'Patient':
        return cls.objects.get(id=id)


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
        """Creates a Session instance."""
        assert data['fee'] > 0

        return cls.objects.create(
            therapist=data['therapist'],
            patient=data['patient'],
            fee=data['fee'],
        )

    @classmethod
    def get_by_id(cls, id: int) -> 'Session':
        return cls.objects.get(id=id)

    def add_payment(self, amount: float) -> 'Payment':
        """Create a Payment instance for this session."""

        assert amount > 0

        already_paid = self.payments.aggregate(
            sum=models.Sum('amount')
        )["sum"] or 0

        if amount > self.fee - already_paid:
            raise PaymentTooHighException()

        return Payment.objects.create(
            amount=amount,
            session=self,
        )


class Payment(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(
        'therapy_sessions.Session',
        on_delete=models.PROTECT,
        related_name="payments"
    )
