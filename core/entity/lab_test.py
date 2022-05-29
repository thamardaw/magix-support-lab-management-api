from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .test_category import Test_Category

class Lab_Test(BaseModel):
    id : int
    name : str
    test_category_id : Optional[int] = None
    test_category_ : Optional[Test_Category] = None
    test_category_name : Optional[str] = None
    created_time: Optional[datetime] = None
    updated_time: Optional[datetime] = None
    created_user_id: Optional[int] = None
    updated_user_id: Optional[int] = None
    class Config():
        orm_mode = True