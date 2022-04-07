from rest_framework import serializers

from therapy_sessions.models import Payment, Patient, Session


class CreateSessionSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Session
        fields = ['patient_id', 'fee']


class AddPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['amount']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()
    class Meta:
        model = Session
        fields = '__all__'

