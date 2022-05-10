from pydantic import BaseModel
from typing import Optional, List
from infrastructure.models.parameter import result_type_enum
from .parameter_range import Parameter_Range

class Parameter(BaseModel):
    name : str
    unit : str
    lab_test_id : Optional[int] = None
    result_type : Optional[result_type_enum] = None
    result_default_text : Optional[List[str]] = None
    parameter_ranges : Optional[List[Parameter_Range]] = []