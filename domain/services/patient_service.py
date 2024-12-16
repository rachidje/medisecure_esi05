
# class Helpers
from domain.entities.patient import Patient
from domain.exceptions.missing_guardian_consent_exception import MissingGuardianConsentException
from domain.exceptions.missing_patient_consent_exception import MissingPatientConsentException


class PatientService:
    @staticmethod
    def validate_guardian_consent(patient: Patient):
        if patient.is_minor() and not patient.guardian_consent:
            raise MissingGuardianConsentException()
    
    @staticmethod
    def validate_patient_consent(patient: Patient):
        if not patient.consent:
            raise MissingPatientConsentException()

