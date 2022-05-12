from pydantic import BaseModel
from datetime import datetime
from datetime import date
from typing import List,Optional
from .lab_result import Lab_Result
from .patient import Patient

class Lab_Report(BaseModel):
    id : int
    patient_id : int
    patient : Optional[Patient] = None
    doctor_name : Optional[str] = None
    sample_id : Optional[int] = None
    sample_type : Optional[str] = None
    patient_type : Optional[str] = None
    test_date : Optional[date] = None
    lab_results : Optional[List[Lab_Result]] = []
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True