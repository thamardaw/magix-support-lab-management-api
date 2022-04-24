from pydantic import BaseModel
from datetime import datetime
from typing import Optional
# from .parameter import Parameter

class Parameter_Range(BaseModel):
    id : int
    parameter_id : Optional[int] = None
    # parameter : Optional[Parameter] = None
    lower_limit : Optional[int] = None
    upper_limit : Optional[int] = None
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True