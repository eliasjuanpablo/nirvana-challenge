from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from therapy_sessions.exceptions import DomainException

from therapy_sessions.models import Session, Therapist, Patient
from therapy_sessions.serializers import CreateSessionSerializer, SessionSerializer


def get_current_therapist(request):
    """Extracts the current therapist from the request."""

    # NOTE: currently mocked, should actually infer it from the request's auth token or similar
    return Therapist.objects.first()


class CreateSessionView(APIView):
    def post(self, request):
        try:
            input_serializer = CreateSessionSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)

            data = input_serializer.initial_data
            therapist = get_current_therapist(request)
            patient = Patient.get_by_id(data['patient_id'])

            session = Session.create({
                'patient': patient,
                'therapist': therapist,
                'fee': data['fee'],
            })
        except (AssertionError, DomainException):
            raise ValidationError()

        output_serializer = SessionSerializer(session)

        return JsonResponse(output_serializer.data, status=201)
