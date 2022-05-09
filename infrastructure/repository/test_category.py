from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.test_category import Test_Category
from core.entity.test_category import Test_Category as Test_CategoryDTO

class TestCategoryRepository(BaseRepo):
    def persist(self,test_category) -> Test_CategoryDTO:
        new_test_category = Test_Category(**test_category.dict())
        new_test_category = self.create(new_test_category)
        return Test_CategoryDTO.from_orm(new_test_category)
    
    def update(self,id,test_category) -> None:
        test_category_orm = self.read(Test_Category,id)
        if type(test_category) is dict:
            super().update(test_category_orm,test_category)
        else:
            super().update(test_category_orm,test_category.dict())
        return

    def list(self) -> List[Test_CategoryDTO]:
        test_categorys = self.read_all(Test_Category)
        return [Test_CategoryDTO.from_orm(test_category) for test_category in test_categorys]
    
    def delete(self,id) -> None:
        self.read(Test_Category,id)
        super().delete(Test_Category,id)
        return 
        
    def getById(self,id: int) -> Test_CategoryDTO:
        test_category_orm = self.read(Test_Category,id)
        return Test_CategoryDTO.from_orm(test_category_orm)
