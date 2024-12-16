from datetime import date
from pydantic import BaseModel, EmailStr


class Patient(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    date_of_birth: date