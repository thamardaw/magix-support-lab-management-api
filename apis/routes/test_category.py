from fastapi import APIRouter, Depends, status
from schemas.message import Message
from schemas.test_category import Test_Category
from core.services.test_category import TestCategoryService
from core.entity.test_category import Test_Category as Test_CategoryDTO
from typing import List
from infrastructure.repository.test_category import TestCategoryRepository

router = APIRouter(prefix="/test_categorys", tags=["Test_Categorys"])

@router.get('/',status_code=status.HTTP_200_OK, response_model=List[Test_CategoryDTO])
def get_all_test_categorys(repo=Depends(TestCategoryRepository)):
    return TestCategoryService(repo).getAllTestCategory()

@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=Test_CategoryDTO)
def get_test_category(id: int, repo=Depends(TestCategoryRepository)):
    return TestCategoryService(repo).getTestCategory(id)

@router.post("/", status_code=status.HTTP_200_OK, response_model=Message)
def create_test_category(request: Test_Category, repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).createTestCategory(request)
    return {"detail": "Test Category create successful."}

@router.put("/{id}",status_code=status.HTTP_200_OK,response_model=Message)
def update_test_category(id: int, request: Test_Category,repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).updateTestCategory(id,request)
    return {"detail": "Test Category update successful."}

@router.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Message)
def delete_test_category(id: int, repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).deleteTestCategory(id)
    return {"detail": "Test Category delete successful."}

@router.post("/bulk_delete",status_code=status.HTTP_200_OK, response_model=Message)
def delete_multiple_test_categorys(ids: List[int], repo=Depends(TestCategoryRepository)):
    TestCategoryService(repo).deleteMulitpleTestCategory(ids)
    return {"detail": "Test Categorys delete successful."}
