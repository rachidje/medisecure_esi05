from typing import Protocol

from domain.entities.patient import Patient


class PatientRepositoryInterface(Protocol):
    def find_by_email(self, email: str) -> Patient | None: ...
    def create(self, patient: Patient) -> None: ...