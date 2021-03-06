from pydantic import BaseModel
from typing import Optional

class Lab_Result(BaseModel):
    parameter_name : Optional[str] = None
    test_name : Optional[str] = None
    test_id: Optional[int] = None
    parameter_id : Optional[int] = None
    unit : Optional[str] = None
    result : Optional[str] = None
    upper_limit : Optional[float] = None
    lower_limit : Optional[float] = None
    remark : Optional[str] = None