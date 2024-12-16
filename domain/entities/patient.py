from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr


class Patient(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    date_of_birth: date
    sex: str
    address: str
    phone_number: str
    consent: bool
    guardian_consent: Optional[bool] = False

    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
    
    def is_minor(self):
        return self.age() < 18