

from domain.entities.patient import Patient


class InMemoryPatientRepository:
    def __init__(self):
        self.patients : list[Patient] = []

    def create(self, patient: Patient):
        self.patients.append(patient)

    def find_by_email(self, email: str):
        for patient in self.patients:
            if patient.email == email:
                return patient
        return None