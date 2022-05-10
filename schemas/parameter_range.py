from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Parameter_Range(BaseModel):
    lower_limit : Optional[int] = None
    upper_limit : Optional[int] = None
    low_remark : Optional[str] = None
    high_remark : Optional[str] = None
    normal_remark : Optional[str] = None