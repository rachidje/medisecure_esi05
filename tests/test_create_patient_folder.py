from datetime import date
from typing import Any
import pytest

from application.usecases.create_patient_folder import CreatePatientFolderUsecase
from domain.entities.patient import Patient
from domain.exceptions.missing_guardian_consent_exception import MissingGuardianConsentException
from domain.exceptions.missing_patient_consent_exception import MissingPatientConsentException
from domain.exceptions.missing_required_field import MissingRequiredField
from domain.exceptions.patient_already_exist_exception import PatientAlreadyExistException
from infrastructure.adapters.secondary.in_memory_patient_repository import InMemoryPatientRepository

    

class TestCreatePatientFolderUsecase:
    def setup_method(self):
        self.repository = InMemoryPatientRepository()
        self.usecase = CreatePatientFolderUsecase(self.repository)
        
    def execute_without_all_fields(self, data: Any):
        self.usecase.execute(data)

    def test_should_fail_if_patient_already_exist(self):
        self.repository.create(Patient(
            firstname= 'John', 
            lastname= 'Doe', 
            email= 'johndoe@gmail.com', 
            date_of_birth= date(1979, 1, 1),
            sex="M",
            address= "25 rue de la paix",
            phone_number= "0601020304",
            consent= True
        ))

        with pytest.raises(PatientAlreadyExistException):
            self.usecase.execute({
                "firstname" : "John",
                "lastname" : "Doe",
                "email": "johndoe@gmail.com",
                "date_of_birth": date(1979, 1, 1),
                "sex": "M",
                "address": "25 rue de la paix",
                "phone_number": "0601020304",
                "consent": True
            })

    def test_should_fail_if_missing_data(self):
        with pytest.raises(MissingRequiredField):
            self.execute_without_all_fields({
                "firstname" : "John",
                "lastname" : "Doe",
                "email": "johndoe@gmail.com",
                "sex": "M",
                "address": "25 rue de la paix",
                "phone_number": "0601020304",
                "consent": True
            })

    def test_should_fail_if_no_patient_consent(self):
        with pytest.raises(MissingPatientConsentException):
            self.usecase.execute({
                "firstname" : "John",
                "lastname" : "Doe",
                "email": "johndoe@gmail.com",
                "date_of_birth": date(1979, 1, 1),
                "sex": "M",
                "address": "25 rue de la paix",
                "phone_number": "0601020304",
                "consent": False
            })

    def test_should_fail_if_no_guardian_consent_for_minor(self):
        with pytest.raises(MissingGuardianConsentException):
            self.usecase.execute({
                "firstname" : "John",
                "lastname" : "Doe",
                "email": "johndoe@gmail.com",
                "date_of_birth": date(2014, 1, 1),
                "sex": "M",
                "address": "25 rue de la paix",
                "phone_number": "0601020304",
                "consent": False,
                "guardian_consent": False
            })

    def test_should_create_patient_folder(self):
        self.usecase.execute({
                "firstname" : "John",
                "lastname" : "Doe",
                "email": "johndoe@gmail.com",
                "date_of_birth": date(1979, 1, 1),
                "sex": "M",
                "address": "25 rue de la paix",
                "phone_number": "0601020304",
                "consent": True,
            })
        
        fetched_patient = self.repository.find_by_email("johndoe@gmail.com")
        assert fetched_patient is not None

    # def test_should_return_id(self):
    #     ...