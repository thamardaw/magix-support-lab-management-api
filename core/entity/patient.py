from datetime import date
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from infrastructure.models.patient import gender_enum

class Patient(BaseModel):
    id: int
    name: Optional[str] = None
    gender: Optional[gender_enum] = None
    date_of_birth: Optional[date] = None 
    age: Optional[int] = None
    address: Optional[str] = None
    contact_details: Optional[str] = None
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True