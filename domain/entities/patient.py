from pydantic import BaseModel, EmailStr


class Patient(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr