from pydantic import BaseModel
from typing import Optional

class Lab_Result(BaseModel):
    parameter_name : Optional[str] = None
    test_name : Optional[int] = None
    parameter_id : Optional[int] = None
    unit : Optional[str] = None
    result : Optional[str] = None
    upper_limit : Optional[int] = None
    lower_limit : Optional[int] = None
    remark : Optional[str] = None