from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Test_Category(BaseModel):
    id : int
    name : str
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True