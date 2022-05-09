from core.protocol.test_category import TestCategoryProtocol
from core.entity.test_category import Test_Category
from exceptions.http import BAD_REQUEST
from typing import List

class TestCategoryService:
    def __init__(self,test_category_repo:TestCategoryProtocol)->None:
        self.test_category_repo = test_category_repo
    
    def getAllTestCategory(self) -> List[Test_Category]:
        return self.test_category_repo.list()
    
    def getTestCategory(self,id:int) -> Test_Category:
        return self.test_category_repo.getById(id)
    
    def createTestCategory(self,test_category) -> None:
        self.test_category_repo.persist(test_category)
        return 
    
    def updateTestCategory(self,id:int,test_category) -> None:
        self.test_category_repo.update(id,test_category)
        return
    
    def deleteTestCategory(self,id:int) -> None:
        try:
            self.test_category_repo.delete(id)
        except:
            raise BAD_REQUEST("Test Category cannot be deleted.")
        return 

    def deleteMulitpleTestCategory(self,ids) -> None:
        for id in ids:
            try:
                self.test_category_repo.delete(id)
            except:
                raise BAD_REQUEST(f"Test Category with id {id} cannot be deleted.")
        return 