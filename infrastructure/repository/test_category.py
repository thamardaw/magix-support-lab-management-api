from typing import List
from infrastructure.base_repo import BaseRepo
from infrastructure.models.test_category import Test_Category
from infrastructure.models.lab_test import Lab_Test
from core.entity.test_category import Test_Category as Test_CategoryDTO
from core.entity.lab_test import Lab_Test as Lab_TestDTO
from exceptions.repo import SQLALCHEMY_ERROR
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_

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

    def persistLabTest(self,lab_test) -> Lab_TestDTO:
        new_lab_test = Lab_Test(**lab_test.dict())
        new_lab_test = self.create(new_lab_test)
        return Lab_TestDTO.from_orm(new_lab_test)

    def updateLabTest(self,id,lab_test) -> None:
        lab_test_orm = self.read(Lab_Test,id)
        if type(lab_test) is dict:
            super().update(lab_test_orm,lab_test)
        else:
            super().update(lab_test_orm,lab_test.dict())
        return

    def listLabTest(self) -> List[Lab_TestDTO]:
        lab_tests = self.read_all(Lab_Test)
        return [Lab_TestDTO.from_orm(lab_test) for lab_test in lab_tests]

    def listLabTestOpTestCategoryId(self,test_category_id: int) -> List[Lab_TestDTO]:
        try:
            lab_tests = self._db.query(Lab_Test).filter(or_(test_category_id == None,Lab_Test.test_category_id == test_category_id))\
                .order_by(Lab_Test.id.desc()).all()
            return [Lab_TestDTO.from_orm(lab_test) for lab_test in lab_tests]
        except SQLAlchemyError as e:
            raise SQLALCHEMY_ERROR(e)

    def deleteLabTest(self,id) -> None:
        self.read(Lab_Test,id)
        super().delete(Lab_Test,id)
        return 

    def getById(self,id: int) -> Lab_TestDTO:
        lab_test_orm = self.read(Lab_Test,id)
        return Lab_TestDTO.from_orm(lab_test_orm)
