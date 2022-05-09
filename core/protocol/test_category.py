from typing import List
from typing import Protocol
from core.entity.test_category import Test_Category as Test_CategoryDTO
from core.entity.lab_test import Lab_Test as Lab_TestDTO

class TestCategoryProtocol(Protocol):
    def persist(self,test_category) -> Test_CategoryDTO:
        ...

    def update(self,id,test_category) -> None:
        ...
    
    def list(self) -> List[Test_CategoryDTO]:
        ...
    
    def delete(self,id) -> None:
        ...
    
    def getById(self,id: int) -> Test_CategoryDTO:
        ...

    def persistLabTest(self,lab_test) -> Lab_TestDTO:
        ...

    def updateLabTest(self,id,lab_test) -> None:
        ...

    def listLabTest(self) -> List[Lab_TestDTO]:
        ...

    def listLabTestOpTestCategoryId(self,test_category_id: int) -> List[Lab_TestDTO]:
        ...

    def deleteLabTest(self,id) -> None:
        ...

    def getById(self,id: int) -> Lab_TestDTO:
        ...