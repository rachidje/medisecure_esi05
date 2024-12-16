from typing import TypedDict

from pydantic import ValidationError
from domain.entities.patient import Patient
from domain.exceptions.missing_required_field import MissingRequiredField
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistException
from infrastructure.adapters.secondary.in_memory_patient_repository import InMemoryPatientRepository

class PatientDataPayload(TypedDict):
    firstname: str
    lastname: str
    email: str

class CreatePatientFolderUsecase:
    def __init__(self, repository: InMemoryPatientRepository):
        self.repository = repository

    def execute(self, patient_data: PatientDataPayload):
        existing_patient = self.repository.find_by_email(patient_data["email"])
        if existing_patient:
            raise PatientAlreadyExistException()
        try:
            patient = Patient.model_validate(patient_data)
        except ValidationError as e:
            raise MissingRequiredField(f"Missing required: {e.errors()[0]['loc'][0]}")