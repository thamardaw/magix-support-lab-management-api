from core.protocol.test_category import TestCategoryProtocol
from core.entity.test_category import Test_Category
from core.entity.lab_test import Lab_Test
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
        # try:
        self.test_category_repo.delete(id)
        # except:
        #     raise BAD_REQUEST("Test Category cannot be deleted.")
        # return 

    def deleteMulitpleTestCategory(self,ids) -> None:
        for id in ids:
            try:
                self.test_category_repo.delete(id)
            except:
                raise BAD_REQUEST(f"Test Category with id {id} cannot be deleted.")
        return 

    def createLabTest(self,lab_test) -> None:
        self.test_category_repo.persistLabTest(lab_test)
        return

    def updateLabTest(self,id:int,lab_test) -> None:
        self.test_category_repo.updateLabTest(id,lab_test)
        return

    def deleteLabTest(self,id:int) -> None:
        try:
            self.test_category_repo.deleteLabTest(id)
        except:
            raise BAD_REQUEST("Lab Test cannot be deleted.")
        return

    def deleteMulitpleLabTest(self,ids) -> None:
        for id in ids:
            try:
                self.test_category_repo.deleteLabTest(id)
            except:
                raise BAD_REQUEST(f"Lab Test with id {id} cannot be deleted.")
        return

    def getAllLabTest(self) -> List[Lab_Test]:
        return self.test_category_repo.listLabTest()

    def getLabTest(self,id:int) -> Lab_Test:
        return self.test_category_repo.getById(id)

    def getAllLabTestByOpTestCategoryId(self,test_category_id:int) -> List[Lab_Test]:
        return self.test_category_repo.listLabTestOpTestCategoryId(test_category_id)
