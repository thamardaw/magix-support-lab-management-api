from pydantic import BaseModel
from datetime import datetime
from typing import Optional
# from .lab_test import Lab_Test

class Parameter(BaseModel):
    id : int
    name : str
    unit : str
    lab_test_id : Optional[int] = None
    # lab_test : Optional[Lab_Test] = None
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True