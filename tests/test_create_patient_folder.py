import pytest

from application.usecases.create_patient_folder import CreatePatientFolderUsecase
from domain.entities.patient import Patient
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistException
from infrastructure.adapters.secondary.in_memory_patient_repository import InMemoryPatientRepository


class TestCreatePatientFolderUsecase:
    def test_should_fail_if_patient_already_exist(self):
        repository = InMemoryPatientRepository()
        usecase = CreatePatientFolderUsecase(repository)
        repository.create(Patient(
            firstname= 'John', lastname= 'Doe', email= 'johndoe@gmail.com'
        ))

        with pytest.raises(PatientAlreadyExistException):
            usecase.execute({
                "firstname" : "John",
                "lastname" : "Doe",
                "email": "johndoe@gmail.com"
            })

    # def test_should_fail_if_missing_data(self):
    #     ...

    # def test_should_fail_if_no_patient_consent(self):
    #     ...

    # def test_should_fail_if_no_guardian_consent_for_minor(self):
    #     ...

    # def test_should_return_id(self):
    #     ...