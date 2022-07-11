from datetime import date
from pydantic import BaseModel
from typing import Optional
from infrastructure.models.patient import gender_enum

class Patient(BaseModel):
    patient_id: str
    name: str
    gender: gender_enum
    date_of_birth: Optional[date] = None
    age: str
    address: str
    contact_details: str
