from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .lab_test import Lab_Test

class Lab_Result(BaseModel):
    id : int
    lab_report_id : Optional[int] = None
    parameter_name : Optional[str] = None
    test_name : Optional[str] = None
    test_id: Optional[int] = None
    test: Optional[Lab_Test] = None
    parameter_id : Optional[int] = None
    unit : Optional[str] = None
    result : Optional[str] = None
    upper_limit : Optional[float] = None
    lower_limit : Optional[float] = None
    remark : Optional[str] = None
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True