from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.parameter import Parameter
from schemas.parameter_range import Parameter_Range
from core.services.test_category import TestCategoryService
from core.entity.parameter import Parameter as ParameterDTO
from typing import List, Optional
from infrastructure.repository.test_category import TestCategoryRepository

router = APIRouter(prefix="/parameters", tags=["Parameters"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[ParameterDTO])
def get_all_parameters(lab_test_id: Optional[int] = None, repo=Depends(TestCategoryRepository)):
    return TestCategoryService(repo).getAllParameterByLabTestId(lab_test_id)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ParameterDTO)
def get_parameter(id: int, repo=Depends(TestCategoryRepository)):
    return TestCategoryService(repo).getParameter(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create_parameter(request: Parameter, repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).createParameter(request)
    return {"detail": "Parameter create successful."}

@router.post("/ranges/{parameter_id}", status_code=status.HTTP_200_OK, response_model=Message)
def add_parameter_range(parameter_id: int, request: Parameter_Range, repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).addParameterRange(parameter_id,request)
    return {"detail": "Parameter range added."}

@router.delete("/ranges/{parameter_range_id}",status_code=status.HTTP_200_OK, response_model=Message)
def remove_parameter_range(parameter_range_id: int, repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).removeParameterRange(parameter_range_id)
    return {"detail": "Parameter range removed."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update_parameter(id: int, request: Parameter,repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).updateParameter(id,request)
    return {"detail": "Parameter update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete_parameter(id: int, repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).deleteParameter(id)
    return {"detail": "Parameter delete successful."}

@router.post("/bulk_delete",status_code=status.HTTP_200_OK, response_model=Message)
def delete_multiple_parameters(ids: List[int], repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).deleteMulitpleParameter(ids)
    return {"detail": "Parameters delete successful."}
