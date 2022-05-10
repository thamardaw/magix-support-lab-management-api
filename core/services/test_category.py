from core.protocol.test_category import TestCategoryProtocol
from core.entity.test_category import Test_Category
from core.entity.lab_test import Lab_Test
from core.entity.parameter import Parameter
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
        return self.test_category_repo.getLabTestById(id)

    def getAllLabTestByOpTestCategoryId(self,test_category_id:int) -> List[Lab_Test]:
        return self.test_category_repo.listLabTestOpTestCategoryId(test_category_id)

    def createParameter(self,parameter) -> None:
        parameter = parameter.dict()
        parameter_ranges = parameter.pop("parameter_ranges")  
        new_parameter = self.test_category_repo.persistParameter(parameter)
        for parameter_range in parameter_ranges:
            parameter_range["parameter_id"] = new_parameter.id
            self.test_category_repo.persistParameterRange(parameter_range)
        return

    def updateParameter(self,id:int,parameter) -> None:
        parameter = parameter.dict()
        parameter.pop("parameter_ranges")  
        self.test_category_repo.updateParameter(id,parameter)
        return

    def deleteParameter(self,id:int) -> None:
        try:
            self.test_category_repo.deleteParameter(id)
        except:
            raise BAD_REQUEST("Parameter cannot be deleted.")
        return

    def deleteMulitpleParameter(self,ids) -> None:
        for id in ids:
            try:
                self.test_category_repo.deleteParameter(id)
            except:
                raise BAD_REQUEST(f"Parameter with id {id} cannot be deleted.")
        return

    def getAllParameter(self) -> List[Parameter]:
        return self.test_category_repo.listParameter()

    def getParameter(self,id:int) -> Parameter:
        return self.test_category_repo.getParameterById(id)

    def getAllParameterByLabTestId(self,lab_test_id:int) -> List[Parameter]:
        return self.test_category_repo.listParameterByLabTestId(lab_test_id)

    def addParameterRange(self,parameter_id,parameter_range) -> None:
        parameter_orm = self.test_category_repo.getParameterById(parameter_id)
        parameter_range = dict(parameter_range,parameter_id=parameter_orm.id)
        self.test_category_repo.persistParameterRange(parameter_range)
        return

    def removeParameterRange(self,parameter_range_id) -> None:
        self.test_category_repo.deleteParameterRange(parameter_range_id)
        return
