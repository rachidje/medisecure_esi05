from domain.entities.patient import Patient
from domain.ports.secondary.patient_repository_interface import PatientRepositoryInterface

class InMemoryPatientRepository(PatientRepositoryInterface):
    def __init__(self):
        self.patients : list[Patient] = []

    def create(self, patient: Patient):
        self.patients.append(patient)

    def find_by_email(self, email: str) -> Patient | None:
        for patient in self.patients:
            if patient.email == email:
                return patient
        return None