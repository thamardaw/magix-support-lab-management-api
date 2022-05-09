from pydantic import BaseModel
from typing import Optional

class Lab_Test(BaseModel):
    name : str
    test_category_id : Optional[int] = None