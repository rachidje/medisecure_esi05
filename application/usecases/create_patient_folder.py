from datetime import date
from typing import NotRequired, TypedDict

from pydantic import ValidationError
from domain.entities.patient import Patient
from domain.exceptions.missing_required_field import MissingRequiredField
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistException
from domain.ports.secondary.patient_repository_interface import PatientRepositoryInterface
from domain.services.patient_service import PatientService

class PatientDataPayload(TypedDict):
    firstname: str
    lastname: str
    email: str
    date_of_birth: date
    sex: str
    address: str
    phone_number: str
    consent: bool
    guardian_consent: NotRequired[bool]

class CreatePatientFolderUsecase:
    def __init__(self, repository: PatientRepositoryInterface):
        self.repository = repository

    def execute(self, patient_data: PatientDataPayload):
        existing_patient = self.repository.find_by_email(patient_data["email"])
        
        if existing_patient:
            raise PatientAlreadyExistException()
        try:
            patient = Patient.model_validate(patient_data)
        except ValidationError as e:
            raise MissingRequiredField(f"Missing required: {e.errors()[0]['loc'][0]}")
        
        PatientService.validate_guardian_consent(patient)
        PatientService.validate_patient_consent(patient)

        self.repository.create(patient)
        