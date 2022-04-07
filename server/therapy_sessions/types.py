from typing import TypedDict


class SessionCreateData(TypedDict):
    therapist: object
    patient: object
    fee: float
