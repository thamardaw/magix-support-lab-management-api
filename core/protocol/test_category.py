from typing import List
from typing import Protocol
from core.entity.test_category import Test_Category as Test_CategoryDTO
from core.entity.lab_test import Lab_Test as Lab_TestDTO
from core.entity.parameter import Parameter as ParameterDTO
from core.entity.parameter_range import Parameter_Range as Parameter_RangeDTO

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

    def getLabTestById(self,id: int) -> Lab_TestDTO:
        ...

    def persistParameter(self,parameter) -> ParameterDTO:
        ...

    def updateParameter(self,id,parameter) -> None:
        ...

    def listParameter(self) -> List[ParameterDTO]:
        ...

    def deleteParameter(self,id) -> None:
        ...

    def getParameterById(self,id: int) -> ParameterDTO:
        ...

    def listParameterByLabTestId(self,lab_test_id: int) -> List[ParameterDTO]:
        ...

    def persistParameterRange(self,parameter_range) -> Parameter_RangeDTO:
        ...

    def updateParameterRange(self,id,parameter_range) -> None:
        ...

    def listParameterRange(self) -> List[Parameter_RangeDTO]:
        ...

    def listParameterRangeByParameterId(self,parameter_id: int) -> List[Parameter_RangeDTO]:
        ...

    def deleteParameterRange(self,id) -> None:
        ...

    def getParameterRangeById(self,id: int) -> Parameter_RangeDTO:
        ...

    

    
    
    