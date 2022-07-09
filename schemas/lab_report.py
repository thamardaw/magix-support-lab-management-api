from pydantic import BaseModel
from datetime import date
from typing import Optional

class Lab_Report(BaseModel):
    patient_id : int
    doctor_name : Optional[str] = None
    sample_id : Optional[int] = None
    sample_type : Optional[str] = None
    patient_type : Optional[str] = None
    test_date : Optional[date] = None