from rest_framework import serializers

from therapy_sessions.models import Payment, Session


class CreateSessionSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Session
        fields = ['patient_id', 'fee']


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class AddPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'