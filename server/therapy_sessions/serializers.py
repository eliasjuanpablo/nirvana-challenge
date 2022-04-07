from rest_framework import serializers

from therapy_sessions.models import Session


class CreateSessionSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(read_only=False)

    class Meta:
        model = Session
        fields = ["patient_id", "fee"]


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
