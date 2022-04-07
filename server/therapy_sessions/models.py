from django.db import models


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


class Payment(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(
        'therapy_sessions.Session',
        on_delete=models.PROTECT,
    )
