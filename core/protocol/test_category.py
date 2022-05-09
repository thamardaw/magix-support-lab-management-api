from typing import List
from typing import Protocol
from core.entity.test_category import Test_Category as Test_CategoryDTO

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
