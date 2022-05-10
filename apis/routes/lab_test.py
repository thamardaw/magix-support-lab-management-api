from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.lab_test import Lab_Test
from core.services.test_category import TestCategoryService
from core.entity.lab_test import Lab_Test as Lab_TestDTO
from typing import List, Optional
from infrastructure.repository.test_category import TestCategoryRepository

router = APIRouter(prefix="/lab_tests", tags=["Lab Tests"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[Lab_TestDTO])
def get_all_lab_tests(test_category_id: Optional[int] = None,repo=Depends(TestCategoryRepository)):
    return TestCategoryService(repo).getAllLabTestByOpTestCategoryId(test_category_id)

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=Lab_TestDTO)
def get_lab_test(id: int, repo=Depends(TestCategoryRepository)):
    return TestCategoryService(repo).getLabTest(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Lab_TestDTO)
def create_lab_test(request: Lab_Test, repo=Depends(TestCategoryRepository)):
    return TestCategoryService(repo).createLabTest(request)

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update_lab_test(id: int, request: Lab_Test,repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).updateLabTest(id,request)
    return {"detail": "Lab Test update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete_lab_test(id: int, repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).deleteLabTest(id)
    return {"detail": "Lab Test delete successful."}

@router.post("/bulk_delete",status_code=status.HTTP_200_OK, response_model=Message)
def delete_multiple_lab_tests(ids: List[int], repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).deleteMulitpleLabTest(ids)
    return {"detail": "Lab Tests delete successful."}
