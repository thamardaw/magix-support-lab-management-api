from datetime import date
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from infrastructure.models.patient import gender_enum

class Patient(BaseModel):
    id: int
    patient_id: Optional[str] = None
    name: str
    gender: gender_enum
    date_of_birth: Optional[date] = None 
    age: str
    address: str
    contact_details: Optional[str] = None
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True