from django.http import JsonResponse
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.views import APIView
from therapy_sessions.exceptions import DomainException

from therapy_sessions.models import Session, Therapist, Patient
from therapy_sessions.serializers import CreateSessionSerializer, PatientSerializer, PaymentSerializer, SessionSerializer


def get_current_therapist(request):
    """Extracts the current therapist from the request."""

    # NOTE: currently mocked, should actually infer it from the request's auth token or similar
    return Therapist.objects.first()


class ListCreateSession(APIView):
    def get(self, request):
        therapist = get_current_therapist(request)
        sessions = therapist.get_sessions()

        output_serializer = SessionSerializer(sessions, many=True)

        return JsonResponse(output_serializer.data, status=200, safe=False)

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
                'fee': float(data['fee']),
            })
        except (AssertionError, DomainException):
            raise ValidationError()
        except Session.DoesNotExist:
            raise NotFound()

        output_serializer = SessionSerializer(session)

        return JsonResponse(output_serializer.data, status=201)


class AddPaymentView(APIView):
    def post(self, request, id):
        try:
            session = Session.get_by_id(id)
            payment = session.add_payment(float(request.data['amount']))
        except (AssertionError, DomainException):
            raise ValidationError()
        except Session.DoesNotExist:
            raise NotFound()

        output_serializer = PaymentSerializer(payment)
        return JsonResponse(output_serializer.data, status=201)


class PatientsView(APIView):
    def get(self, request):
        therapist = get_current_therapist(request)
        patients = therapist.get_patients()
        output_serializer = PatientSerializer(patients, many=True)

        return JsonResponse(output_serializer.data, status=200, safe=False)
