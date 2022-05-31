from pydantic import BaseModel
from typing import Optional

class Lab_Test(BaseModel):
    name : str
    test_category_id : Optional[int] = None
    test_category_name : Optional[str] = None
    show_in_report_form : Optional[bool] = None